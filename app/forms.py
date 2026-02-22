from dataclasses import fields
from xml.parsers.expat import model
from django.forms import ModelForm, Form, EmailField, CharField, PasswordInput
from .models import Blog

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))



class UserSignupForm(UserCreationForm):
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput)


class Blog3Form(ModelForm):
    class Meta:
        model=Blog
        fields='__all__'



