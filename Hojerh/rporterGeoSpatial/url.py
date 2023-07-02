from . import views
from django.urls import path

app_name = "rporterGeoSpatial"

urlpatterns = [
    path("homeSpatialDashboard/", views.home_page_view_dashboard, name="em_dashboard"),
    path("county_data/", views.county_datasets, name="country"),
    path("incident_data/", views.point_dataset, name="incident"),
]
