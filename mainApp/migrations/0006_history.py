# Generated by Django 4.0.2 on 2022-02-18 18:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_snippet_expiry_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_time', models.DateTimeField(default=datetime.datetime.now)),
                ('ip', models.GenericIPAddressField()),
                ('snippet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.snippet')),
            ],
        ),
    ]
