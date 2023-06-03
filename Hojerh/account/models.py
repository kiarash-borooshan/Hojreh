from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

"""" !!! cannot recognize """
# from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="profile")
    # phone_number = PhoneNumberField(blank=True)
    phone_number = models.CharField(blank=True, null=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    user = kwargs.get('instance')
    created = kwargs.get('created')

    if created:
        profile = Profile(user=user)
        profile.save()
