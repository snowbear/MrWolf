from wolf import views
from wolf.tests.views import common


class Tests(common.ViewTestBase):
    def test_can_be_rendered(self):
        request = self.request_get('wolf:index', [])
        views.index(request)
