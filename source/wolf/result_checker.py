def trim_whitespaces(s):
    return ' '.join(s.split())


def compare_result(actual, expected):
    return trim_whitespaces(actual) == trim_whitespaces(expected)
