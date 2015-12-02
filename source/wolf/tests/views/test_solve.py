from wolf import views
from wolf.tests import model_mocks
from wolf.tests.views import common


class Tests(common.ViewTestBase):
    def test_can_be_rendered(self):
        solution = model_mocks.mock_solution()
        request = self.request_get('wolf:solve', [solution.id])
        views.solve(request, solution.id)
