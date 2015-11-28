from django import test
from django.core import urlresolvers
from django.test.client import RequestFactory


class ViewTestBase(test.TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

    def request_get(self, view_name, args):
        url = urlresolvers.reverse(view_name, args=args)
        return self.request_factory.get(url)
        
    def request_post(self, view_name, args=None, data=None):
        url = urlresolvers.reverse(view_name, args=args)
        return self.request_factory.post(url, data)
