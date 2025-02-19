from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm


def register(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def profile(request):
    return render(request, 'profile.html', {'user': request.user})