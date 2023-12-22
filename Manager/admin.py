from django.contrib import admin
from django.contrib import auth
from .models import *

# Register your models here.
admin.site.register(Manager)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    exclude = None
    list_filter = ['is_active', 'date_joined', 'username']
    search_fields = ['date_joined', 'username', 'email']
    date_hierarchy = 'date_joined'
    ordering = ['is_active', 'date_joined', 'username']
    fieldsets = [
        (None, {'fields': ['username', 'email', 'password'], "classes": ["wide", "extrapretty"]}),
        ('Personal info', {'fields': ['first_name', 'last_name', 'avatar'],  "classes": ["collapse", "wide", "extrapretty"]}),
        ('Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser']}), 
    ]

@admin.register(PersonalList)
class PersonalListAdmin(admin.ModelAdmin):
    list_display = ['price', 'category']
    search_fields = ['price', 'category']
    ordering = ['category', 'price']
    list_filter = ['category']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    exclude = ['public_date']
    list_display = ['name', 'brief', 'event', 'start_date', 'duration']
    filter_horizontal = ['personal_list']
    fieldsets = [
        (None, {'fields': ['name', 'brief', 'photo'], "classes": ["wide", "extrapretty"]}),
        ('Event info', {'fields': ['event', 'start_date', 'duration']}),
        ('Personal list', {'fields': ['personal_list']}),
    ]