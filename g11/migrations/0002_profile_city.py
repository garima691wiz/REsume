# Generated by Django 3.0.3 on 2021-09-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g11', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='City',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]
