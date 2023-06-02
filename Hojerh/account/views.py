from django.shortcuts import render
from .forms import RegisterForm


def register_user(request):
    form = RegisterForm()
    return render(request,
                  'account/register.html',
                  {'form': form})
