from django.shortcuts import render
from django.http import HttpRequest

def say_hello(request):
    return HttpRequest('hello world')

# Create your views here.
