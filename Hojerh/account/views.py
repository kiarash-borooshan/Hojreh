from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm, RegisterProfileForm, LoginForm
from .models import Profile


def register_user(request: HttpRequest):

    if request.method == "POST":

        # send data to server
        """ register user """
        form = RegisterForm(request.POST)
        profile_form = RegisterProfileForm(request.POST, files=request.FILES)

        if form.is_valid() and profile_form.is_valid():

            # cd = form.cleaned_data
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


def login_user(request: HttpRequest):

    password_msg = None
    user_msg = None

    if request.method == "POST":
        l_form = LoginForm(data=request.POST)

        if l_form.is_valid():
            cd = l_form.cleaned_data

            email = cd["email"]
            password = cd["password"]

            try:
                user: User = User.objects.get(email=email)

                if user.check_password(password):
                    login(request, user)
                    return HttpResponse("Dashboard")
                else:
                    password_msg = "password is not match "
            except User.DoesNotExist:
                user_msg = "email is not valid"

    else:
        l_form = LoginForm()

    context = {"form": l_form,
               "password_msg": password_msg,
               "user_msg": user_msg}

    return render(request,
                  "account/login.html",
                  context)


def logout_user(request):

    logout(request)

    return redirect("ToysApp:index")
