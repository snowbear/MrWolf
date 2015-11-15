from wolf import models, views
from wolf.tests.views import common

class Views_Solve_Tests(common.ViewTestBase):
    def test_can_be_rendered(self):
        solution = models.Solution.objects.create()
        request = self.request_get('wolf:solve', [ solution.id ])
        views.solve(request, solution.id)
