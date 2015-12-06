from django.test import *
from grabbers.test_grabbers import *
from django_site import testing
import ddt

from wolf import data


@ddt.ddt
class CfGrabberTests(SimpleTestCase):
    @ddt.data(
        ("http://codeforces.com/contest/597/problem/A",
         [data.Test("1 1 10", "10"), data.Test("2 -4 4", "5")]),
        ("http://codeforces.com/contest/514/problem/E",
         [data.Test("3 3\n1 2 3", "8")]),
    )
    @ddt.unpack
    @testing.test_category('slow')
    def test_parsing(self, url, expected_tests):
        grabber = CfTestGrabber()

        self.assertTrue(grabber.can_grab_from(url))
        grabbed_tests = grabber.grab_tests(url)
        self.assertEqual(grabbed_tests, expected_tests)
