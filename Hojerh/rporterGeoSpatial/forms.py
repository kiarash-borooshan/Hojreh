from django import forms
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.utils.text import slugify

from .models import Incidences


class NewEmPostForm(forms.ModelForm):
    class Meta:
        model = Incidences
        exclude = ["user", "slug"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "input"}),
            "geo_tag_photo": forms.FileInput(attrs={"class": "input"}),
            "date": forms.DateInput(attrs={"class": "input"}),
            "variety": forms.TextInput(attrs={"class": "input"}),
            "health_status": forms.TextInput(attrs={"class": "input"}),
            "disease_name": forms.TextInput(attrs={"class": "input"}),
            "solution": forms.Textarea(attrs={"class": "input"}),

        }

    def save(self, comit: bool, request):
        post: Incidences = super().save(commit=False)
        cd = self.cleaned_data
        title = cd["name"]
        post.slug = slugify(title)
        post.user = request.user

        if comit:
            post.save()

        return post
