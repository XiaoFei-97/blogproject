# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-10-14 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180917_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image_url',
            field=models.URLField(default='', verbose_name='头像地址'),
        ),
    ]
