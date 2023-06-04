from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"category: {self.name}"


class GenderType(models.Model):
    name = models.CharField()

    def __str__(self):
        return f" gender: {self.name}"


class Ages(models.Model):
    age = models.TextField()

    def __str__(self):
        return f"age: {self.age}"


class Toys(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="user",
                             blank=True, null=True)

    name = models.CharField(max_length=255)
    code = models.TextField()

    # box_size = models.IntegerField(blank=True, null=True)

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name="category_toys",
                                 blank=True, null=True)

    gender = models.ForeignKey(GenderType,
                               on_delete=models.CASCADE,
                               related_name="gender_toys",
                               blank=True, null=True)

    age = models.ForeignKey(Ages,
                            on_delete=models.CASCADE,
                            related_name="age_toys",
                            blank=True, null=True)

    banner = models.ImageField(null=True, blank=True)

    body = models.TextField()
    
    video_link = models.TextField(null=True, blank=True)

    available = models.BooleanField()

    date = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField()

    def __str__(self):
        return f"toys: {self.name}"
