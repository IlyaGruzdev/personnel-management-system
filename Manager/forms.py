from django import forms
from .models import *

class LoginForm(forms.Form):
  login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-styling'}))
  password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-styling', 'type': 'password', 'name': 'password', 'id': 'logpass'}))
  check = forms.CharField(widget=forms.TextInput(attrs={'type': 'checkbox', 'id': 'checkbox'}))

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-styling', 'type': 'text'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-styling', 'type': 'email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-styling', 'type': 'password'}) )
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-styling', 'type': 'password'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data