from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Incidences, IRN_adm1
# Register your models here.


@admin.register(Incidences)
class IncidenceDecor(LeafletGeoAdmin):
    list_display = ("name", "location")


@admin.register(IRN_adm1)
class CountiesDecor(LeafletGeoAdmin):
    list_display = ("name_1", "varname_1")

