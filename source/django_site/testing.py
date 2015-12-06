import unittest
from django.test import runner


def test_category(category_name):
    def inner(f):
        setattr(f, category_name, True)
        return f
    return inner


class TestLoader(unittest.TestLoader):
    fast_only = False

    def getTestCaseNames(self, testcase_class):
        decorator_name = 'slow'

        def is_fast(attr_name):
            fn = getattr(testcase_class, attr_name)
            if hasattr(fn, decorator_name):
                return False
            return True

        res = super().getTestCaseNames(testcase_class)
        if self.fast_only:
            res = list(filter(is_fast, res))
        return res


class DiscoverRunner(runner.DiscoverRunner):
    test_loader = TestLoader()

    @classmethod
    def add_arguments(cls, parser):
        parser.add_argument('-f', '--fast_only', action='store_true', dest='fast_only',
                            default=False,
                            help='Run only fast unit tests')
        super().add_arguments(parser)

    def __init__(self, fast_only=False, **kwargs):
        super().__init__(**kwargs)
        self.test_loader.fast_only = fast_only
