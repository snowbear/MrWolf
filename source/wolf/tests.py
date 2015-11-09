import json
from django.test import SimpleTestCase
from django.test.client import RequestFactory
from unittest.mock import *
from wolf.models import *
from wolf import views

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
