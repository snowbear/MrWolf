import json, uuid
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe

from hackerrank import api
from wolf.models import *

class SubmissionResult:
    def __init__(self, successful, output):
        self.successful = successful
        self.output = output

def index(request):
    return HttpResponse("")

def solve(request, solutionId):
    solution = get_object_or_404(Solution, pk = solutionId)
    return render(request, 'wolf/solve.html', {
        'code': solution.code,
        'tests': solution.tests,
        'solutionId': solutionId,
    })

def update_solution(id, code, tests):
    solution = Solution.objects.get(pk = id)
    solution.code = code
    solution.tests = json.dumps(tests)
    
    solution.save()
    
def run(request, solutionId):
    code = request.POST['code']
    
    tests = json.loads(request.POST['tests'])
    
    input = [ t['input'] for t in tests ]
    expected_output = [ t['output'] for t in tests ]
    
    update_solution(solutionId, code, tests)
    
    language = api.HR_LANGUAGE.CPP
    execution_result = api.runCode(language, code, input)
    
    result = [SubmissionResult(expected == actual, actual).__dict__ for (actual, expected) in zip(execution_result, expected_output)]
    
    return HttpResponse(json.dumps(result))