# Generated by Django 4.0.2 on 2022-02-18 16:42

from django.db import migrations, models
import mainApp.helper


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_alter_snippet_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='expiry_time',
            field=models.DateTimeField(default=mainApp.helper.expiry_time_func),
        ),
    ]