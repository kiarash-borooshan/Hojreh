from django.shortcuts import render


def register_user(request):
    return render(request,
                  'account/register.html')
