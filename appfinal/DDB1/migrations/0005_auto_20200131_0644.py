# Generated by Django 3.0 on 2020-01-31 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DDB', '0004_auto_20200131_0643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_info',
            old_name='Name',
            new_name='name',
        ),
    ]
