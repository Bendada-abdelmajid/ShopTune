# Generated by Django 4.1.7 on 2023-03-17 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0004_categorys_main_cat_categorys_sub_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='maincat',
            name='slug',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
