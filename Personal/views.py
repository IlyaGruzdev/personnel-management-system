from django.shortcuts import render

# Create your views here.
def profile(request, username):
  return render(request, 'personal/profile.html')