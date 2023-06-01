from django.contrib.auth.models import User
from django.db import models
"""" cannot recogniza """
# from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="profile")
    # phone_number = PhoneNumberField(blank=True)
    phone_number = models.CharField(blank=True, null=True)
    photo = models.ImageField(null=True, blank=True)
