from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput,TextInput
from django.contrib.auth.models import User
from django import forms
from applications.models import Task
#User Sign Up
class Sign_Up_Form(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

#User Login
class Login_Form(AuthenticationForm):
    username=forms.CharField(widget=TextInput)
    password=forms.CharField(widget=PasswordInput)

#Create Task
class Create_Task(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','content',]
        exclude=['user',]






