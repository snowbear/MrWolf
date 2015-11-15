from django.test import *
from grabbers.test_grabbers import *

from wolf import data

class CfGrabberTests(SimpleTestCase):
    def test_parsing(self):
        grabber = CfTestGrabber()
        
        valid_urls = [
            ( "http://codeforces.com/contest/597/problem/A" ,
                [ data.Test( "1 1 10" , "10" ) , data.Test( "2 -4 4" , "5" ) ] ),
            ( "http://codeforces.com/contest/514/problem/E" ,
                [ data.Test( "3 3\n1 2 3" , "8" ) ] ),
        ]
        
        for (url, expected_tests) in valid_urls:
            self.assertTrue(grabber.can_grab_from(url))
            grabbed_tests = grabber.grab_tests(url)
            self.assertEqual(grabbed_tests, expected_tests) 