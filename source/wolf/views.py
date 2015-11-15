import json, uuid
from django import shortcuts
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.safestring import mark_safe

from hackerrank import api
from grabbers import test_grabbers
from wolf.models import *
from wolf import models

def serialize_tests_to_json(tests):
    # todo: find a proper way to simply serialize a list of my objects
    return json.dumps( [ t.__dict__ for t in tests ] )
        
def index(request):
    return HttpResponse("")

def templates(request):
    templates = models.Template.objects.all()
    return render(request, 'wolf/templates.html', {
        'templates': templates,
    })

def template_edit(request, templateId):
    template = shortcuts.get_object_or_404(models.Template, pk = templateId)
    if 'code' in request.POST:
        template.code = request.POST['code']
        template.save()
    return render(request, 'wolf/templates-edit.html', {
        'template': template,
    })
    
def parse(request):
    if 'url' in request.POST:
        url = request.POST['url']
        test_grabber = next(g for g in test_grabbers.available_grabbers if g.can_grab_from(url))
        tests = test_grabber.grab_tests(url)
        template = models.Template.objects.all()[0]
        
        solution = Solution.objects.create(code = template.code, tests = serialize_tests_to_json(tests))
        
        return redirect('wolf:solve', solutionId = solution.id)
    else:
        return render(request, 'wolf/parse.html', {
        })
    
def solve(request, solutionId):
    solution = get_object_or_404(Solution, pk = solutionId)
    return render(request, 'wolf/solve.html', {
        'code': solution.code,
        'tests': solution.tests,
        'solutionId': solutionId,
    })

def update_solution(id, code, jsTests):
    solution = Solution.objects.get(pk = id)
    solution.code = code
    solution.tests = jsTests
    
    solution.save()
    
def run(request, solutionId):
    code = request.POST['code']
    
    jsTests = request.POST['tests']
    tests = data.Test.from_json_str(jsTests)
    
    input = [ t.input for t in tests ]
    expected_output = [ t.output for t in tests ]
    
    update_solution(solutionId, code, jsTests)
    
    language = api.HR_LANGUAGE.CPP
    execution_result = api.runCode(language, code, input)
    
    result = [data.SubmissionResult(expected == actual, actual).__dict__ for (actual, expected) in zip(execution_result, expected_output)]
    
    return HttpResponse(json.dumps(result))