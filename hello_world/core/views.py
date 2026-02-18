from django.shortcuts import render
from django.http import HttpRequest

def index(request: HttpRequest):
    context = {
        "title": "Password Checker",
        "subtitle": "Created for UofU CS3090",
        "description": "This is a password checker that checks the strength of a password and provides feedback on how to improve it."
    }
    return render(request, "index.html", context)
