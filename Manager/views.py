from django.shortcuts import render
from django.contrib.sitemaps import Sitemap
from django.http import HttpRequest
from .forms import LoginForm, RegisterForm
from .models import *
from django import forms
from django.core.exceptions import ValidationError

def index(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            username = registerForm.cleaned_data['username']
            email = registerForm.cleaned_data['email']
            password = registerForm.cleaned_data['password']

            CustomUser.objects.create(username=username, email=email, password=password)
            registerForm = RegisterForm()  # Сброс формы после успешного создания пользователя
        else:
            print(registerForm.errors)
    else:
        registerForm = RegisterForm()

    loginForm = LoginForm()
    return render(request, 'index.html', context={'loginform': loginForm, 'registerform': registerForm})

def register(request):
  return render(request, 'p.html')



