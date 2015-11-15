import json
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.test import SimpleTestCase
from django.test.client import RequestFactory
from unittest.mock import *

from wolf import views, data
from wolf.models import *

class Views_Parse_Tests(SimpleTestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

    def test_can_be_rendered_when_no_url_provided(self):
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