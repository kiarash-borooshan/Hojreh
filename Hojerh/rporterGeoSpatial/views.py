from django.core.serializers import serialize
from django.http import HttpResponse
from .models import IRN_adm1, Incidences
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.


def home_page_view(TemplateView):
    template_name = "index.html"
    return render(TemplateView,
                  "GeoSpatial/index.html")


def county_datasets(request):
    counties = serialize("geojson", IRN_adm1.objects.all())
    return HttpResponse(counties, content_type="json")


def point_dataset(request):
    points = serialize("geojson", Incidences.objects.all())
    return HttpResponse(points, content_type="json")