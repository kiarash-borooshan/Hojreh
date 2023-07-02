from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import IRN_adm1, Incidences
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.


@login_required(login_url="account:login_em")
def home_page_view_dashboard(TemplateView):
    template_name = "index.html"
    return render(TemplateView,
                  "GeoSpatial/em_dashboard.html")


def county_datasets(request):
    counties = serialize("geojson", IRN_adm1.objects.all())
    return HttpResponse(counties, content_type="json")


def point_dataset(request):
    points = serialize("geojson", Incidences.objects.all())
    return HttpResponse(points, content_type="json")
