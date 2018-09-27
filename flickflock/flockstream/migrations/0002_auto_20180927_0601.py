# Generated by Django 2.1.1 on 2018-09-27 06:01

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flockstream', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='caption',
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(default='dis photo', max_length=50),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to=django.core.files.storage.FileSystemStorage(location='media/images')),
        ),
    ]
