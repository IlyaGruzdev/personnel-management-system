from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
# Create your views here.
def profile(request, username):
  return render(request, 'personal/profile.html')

def getPersonal(request):
    results = int(request.POST.get('results', 50))
    users = CustomUser.objects.all().values('username', 'email', 'avatar', 'date_joined')[:results]

    return JsonResponse({'data': list(users)}, safe=False)
