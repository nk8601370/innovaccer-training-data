from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django.db import models 
from django import forms 

class CustomRegistrationForm(UserCreationForm): 
    # password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput) 
    class Meta: 
        model = User 
        fields = ['username', 'email', 'first_name', 'last_name'] 
        # labels = {'email':'Email'} 