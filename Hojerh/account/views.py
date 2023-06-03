from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import RegisterForm, RegisterProfileForm
from .models import Profile


def register_user(request: HttpRequest):

    if request.method == "POST":

        """ register user """
        form = RegisterForm(request.POST)
        profile_form = RegisterProfileForm(request.POST, files=request.FILES)

        if form.is_valid() and profile_form.is_valid():

            cd = form.cleaned_data
            pcd = profile_form.cleaned_data

            user: User = form.save()
            # user.set_password(cd['password'])
            # user.save()

            profile = Profile.objects.get(user=user)
            profile.photo = pcd['photo']
            profile.phone_number = pcd['phone_number']
            profile.save()

            return HttpResponse("Created account")

    else:
        form = RegisterForm()
        profile_form = RegisterProfileForm()

    return render(request,
                  'account/register.html',
                  {'form': form,
                   'profile_form': profile_form})
