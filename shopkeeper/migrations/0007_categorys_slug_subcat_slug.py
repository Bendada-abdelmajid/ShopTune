# Generated by Django 4.1.7 on 2023-03-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0006_alter_maincat_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorys',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subcat',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
