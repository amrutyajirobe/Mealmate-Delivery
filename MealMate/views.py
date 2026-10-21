from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello(request):
    return render(request, 'delivery/index.html')


def open_signup(request):
    return render(request, 'delivery/signup.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        mobile = request.POST.get('mobile', '').strip()
        address = request.POST.get('address', '').strip()

        # Check for required fields
        if not username or not password:
            return render(request, 'delivery/signup.html', {
                'error': 'Username and password are required.'
            })

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'delivery/signup.html', {
                'error': f"User '{username}' already exists. Please choose a different username or log in."
            })

        # Check if email is already registered
        if email and User.objects.filter(email=email).exists():
            return render(request, 'delivery/signup.html', {
                'error': f"An account with email '{email}' already exists. Please log in."
            })

        # Create the new user
        User.objects.create_user(username=username, email=email, password=password)
        return HttpResponse("Sign up successful!")

    # If the request method is GET, render the signup page
    return render(request, 'delivery/signup.html')


def open_signin(request):
    return render(request, 'delivery/signin.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username or not password:
            return render(request, 'delivery/signin.html', {
                'error': 'Please provide both username and password.'
            })

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(f"Sign in successful! Welcome, {user.username}.")
        else:
            return render(request, 'delivery/signin.html', {
                'error': 'Invalid username or password. Please try again.'
            })

    # If the request method is GET, render the signin page
    return render(request, 'delivery/signin.html')
