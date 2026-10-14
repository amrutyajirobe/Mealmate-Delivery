from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello(request):
    return render(request, 'delivery/index.html')


def open_signup(request):
    return render(request, 'delivery/signup.html')


def open_signin(request):
    return render(request, 'delivery/signin.html')
