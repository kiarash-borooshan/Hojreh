from . import views
from django.urls import path

# app_name = 'account'

urlpatterns = [
    path("register", views.register_user)
]