from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         widgets = {
#             "username": forms.TextInput(attrs={'class': 'form-control mb-3'}),
#             "email": forms.EmailInput(attrs={'class': 'form-control mb-3'}),
#             "password": forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
#         }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
                    "username": forms.TextInput(attrs={'class': 'form-control mb-3'}),
                    "email": forms.EmailInput(attrs={'class': 'form-control mb-3'}),
                    "password1": forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
                    "password2": forms.PasswordInput(attrs={'class': 'form-control mb-6'}),
                }


class RegisterProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'photo': forms.FileInput(attrs={'class': 'form-control mb-3'}),
        }
