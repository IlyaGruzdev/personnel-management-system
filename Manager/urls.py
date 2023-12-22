from django.urls import path, re_path, include
from Manager import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

  path("accounts/", include("django.contrib.auth.urls")),  
  path('logout/', views.log_out, name = 'logout'),
  re_path(r'profile/(?P<username>[\w+ ./]+)/', views.profile, name='manager_profile'),
  path('post/creating/', views.postCreating, name='post_creating'),
  path('get/project/<int:project_id>/user/<int:user_id>/', views.getProject, name='get_project'),
  path('progect/<int:project_id>/user/<int:user_id>', views.projectShow, name='project_show')
]
