# Generated by Django 4.1.7 on 2023-04-15 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0017_review_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]