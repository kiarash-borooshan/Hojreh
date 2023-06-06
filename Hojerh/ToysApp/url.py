from . import views
from django.urls import path

app_name = 'ToysApp'

urlpatterns = [
    path("donyaye koodakan/", views.index_toys, name="index"),
    path("categories/<str:category>/<slug:slug>/", views.detail_toys, name='toy_detail'),
    path("categories/<str:category>/<slug:slug>/share/", views.share_post, name='toy_share_post'),
    path("categories/<str:category>/<slug:slug>/share/send/", views.send_post, name='toy_send_post'),
    path("donyaye koodakan categories/", views.categories_toys, name='categories')
]
