# Generated by Django 4.2.2 on 2023-07-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0024_order_order_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="pdf_filepath",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]