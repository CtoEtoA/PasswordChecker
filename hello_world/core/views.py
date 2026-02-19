from django.shortcuts import render
from django.http import HttpRequest
from .forms import PasswordCheckForm
from .utils import check_password

def index(request: HttpRequest):
    error = ''
    success = ''
    context = {
        "title": "Password Checker",
        "subtitle": "Created for UofU CS3090",
        "description": "This is a password checker that checks the strength of a password and provides feedback on how to improve it.",
        "subdescription": "This should not be used with real passwords, as it is only a demonstration and does not implement any security measures.",
    }

    if request.method == 'POST':
        form = PasswordCheckForm(request.POST)
        if form.is_valid():
            pwd = form.cleaned_data.get('password', '')
            ok, message = check_password(pwd)
            if ok:
                success = message or 'Strong Password!'
            else:
                error = message or 'Weak password'
    else:
        form = PasswordCheckForm()

    return render(
        request,
        'index.html',
        {
            'form': form,
            'error': error,
            'success': success,
            'context': context
        }
    )
