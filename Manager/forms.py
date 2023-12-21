from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import *
from .models import *

class LoginForm(forms.Form):
  type=forms.CharField(initial="login", widget = forms.TextInput(attrs={'type': 'hidden'}))
  login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-styling', 'autocomplete': 'off'}))
  password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-styling', 'type': 'password', 'name': 'password', 'autocomplete': 'off', 'id':'logpassword'}))
  check = forms.CharField(widget=forms.TextInput(attrs={'type': 'checkbox', 'id': 'checkbox'}), required=False)

class RegisterForm(forms.Form):
    type=forms.CharField(widget = forms.HiddenInput(), initial="register")
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-styling'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-styling'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-styling'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-styling'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
    
class ProjectForm(forms.ModelForm):
    event = forms.ChoiceField(choices=TYPES_OF_EVENTS)
    personal_list=forms.MultipleChoiceField(choices = TYPES_OF_PERSONAL, widget=forms.SelectMultiple(attrs={'size': '5'}))
    class Meta:
        model = Project
        fields = ['name', 'brief', 'photo', 'event', 'start_date', 'duration', 'personal_list']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Input project name'}),
            'brief': forms.Textarea(attrs={'class': 'field', 'rows': 7, 'cols': 20, 'placeholder': 'Input brief'}),
            'photo': forms.FileInput(attrs={'class': 'field', 'placeholder': 'Change project photo'}),
            'start_date': forms.DateInput(attrs={'class': 'field', 'placeholder': 'Input start project date', 'type': 'date'}),
            'duration': forms.NumberInput(attrs={'class': 'field', 'placeholder': 'Input project duration in hours', 'type': 'number'}),
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs['enctype'] = 'multipart/form-data'

