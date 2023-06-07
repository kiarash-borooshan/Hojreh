from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileDecore(admin.ModelAdmin):
    list_display = ("user", "phone_number")

