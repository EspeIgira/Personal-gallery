# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-15 10:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_images_images_main_img'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='image',
            old_name='Images_Main_Img',
            new_name='Image_Main_Img',
        ),
    ]