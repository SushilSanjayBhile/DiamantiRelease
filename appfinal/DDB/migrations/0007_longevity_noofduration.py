# Generated by Django 3.0 on 2020-02-12 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DDB', '0006_auto_20200212_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='longevity',
            name='NoOfDuration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
