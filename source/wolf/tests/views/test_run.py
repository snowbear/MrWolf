import json
from unittest import mock

from wolf import models, views
from wolf.tests.views import common
from hackerrank import api


class Tests(common.ViewTestBase):
    def test_run_updatesSolution(self):
        solution = models.Solution.objects.create(code='', tests='')

        new_code = 'new code'
        new_tests = [{"input": "2 1", "output": "4"}]

        views.api.run_code = mock.MagicMock(return_value=['3'])
        views.compare_result = mock.MagicMock(return_value=False)

        data = {'code': new_code, 'tests': json.dumps(new_tests)}
        request = self.request_post('wolf:run', args=[solution.id], data=data)
        result = json.loads(views.run(request, solution.id).content.decode())

        updated_solution = models.Solution.objects.get(pk=solution.id)
        self.assertEqual(updated_solution.code, new_code)
        self.assertEqual(json.loads(updated_solution.tests), new_tests)

        self.assertEqual(result, {
            'compiled': True,
            'result': [{
                'successful': False,
                'output': '3',
            }],
        })

    def test_run_compilationError(self):
        solution = models.Solution.objects.create()

        code = 'some code'
        tests = [{"input": "", "output": ""}]

        compilation_error = 'ce'

        views.api.run_code = mock.MagicMock(return_value=api.CompilationError(compilation_error))

        request = self.request_post('wolf:run', args=[solution.id], data={'code': code, 'tests': json.dumps(tests)})

        result = json.loads(views.run(request, solution.id).content.decode())

        self.assertDictEqual(result, {
            'compiled': False,
            'compilation_error': compilation_error,
        })
