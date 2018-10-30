# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-10-14 15:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0004_auto_20181014_1224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oauth_ex',
            options={'verbose_name': '第三方登录', 'verbose_name_plural': '第三方登录'},
        ),
        migrations.AddField(
            model_name='oauth_ex',
            name='oauth_type',
            field=models.CharField(choices=[('1', 'github'), ('2', 'qq'), ('3', 'weibo')], default='1', max_length=1, verbose_name='第三方'),
        ),
        migrations.AlterField(
            model_name='oauth_ex',
            name='openid',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='oauth_ex',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]