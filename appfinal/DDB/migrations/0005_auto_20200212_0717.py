# Generated by Django 3.0 on 2020-02-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DDB', '0004_auto_20200211_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='stress',
            name='LinkFlap',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='stress',
            name='NoOfIteration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]