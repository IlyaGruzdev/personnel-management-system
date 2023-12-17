from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sitemaps import Sitemap
from django.http import HttpRequest
from django.http import JsonResponse
from .forms import LoginForm, RegisterForm
from .models import *
from django.contrib.auth import logout
from django.core.exceptions import ValidationError
from django.contrib import messages, sessions

def index(request):
    print(request.POST)
    if request.method == 'POST':
        if(request.POST.get("type")=="register"):
            registerForm = RegisterForm(request.POST)
            if registerForm.is_valid():
                username = registerForm.cleaned_data['username']
                email = registerForm.cleaned_data['email']
                password = registerForm.cleaned_data['password']
                if CustomUser.objects.filter(username=username).exists():
                    return JsonResponse({'error': 'username is already exist'}, status = 400)
                else:
                    CustomUser.objects.create(username=username, email=email, password=password)
                    request.session['user'] = username
                    registerForm = RegisterForm()
                    return JsonResponse({'message': 'data was saved'})
            else:
                print(registerForm.errors)
                errors=dict(registerForm.errors)
                return JsonResponse({'errors': errors}, status = 400)
        elif(request.POST.get("type")=="login"):
            print("post")
            loginForm=LoginForm(request.POST)
            if loginForm.is_valid():
                login = loginForm.cleaned_data['login']
                password = loginForm.cleaned_data['password']
                remember_me = loginForm.cleaned_data['check']
                try:
                    user=CustomUser.objects.get(username=login)
                    if(user.password==password):
                        if not remember_me:
                            request.session['user']=user.username
                            request.session.set_expiry(60)
                        else:
                            request.session['user']=user.username
                        return JsonResponse({'message': 'data was saved'})
                    else:
                        return JsonResponse({'error': f'password {password} does not confirm'}, status = 400)
                    
                except:
                    return JsonResponse({'error': f'login {login} does not exist'}, status = 400)
            else:
                return JsonResponse({'errors': loginForm.errors}, status = 400)
        else:
            return JsonResponse({'error': f'wrong {loginForm.cleaned_data["type"]}'}, status = 400)


    else:
        
        if('user' in request.session):
            user = CustomUser.objects.get(username=request.session['user']) 
        else:
            user=None
        registerForm = RegisterForm()             
        loginForm = LoginForm()
        context = {'loginform': loginForm, 'registerform': registerForm, 'user': user}
        return render(request, 'index.html', context=context)

def log_out(request):
    logout(request)
    return redirect('home')
    
def profile(request, username):
  user = get_object_or_404(CustomUser, username=username)
  return render(request, 'manager/profile.html', context={'user': user})



