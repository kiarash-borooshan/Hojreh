from django.contrib.auth.models import User
from django.db import models
# from taggit.managers import TaggableManager
from django.urls import reverse


#  create manager
class ToysManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(available=True)


class Category(models.Model):
    name = models.CharField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.name


class GenderType(models.Model):
    name = models.CharField()

    objects = models.Manager()

    def __str__(self):
        return self.name


class Ages(models.Model):
    age = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.age


class Toys(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="user",
                             blank=True, null=True)

    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, 
                             blank=True, null=True)
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

    banner = models.ImageField(upload_to='Toys/media', null=True, blank=True)

    body = models.TextField()
    
    video_link = models.TextField(null=True, blank=True)

    # tags = TaggableManager()

    available = models.BooleanField()

    date = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField()

    objects = models.Manager()

    available_post = ToysManager()

    def get_absolute_url(self):
        return reverse("ToysApp:toy_detail",
                       args=[self.category.name, self.slug])

    def __str__(self):
        return self.name
