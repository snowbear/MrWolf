import json
from django import http, shortcuts

from hackerrank import api
from grabbers import test_grabbers
from wolf import data, models
from wolf.result_checker import compare_result


def serialize_tests_to_json(tests):
    # todo: find a proper way to simply serialize a list of my objects
    return json.dumps([t.__dict__ for t in tests])


def index(request):
    return http.HttpResponse("")


def templates(request):
    templates_to_show = models.Template.objects.all()
    return shortcuts.render(request, 'wolf/templates.html', {
        'templates': templates_to_show,
    })


def template_edit(request, template_id):
    template = shortcuts.get_object_or_404(models.Template, pk=template_id)
    if request.method == 'POST':
        template.code = request.POST['code']
        new_language_id = int(request.POST['language_id'])
        template.language = models.Language.objects.get(pk=new_language_id)
        template.save()
    return shortcuts.render(request, 'wolf/templates-edit.html', {
        'template': template,
        'languages': models.Language.objects.all(),
    })


def parse(request):
    if 'url' in request.POST:
        url = request.POST['url']
        test_grabber = next(g for g in test_grabbers.available_grabbers if g.can_grab_from(url))
        tests = test_grabber.grab_tests(url)
        template = models.Template.objects.all()[0]
        
        solution = models.Solution.objects.create(
            code=template.code,
            language=template.language,
            tests=serialize_tests_to_json(tests),
        )
        
        return shortcuts.redirect('wolf:solve', solution_id=solution.id)
    else:
        return shortcuts.render(request, 'wolf/parse.html', {
        })


def solve(request, solution_id):
    solution = shortcuts.get_object_or_404(models.Solution, pk=solution_id)
    return shortcuts.render(request, 'wolf/solve.html', {
        'code': solution.code,
        'tests': solution.tests,
        'solution_id': solution_id,
    })


def update_solution(solution_id, code, js_tests):
    solution = models.Solution.objects.get(pk=solution_id)
    solution.code = code
    solution.tests = js_tests
    
    solution.save()


def run(request, solution_id):
    code = request.POST['code']

    js_tests = request.POST['tests']
    tests = data.Test.from_json_str(js_tests)
    
    tests_input = [t.input for t in tests]
    expected_output = [t.output for t in tests]
    
    update_solution(solution_id, code, js_tests)
    
    language = api.HR_LANGUAGE.CPP
    execution_result = api.run_code(language, code, tests_input)

    if type(execution_result) is api.CompilationError:
        return http.JsonResponse({
            'compiled': False,
            'compilation_error': execution_result.error,
        })

    result = [data.SubmissionResult(compare_result(actual, expected), actual).__dict__
              for (actual, expected) in zip(execution_result, expected_output)]
    
    return http.JsonResponse({
        'compiled': True,
        'result': result,
    })
