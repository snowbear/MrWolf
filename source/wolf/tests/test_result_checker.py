import unittest
from ddt import ddt, data, unpack
from wolf import result_checker


@ddt
class TestResultChecker(unittest.TestCase):
    @data(
        ('test', 'test', True),
        ('test1 and test2', 'test1 and test2', True),
        ('test', 'test\n', True),
        ('test1', 'test2', False),
        ('test1   and   test2', 'test1 and test2', True),
          )
    @unpack
    def test_ignores_whitespaces(self, output, compare_to, expected_result):
        outcome = result_checker.compare_result(output, compare_to)
        self.assertEqual(outcome, expected_result)
