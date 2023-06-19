from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('core.url', namespace='core')),
    path("account/", include('account.url')),
    path("toys/", include('ToysApp.url', namespace="ToysApp")),
    path("spatial/", include("rporterGeoSpatial.url", namespace="reporterGeoSpatial"))
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
