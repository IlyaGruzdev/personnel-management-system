from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sitemaps import Sitemap
from django.http import HttpRequest
from django.http import JsonResponse
from .forms import LoginForm, RegisterForm, ProjectForm
from .models import *
from django.contrib.auth import logout
from django.core.exceptions import ValidationError
from django.contrib import messages, sessions
from django.db import transaction
import json

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
                        if(user.is_manager):
                            try:
                                manager=user.manager 
                            except:
                                manager=Manager.objects.create(user=user)
                                manager.save()
                                print("created manager")
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
        context={}
        try:
            user = CustomUser.objects.get(username=request.session['user'])
        except CustomUser.DoesNotExist:
            user = None
        if user:
            user_url = user.get_absolute_url()
        else:
            user_url=None
        registerForm = RegisterForm()             
        loginForm = LoginForm()
        context = {'loginform': loginForm, 'registerform': registerForm, 'user': user, 'user_url': user_url}
        return render(request, 'index.html', context=context)

def log_out(request):
    logout(request)
    return redirect('home')
    
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    projectForm = ProjectForm()
    user_url = user.get_absolute_url()
    projects = user.manager.projects.all()
    return render(request, 'manager/profile.html', context={'user': user, 'projectform': projectForm, 'user_url': user_url, 'projects': projects})

def postCreating(request):
    if(request.session):
        user = CustomUser.objects.get(username=request.session['user'])
        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            personal_list = request.POST.getlist('personal_list')  # Замените 'excluded_field_name' на имя поля, которое вы хотите исключить
            print(personal_list)
            if 'personal_list' in form.fields:
                del form.fields['personal_list']
            if form.is_valid():
                cleaned_data = form.cleaned_data
                print(cleaned_data)
                if 'personal_list' in cleaned_data:
                    del cleaned_data['personal_list']
                project=Project(**cleaned_data)   
                personalArr = []
                for item in personal_list:
                    item = item.strip()
                    try:
                        list_item =PersonalList(price = cleaned_data['duration']*personal_price[item], category = item)
                        personalArr.append(list_item)
                    except Exception as e:
                        return JsonResponse({'error': str(e)}, status=400)
                
                try:
                    with transaction.atomic():
                        project.save()
                        user.manager.projects.add(project)
                        for item in personalArr:
                            item.save() 
                            project.personal_list.add(item)  # Добавляем personalArr к проекту
                except Exception as e:
                    return JsonResponse({'error': str(e)}, status=400)
            else:
                return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'success': 'successifuly created'})

def getProject(request, project_id, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return JsonResponse({'error': 'User not found'})
    
    if ('user' in request.session and request.session['user'] == user.username):
        try:
            project = user.manager.projects.get(id=project_id)
        except Project.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        serialized_project = json.dumps({
            'name': project.name,
            'event': project.event,
            'id': project.id,
        })
        return JsonResponse({'project': serialized_project})
    else:
        return JsonResponse({'error': 'You are not in the current session'})
    
def projectShow(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    user = get_object_or_404(CustomUser, username=request.session['user'])
    managers = project.managers.all()
    personal = project.personal.all() 
    return render(request, 'manager/project.html', context={'project': project, 'managers': managers, 'personal': personal, 'user': user})