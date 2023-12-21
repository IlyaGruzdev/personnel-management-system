from django.urls import path, re_path, include
from Personal import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
  re_path(r'profile/(?P<username>[\w+ ./]+)/', views.profile, name='personal_profile')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
document_root=settings.MEDIA_ROOT