import json
import requests
from django.conf import settings
from enum import IntEnum


class CompilationError:
    def __init__(self, error):
        self.error = error


class HR_LANGUAGE(IntEnum):
    CPP = 2


def run_code(language, code, input):
    url = "http://api.hackerrank.com/checker/submission.json"

    response = requests.post(url,
                             data={
                                 "source": code,
                                 "lang": int(language),
                                 "testcases": json.dumps(input),
                                 "api_key": settings.HACKERRANK_API_KEY,
                             },
                             )
    result = json.loads(response.text)['result']

    compile_message = result['compilemessage']
    if compile_message != '':
        return CompilationError(compile_message)

    return result['stdout']
