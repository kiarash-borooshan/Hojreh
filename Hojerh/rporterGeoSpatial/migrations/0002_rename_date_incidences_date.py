# Generated by Django 4.2.1 on 2023-07-03 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rporterGeoSpatial', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incidences',
            old_name='date',
            new_name='Date',
        ),
    ]