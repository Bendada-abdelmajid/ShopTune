# Generated by Django 4.1.7 on 2023-04-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0012_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pruduct',
            name='oldprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
