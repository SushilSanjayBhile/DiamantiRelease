# Generated by Django 2.2.7 on 2019-12-18 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DDB', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='releases',
            name='HardwareSupport',
        ),
    ]
