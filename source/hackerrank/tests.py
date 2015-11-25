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
        
        input = ["5 6"]
        
        result = run_code(HR_LANGUAGE.CPP, code, input)
        
        self.assertEqual(result, ["11"])

    def test_cpp_ce(self):
        code = """some code that doesn't compile"""
        input = [""]

        result = run_code(HR_LANGUAGE.CPP, code, input)

        self.assertIsInstance(result, CompilationError)
