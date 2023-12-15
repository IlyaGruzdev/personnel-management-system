from django import forms
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