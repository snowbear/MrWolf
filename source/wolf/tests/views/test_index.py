import json
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.test import SimpleTestCase
from django.test.client import RequestFactory
from unittest.mock import *

from wolf import views, data
from wolf.models import *

class Views_Index_Tests(SimpleTestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

    def test_can_be_rendered(self):
        request = self.request_factory.get('/')
        views.index(request)
