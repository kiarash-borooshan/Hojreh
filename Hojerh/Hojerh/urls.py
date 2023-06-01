from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('core.url', namespace='core')),
    path("auth/", include('account.url')),
]
