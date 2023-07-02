# Generated by Django 4.2.2 on 2023-06-29 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0022_shipmentstatus_shipment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shipment",
            name="driver",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.driver",
            ),
        ),
    ]