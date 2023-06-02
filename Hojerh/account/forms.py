from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control mb-3'}),
            "email": forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            "password": forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
        }
