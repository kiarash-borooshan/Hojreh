from . import views
from django.urls import path

app_name = 'ToysApp'

urlpatterns = [
    path("donyaye koodakan/", views.index_toys, name="index"),
    path("categories/<str:category>/<slug:slug>", views.detail_toys, name='toy_detail'),
    path("donyaye koodakan categories/", views.categories_toys, name='categories')
]
