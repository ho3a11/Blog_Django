from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm


# Form for user login.
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


# Form for new user registration.
class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    repassword = forms.CharField()

