from django.shortcuts import render

def index(request):
    context = {
        "title": "Password Checker",
        "subtitle": "Created for UofU CS3090",
        "description": "This is a password checker that checks the strength of a password and provides feedback on how to improve it."
    }
    return render(request, "index.html", context)
