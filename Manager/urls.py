from django.urls import path, re_path, include
from Manager import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

  path("accounts/", include("django.contrib.auth.urls")),  
  path('logout/', views.log_out, name = 'logout'),
  re_path(r'profile/(?P<username>[\w+ ./]+)/', views.profile, name='manager_profile'),
  path('post/creating/', views.PostCreating, name='post_creating')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
document_root=settings.MEDIA_ROOT