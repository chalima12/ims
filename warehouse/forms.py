from django import forms
from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError

class UserForm(ModelForm):
    # user_name=forms.EmailField(widget=forms.EmailInput,label='Your Email')
    # pass_word=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['first_name','last_name','user_name','password','user_type','email']
        widgets={
             'first_name':forms.TextInput(attrs={'class':"form-control form-control"
                                                 ,'placeholder':'Enter First Name'}),
             'last_name':forms.TextInput(attrs={'class':"form-control form-control",'placeholder':'Enter Last Name' }),
             'email':forms.EmailInput(attrs={'class':"form-control form-control",'placeholder':'Enter user Email'}),
             
             'user_name':forms.TextInput(attrs={'class':"form-control form-control",'placeholder':'Enter username'}),
             'password':forms.PasswordInput(attrs={'class':"form-control form-control",'placeholder':'Enter user password'}),
             "user_type": forms.Select(attrs={"class": "form-control",'placeholder':'Select User type'}),
        }
    def clean_username(self):
        user_name = self.cleaned_data.get('user_name')
        if User.objects.filter(user_name=user_name).exists():
            raise ValidationError("Username already exists")
        return user_name

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
# forms.py

from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
