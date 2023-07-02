# Generated by Django 4.2.2 on 2023-06-26 01:44

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0014_driver_driver_neighborhood_driver_driver_region"),
    ]

    operations = [
        migrations.AlterField(
            model_name="business",
            name="business_region",
            field=smart_selects.db_fields.ChainedForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app.region",
            ),
        ),
    ]
