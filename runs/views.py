from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .models import User, Run, Test, Environment, Status


def index(request):
    if request.method == 'GET':
        return render_template(request)

    elif request.method == 'POST':
        errors = validate_post(request)
        if not errors:
            run = Run()

            try:
                user = User.objects.get(
                        name=request.POST.get('user_name').lower())
            except User.DoesNotExist:
                user = User()
                user.name = request.POST.get('user_name').lower()
                user.save()

            try:
                test = Test.objects.get(
                        name=request.POST.get('test_name').lower())
            except Test.DoesNotExist:
                test = Test()
                test.name = request.POST.get('test_name').lower()
                test.save()

            try:
                environment = Environment.objects.get(
                        description=request.POST.get('test_env'))
            except Environment.DoesNotExist:
                environment = Environment()
                environment.description = request.POST.get('test_env').lower()
                environment.save()

            run.user = user
            run.test = test
            run.environment = environment
            run.status = Status.objects.get(value="waiting")
            run.save()

            return render_template(request, success=True)
        else:
            return render_template(request, errors=errors)
    else:
        return HttpResponseBadRequest()


def updated_runs(request):
    """
    Returns the table with the current runs updated. This is required for the
    automatic update on the browser.
    """
    runs_list = Run.objects.all()
    context = {}
    context['runs_list'] = runs_list
    return render(request, 'runs/runs_table.html', context)


def render_template(request, errors=[], success=None):
    runs_list = Run.objects.all()
    envs_list = Environment.objects.all()
    context = {}
    context['runs_list'] = runs_list
    context['envs_list'] = envs_list
    if errors:
        context['errors'] = errors
    if success:
        context['success'] = success

    return render(request, 'runs/index.html', context)


def validate_post(request):
    errors = []
    if len(request.POST.get('user_name')) == 0:
        errors.append("A user name must be specified.")

    if len(request.POST.get('test_name')) == 0:
        errors.append("A test name must be specified.")

    if len(request.POST.get('test_env')) == 0:
        errors.append("A test environment must be specified.")

    return errors
