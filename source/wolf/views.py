import json, uuid
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.safestring import mark_safe

from hackerrank import api

class SubmissionResult:
    def __init__(self, successful):
        self.successful = successful

def index(request):
    return HttpResponse("")

def solve(request):
    return render(request, 'wolf/solve.html', {
    })

def run(request):
    code = request.POST['code']
    input = json.loads(request.POST['input'])
    expected_output = json.loads(request.POST['output'])
    language = api.HR_LANGUAGE.CPP
    execution_result = api.runCode(language, code, input)
    
    result = [SubmissionResult(expected == actual).__dict__ for (expected, actual) in zip(execution_result, expected_output)]
    
    return HttpResponse(json.dumps(result))