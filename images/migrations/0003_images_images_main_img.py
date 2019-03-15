# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-15 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_remove_images_images_main_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='Images_Main_Img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]