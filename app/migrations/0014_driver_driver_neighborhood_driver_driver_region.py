# Generated by Django 4.2.2 on 2023-06-26 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0013_business_business_neighborhood_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="driver",
            name="driver_neighborhood",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app.neighborhood",
            ),
        ),
        migrations.AddField(
            model_name="driver",
            name="driver_region",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app.region",
            ),
        ),
    ]
