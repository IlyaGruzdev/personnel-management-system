from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils import timezone
import os

# Create your models here.
TYPES_OF_EVENTS = [
  ("personal", "personal on event"),
  ("visiting", "organizing a visiting"),
  ("cleaning", "cleaning"),
  ("auto", "auto events"),
  ("development", "development events"),
  ("security", "event security"),
  ("exhibition", "exhibition services"),
  ("moving", "moving events"),
  ("trucking", "trucking on events"),
  ("parcking", "parking organization"),
  ("photography", "event photography"),
  ("analisis", "data analysis events"),
  ("web design", "web design events"),
  ("svg Animations", "svg animations events"),
  ("ui development", "ui development events"),
  ("testing", "testing events")
]
personal_price = {
   "nurses": 300, "orderlies": 300, "paramedics": 350, "copying and duplicating machine operators": 250,
"security guards": 500, "carpenters": 300, "auxiliary workers": 250, "doormens": 450, "promo-models": 750, "promoters": 500, "loaders": 250, "laborers": 300,
 "promo-personal": 400, "security": 400, "cleaners": 250, "supervisors": 600, "barmens": 1200, "waiters": 700, "drivers": 1000, "parking attendants": 550, "delivers": 350, 
 "temporary staff": 350, "coordinators": 800, "helpers": 250, "animators": 100, "models for presentation": 3000
}
personal_types = ["Not changed", "nurses", "orderlies", "paramedics", "copying and duplicating machine operators",
"security guards", "carpenters", "auxiliary workers", "doormens", "promo-models", "promoters", "loaders", "laborers",
 "promo-personal", "security", "cleaners", "supervisors", "barmens", "waiters", "drivers", "parking attendants", "delivers", 
 "temporary staff", "coordinators", "helpers", "animators", "models for presentation"
 ]
TYPES_OF_PERSONAL = sorted([(item, item) for item in personal_types])

def get_upload_path(instance, filename):
    current_date = timezone.now().strftime("%Y-%m-%d")
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
  def get_absolute_url(self):
      if self.is_personal:
        return reverse("personal_profile", kwargs={"username": self.username})
      elif self.is_manager:
        return reverse("manager_profile", kwargs={"username": self.username})
  def __str__(self):
    return self.username
 

class PersonalList(models.Model):
  price = models.PositiveIntegerField(validators=[MinValueValidator(250), MaxValueValidator(100000)])
  category = models.CharField(max_length=100, choices = TYPES_OF_PERSONAL, default = TYPES_OF_PERSONAL[0])

class Project(models.Model):
  name = models.CharField(max_length=50)
  brief = models.TextField(default="", verbose_name='Краткое описание')
  photo=models.ImageField(null=True, blank=True, upload_to=get_upload_path, default='no_avatar.jpg')
  event = models.CharField(max_length=50, choices = TYPES_OF_EVENTS, default=TYPES_OF_EVENTS[0])
  public_date = models.DateField(auto_now_add=True)
  start_date = models.DateField(default=timezone.now)
  duration = models.PositiveSmallIntegerField(validators = [MinValueValidator(1), MaxValueValidator(10000)], default = 24)
  personal_list = models.ManyToManyField(PersonalList, related_name = "projects")
  def progress(self):
    now = timezone.localdate()
    delta_time = now - self.start_date
    return int((self.duration * 3600 - delta_time.total_seconds()) / (self.duration * 3600)) * 100
  def days_left(self):
    delta_time = timezone.localdate() - self.start_date
    return delta_time.days

class Manager(models.Model):
  projects = models.ManyToManyField(Project, related_name='managers')
  user = models.OneToOneField(CustomUser, related_name='manager', on_delete=models.CASCADE, primary_key=True)


class Message(models.Model):
  message = models.TextField()
  public_date = models.DateTimeField(auto_now_add = True)
  user = models.ForeignKey(CustomUser, related_name='messages', on_delete=models.DO_NOTHING)
  project = models.ForeignKey(Project, null=True, blank = True, related_name='messages', on_delete=models.CASCADE)
  def __str__(self):
    return self.message



