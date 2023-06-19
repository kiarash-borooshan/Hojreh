# from django.db import models
from django.contrib.gis.db import models


class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Incidences'


class IRN_adm1(models.Model):
    id_0 = models.BigIntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    id_1 = models.BigIntegerField()
    name_1 = models.CharField(max_length=75)
    type_1 = models.CharField(max_length=50)
    engtype_1 = models.CharField(max_length=50)
    nl_name_1 = models.CharField(max_length=50, blank=True, null=True)
    varname_1 = models.CharField(max_length=150, blank=True, null=True)
    geom = models.MultiPolygonField()

    objects = models.Manager()

    def __str__(self):
        return self.name_1

    class Meta:
        verbose_name = 'counties'
