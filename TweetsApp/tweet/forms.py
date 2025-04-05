from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','photo'] #from Tweet model

class UserRegistrationForm(UserCreationForm): #default form from django
    email=forms.EmailField() #extra field to be added to the default User model
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')
