# Generated by Django 2.2.7 on 2019-12-18 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DDB', '0002_remove_releases_hardwaresupport'),
    ]

    operations = [
        migrations.AddField(
            model_name='releases',
            name='EngineerCount',
            field=models.IntegerField(default=1),
        ),
    ]