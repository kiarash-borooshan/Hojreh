from . import views
from django.urls import path

app_name = 'ToysApp'

urlpatterns = [
    path("DonyayeKoodakan/", views.index_toys)
]
