# Generated by Django 4.2.2 on 2023-06-26 00:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0008_order_order_dimension_order_weight"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="weight",
            field=models.IntegerField(null=True),
        ),
    ]
