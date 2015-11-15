import json
from unittest import mock

from wolf import models, views
from wolf.tests.views import common

class Views_Run_Tests(common.ViewTestBase):        
    def test_run_updatesSolution(self):
        solution = models.Solution.objects.create(code = '', tests = '')
        
        new_code = 'new code'
        new_tests = [ { "input" : "2 1" , "output" : "4" } ]
        
        views.api.runCode = mock.MagicMock(return_value = [ "3" ])
        
        request = self.request_post('wolf:run', args = [ solution.id ], data = { 'code': new_code , 'tests': json.dumps(new_tests) })
        views.run(request, solution.id)
        
        updated_solution = models.Solution.objects.get(pk = solution.id)
        self.assertEqual(updated_solution.code, new_code)
        self.assertEqual(json.loads(updated_solution.tests), new_tests)
