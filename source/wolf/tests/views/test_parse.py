from django.core import urlresolvers
from unittest import mock

from wolf import data, models, views
from wolf.tests.views import common

class Views_Parse_Tests(common.ViewTestBase):
    def test_can_be_rendered_when_no_url_provided(self):
        request = self.request_get('wolf:parse', [])
        views.parse(request)
        
    def init_post_request(self):
        self.url = "some url"
        self.request = self.request_post('wolf:parse', data = { 'url': self.url })
        
    def test_uses_first_suitable_grabber(self):    
        self.init_post_request()
    
        grabber1 = mock.Mock()
        grabber1.can_grab_from = mock.MagicMock(return_value = False)
        
        grabber2 = mock.Mock()
        grabber2.can_grab_from = mock.MagicMock(return_value = True)
        grabber2.grab_tests = mock.MagicMock(return_value = [])
                
        views.test_grabbers.available_grabbers = [ grabber1 , grabber2 ]
        
        models.Template.objects.create(code = 'my code')

        views.parse(self.request)
        
        grabber2.grab_tests.assert_called_with(self.url)
    
    def test_creates_solution_and_redirects(self):
        self.init_post_request()
    
        tests = [ data.Test("input", "output") ]
    
        grabber = mock.Mock()
        grabber.can_grab_from = mock.MagicMock(return_value = True)
        grabber.grab_tests = mock.MagicMock(return_value = tests)
        
        views.test_grabbers.available_grabbers = [ grabber ]
        
        template = models.Template.objects.create(code = 'my code')
        
        response = views.parse(self.request)
        
        redirect_url_match = urlresolvers.resolve(response.get('location'))
        
        self.assertEqual(redirect_url_match.func, views.solve)
        newSolutionId = int(redirect_url_match.kwargs['solutionId'])
        
        newSolution = models.Solution.objects.get(pk = newSolutionId)
        self.assertEqual(newSolution.getParsedTests(), tests)
        self.assertEqual(newSolution.code, template.code)