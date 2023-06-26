from ToysApp.models import Toys
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.messages import add_message, SUCCESS, WARNING
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm, RegisterEmForm, RegisterProfileForm, RegisterEmProfileForm, \
    LoginForm, \
    ProfileEditForm, UserEditForm, PasswordEditForm, \
    DeleteForm, ThemeForm
from .models import Profile


def register_user(request: HttpRequest):
    """ register Kbarcode user """
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

            """ message """
            add_message(request, SUCCESS,
                        "ثبت‌نام شما با موفقیت انجام شد، اکنون میتوانید به صفحه Log in بروید",
                        "notification is-success",
                        fail_silently=True)

            return redirect("account:login")

    else:
        form = RegisterForm()
        profile_form = RegisterProfileForm()

    return render(request,
                  'account/register.html',
                  {'form': form,
                   'profile_form': profile_form})


def register_user_em(request: HttpRequest):
    """ register ErthMntr user"""
    if request.method == "POST":

        # send data to server
        """ register user """
        form = RegisterEmForm(request.POST)
        profile_form = RegisterEmProfileForm(request.POST, files=request.FILES)

        if form.is_valid() and profile_form.is_valid():

            # cd = form.cleaned_data
            pcd = profile_form.cleaned_data

            user: User = form.save()
            # user.set_password(cd['password'])
            # user.save()

            profile = Profile.objects.get(user=user)
            # profile.photo = pcd['photo']
            profile.phone_number = pcd['phone_number']
            profile.save()

            """ message """
            add_message(request, SUCCESS,
                        "ثبت‌نام شما با موفقیت انجام شد، اکنون میتوانید به صفحه Log in بروید",
                        "notification is-success",
                        fail_silently=True)

            return redirect("account:login")

    else:
        form = RegisterEmForm()
        profile_form = RegisterEmProfileForm()

    return render(request,
                  'account/register_em.html',
                  {'em_form': form,
                   'em_profile_form': profile_form})


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

                    add_message(request, SUCCESS,
                                "شما به اکانت خود وارد شدید",
                                "notification is-success",
                                True)
                    return redirect("account:dashboard")
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


def login_em_user(request: HttpRequest):

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

                    add_message(request, SUCCESS,
                                "شما به اکانت خود وارد شدید",
                                "notification is-success",
                                True)
                    return redirect("rporterGeoSpatial:home")
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
                  "account/login_em.html",
                  context)


def logout_user(request):

    logout(request)

    add_message(request, WARNING,
                "شما از پنل کاربری خود خارج شدید",
                "notification is-warning", True)

    return redirect("ToysApp:index")


@login_required()
def dashboard(request):
    available_post = Toys.available_post.filter()
    # available_post = Toys.objects.all()
    unavailable_post = Toys.unavailable_post.filter()
    if request.method == "POST":
        theme_form = ThemeForm(instance=request.user.profile, data=request.POST)
        if theme_form.is_valid():
            theme_form.save(commit=True)
            return redirect("account:dashboard")
    else:
        theme_form = ThemeForm(instance=request.user.profile, data=request.POST)

    context = {"av_post": available_post,
               "un_av_post": unavailable_post,
               "form": theme_form
               }

    return render(request,
                  'account/dashboard.html',
                  context)


@login_required()
def edit_info(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            add_message(request,
                        SUCCESS,
                        "تغییرات با موفقیت انجام شد",
                        "notification is-success", True)
            return redirect("account:dashboard")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {"form": user_form,
               "profile_form": profile_form}
    return render(request,
                  "account/edit_info.html",
                  context)


@login_required()
def edit_password(request):
    if request.method == "POST":
        ps_form = PasswordEditForm(data=request.POST)
        if ps_form.is_valid():
            cd = ps_form.cleaned_data

            if request.user.check_password(cd['old_password']):
                if cd['new_password'] == cd["new_password2"]:
                    request.user.set_password(cd["new_password"])
                    request.user.save()
                    add_message(request, SUCCESS,
                                "your password has changed",
                                "notification is-success", True)
                    return redirect("account:dashboard")
    else:
        ps_form = PasswordEditForm()
    return render(request,
                  "account/change_password.html",
                  {"form": ps_form})


@login_required()
def delete_account(request):
    if request.method == "POST":
        form = DeleteForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if request.user.check_password(password):
                request.user.delete()
                add_message(request, WARNING,
                            "your account deleted",
                            "notification is-danger", True)
                return redirect("ToysApp:index")
            else:
                add_message(request, WARNING,
                            "your password is wrong",
                            "notification is-danger", True)
    else:
        form = DeleteForm()
    return render(request, 'account/delete_account.html',
                  {"form": form})
