# Generated by Django 4.1.7 on 2023-03-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0010_pruduct_oldprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pruduct',
            name='oldprice',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pruduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
