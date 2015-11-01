from django.test import SimpleTestCase
from hackerrank.api import *

class ApiTests(SimpleTestCase):
    def test_cpp_valid(self):
        code = """
#include <iostream>

using namespace std;

int main() {
	int a, b;
	cin >> a >> b;
	cout << a + b;
}
        """
        
        input = [ "5 6" ]
        
        result = runCode(HR_LANGUAGE.CPP, code, input)
        
        self.assertEqual(result, [ "11" ])
