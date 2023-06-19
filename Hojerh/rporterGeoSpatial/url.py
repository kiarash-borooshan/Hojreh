from . import views
from django.urls import path

app_name = "rporterGeoSpatial"

urlpatterns = [
    path("homeSpatial/", views.home_page_view, name="home"),
    path("county_data/", views.county_datasets, name="country"),
    path("incident_data/", views.point_dataset, name="incident"),
]
