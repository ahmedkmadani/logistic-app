# Generated by Django 4.2.2 on 2023-06-25 13:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_order_order_pdf_path"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="order_pdf_path",
        ),
    ]
