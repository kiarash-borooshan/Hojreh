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
                    "username": forms.TextInput(attrs={'class': 'input',
                                                       "placeholder": "نام مغازه خود را وارد فرمایید"}),
                    "email": forms.EmailInput(attrs={'class': 'input',
                                                     "placeholder": "ایمیل خود را وارد فرمایید"}),
                    "password1": forms.PasswordInput(attrs={'class': 'input',
                                                            "placeholder": "پسورد"}),
                    "password2": forms.PasswordInput(attrs={'class': 'input',
                                                            "placeholder": "تکرار پسورد"}),
                }

        labels = {
            "username": "نام مغازه",
            "email": "ایمیل",
            "password1": "رمز",
            "password2": "تکرار رمز"
        }


class RegisterProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'input',
                                                   "placeholder": "شماره موبایل: به عنوان مثال ۰۹۳۳۴۲۲۷۶۷۹"}),
            'photo': forms.FileInput(attrs={'class': 'input',
                                            "placeholder": "تصویری از مغازه خود را بارگذاری کنید"}),

        }

        labels = {
            "photo": "تصویری از مغازه خود بارگذاری فرمایید"
        }


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "input"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input"})
    )


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            "username": forms.TextInput(attrs={'class': 'input',
                                               "placeholder": "نام مغازه خود را وارد فرمایید"}),
            "email": forms.EmailInput(attrs={'class': 'input',
                                             "placeholder": "ایمیل خود را وارد فرمایید"})
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'input',
                                                   "placeholder": "شماره موبایل: به عنوان مثال ۰۹۳۳۴۲۲۷۶۷۹"}),


        }

        labels = {
            "photo": "تصویری از مغازه خود بارگذاری فرمایید"
        }
