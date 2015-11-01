import json, requests
from django.conf import settings
from enum import IntEnum

class HR_LANGUAGE(IntEnum):
	CPP = 2    
    
def runCode(language, code, input):
    url = "http://api.hackerrank.com/checker/submission.json"
    
    response = requests.post(url,
        data = {
            "source": code,
            "lang": int(language),
            "testcases": json.dumps(input),
            "api_key": settings.HACKERRANK_API_KEY,
        },
    )
    result = json.loads(response.text)['result']
    
    return result['stdout']