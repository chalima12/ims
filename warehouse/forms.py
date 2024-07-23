from django import forms
from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
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
    
    
    
class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'profile_picture']    

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Current Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'}))


from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
# forms.py
from django import forms
from django.forms import modelformset_factory
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['stock', 'quantity', 'order_date', 'status']
        widgets = {
            'stock': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'order_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

OrderFormSet = modelformset_factory(Order, form=OrderForm, extra=5, can_delete=True)


class MaterialRequestForm(forms.ModelForm):
    class Meta:
        model = MaterialRequest
        user=User.objects.all()
        fields = ['user', 'item', 'request_date', 'status']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'item': forms.Select(attrs={'class': 'form-control'}),
            'request_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

