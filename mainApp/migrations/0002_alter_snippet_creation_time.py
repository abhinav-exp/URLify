# Generated by Django 4.0.2 on 2022-02-18 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
