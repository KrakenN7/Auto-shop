# Generated by Django 4.2.16 on 2024-11-05 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_cars_carspecifications_delete_product_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="carspecifications",
            name="type_engine",
            field=models.CharField(default="бензин", max_length=12),
        ),
    ]
