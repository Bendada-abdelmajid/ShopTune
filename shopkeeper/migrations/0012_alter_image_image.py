# Generated by Django 4.1.7 on 2023-04-04 23:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0011_alter_pruduct_oldprice_alter_pruduct_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]