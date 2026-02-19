from django.shortcuts import render
from django.http import HttpRequest
from .forms import PasswordCheckForm
from .utils import check_password  # optional separate checker

def index(request: HttpRequest):
    context = {
        "title": "Password Checker",
        "subtitle": "Created for UofU CS3090",
        "description": "This is a password checker that checks the strength of a password and provides feedback on how to improve it."
    }
    error = ''
    if request.method == 'POST':
        form = PasswordCheckForm(request.POST)
        if form.is_valid():
            pwd = form.cleaned_data['password']
            ok, message = check_password(pwd)  # implement this
            if not ok:
                error = message
            else:
                error = ''  # or set success message
    else:
        form = PasswordCheckForm()
    return render(request, 'index.html', {'form': form, 'error': error, 'context': context})