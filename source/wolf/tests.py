import json
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.test import SimpleTestCase
from django.test.client import RequestFactory
from unittest.mock import *

from wolf import views, data
from wolf.models import *

class ViewTests(SimpleTestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

    def test_index_can_be_rendered(self):
        request = self.request_factory.get('/')
        views.index(request)
    
    def test_solve_view_can_be_rendered(self):
        solution = Solution.objects.create()
        request = self.request_factory.get('/solve/' + str(solution.id))
        views.solve(request, solution.id)
    
    def test_run_updatesSolution(self):
        solution = Solution.objects.create(code = '', tests = '')
        
        new_code = 'new code'
        new_tests = [ { "input" : "2 1" , "output" : "4" } ]
        
        views.api.runCode = MagicMock(return_value = [ "3" ])
        
        request = self.request_factory.post('/run/' + str(solution.id), { 'code': new_code , 'tests': json.dumps(new_tests) })
        views.run(request, solution.id)
        
        updated_solution = Solution.objects.get(pk = solution.id)
        self.assertEqual(updated_solution.code, new_code)
        self.assertEqual(json.loads(updated_solution.tests), new_tests)

class Views_Parse_Tests(SimpleTestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

    def test_view_with_no_parameter(self):
        request = self.request_factory.get('/parse')
        views.parse(request)
        
    def init_post_request(self):        
        self.url = "some url"
        self.request = self.request_factory.post('/parse', { 'url': self.url })
        
    def test_uses_first_suitable_grabber(self):    
        self.init_post_request()
    
        grabber1 = Mock()
        grabber1.can_grab_from = MagicMock(return_value = False)
        
        grabber2 = Mock()
        grabber2.can_grab_from = MagicMock(return_value = True)
        grabber2.grab_tests = MagicMock(return_value = [])
                
        views.test_grabbers.available_grabbers = [ grabber1 , grabber2 ]
        views.parse(self.request)
        
        grabber2.grab_tests.assert_called_with(self.url)
    
    def test_creates_solution_and_redirects(self):
        self.init_post_request()
    
        tests = [ data.Test("input", "output") ]
    
        grabber = Mock()
        grabber.can_grab_from = MagicMock(return_value = True)
        grabber.grab_tests = MagicMock(return_value = tests)
        
        views.test_grabbers.available_grabbers = [ grabber ]
        response = views.parse(self.request)
        
        redirect_url_match = urlresolvers.resolve(response.get('location'))
        
        self.assertEqual(redirect_url_match.func, views.solve)
        newSolutionId = int(redirect_url_match.kwargs['solutionId'])
        
        newSolution = Solution.objects.get(pk = newSolutionId)
        self.assertEqual(newSolution.getParsedTests(), tests)