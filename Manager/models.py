from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
import os
from datetime import datetime

# Create your models here.

def get_upload_path(instance, filename):
    current_date = datetime.now().strftime("%Y-%m-%d")
    return os.path.join("uploads", current_date, filename)

class CustomUser(AbstractUser):
  is_personal = models.BooleanField(default = False)
  is_manager = models.BooleanField(default = False)
  avatar=models.ImageField(null=True, blank=True, upload_to=get_upload_path, default='no_avatar.jpg')
  def clean(self):
    if(self.is_personal and self.is_manager):
      raise ValidationError("User cannot be both Manager and Personal")

  def clean_fields(self, exclude=None):
    if self.is_personal and self.is_manager:
      if 'is_personal' not in exclude and 'is_manager' not in exclude:
        raise ValidationError("User cannot be both Personal and Manager")
    return super().clean_fields(exclude)


class Project(models.Model):
  name = models.CharField(max_length=50)
  brief = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
  photo=models.ImageField(null=True, blank=True, upload_to=get_upload_path, default='no_avatar.jpg')
  public_date = models.DateField(auto_now_add=True)

class Personal(models.Model):
  raiting = models.SmallIntegerField(MaxValueValidator(100), default=60)
  projects = models.ManyToManyField(Project, related_name='personal')
  user = models.OneToOneField(CustomUser, related_name='personal', on_delete=models.CASCADE,primary_key=True)

class Manager(models.Model):
  projects = models.ManyToManyField(Project, related_name='managers')
  user = models.OneToOneField(CustomUser, related_name='manager', on_delete=models.CASCADE, primary_key=True)




