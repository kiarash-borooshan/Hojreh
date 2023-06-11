from . import views
from django.urls import path

app_name = 'account'

urlpatterns = [
    path("register", views.register_user, name="register"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("dashboard/edit_info", views.edit_info, name="edit_info"),
]
