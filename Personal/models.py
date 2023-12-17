from django.db import models
from Manager.models import *
# Create your models here.
class Personal(models.Model):
  raiting = models.SmallIntegerField(MaxValueValidator(100), default=60)
  projects = models.ManyToManyField(Project, related_name='personal')
  user = models.OneToOneField(CustomUser, related_name='personal', on_delete=models.CASCADE,primary_key=True)
