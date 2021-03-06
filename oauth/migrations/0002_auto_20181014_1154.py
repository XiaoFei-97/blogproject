# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-10-14 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuth_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=12)),
                ('title', models.CharField(max_length=12)),
                ('img', models.FileField(upload_to='static/img/connect')),
            ],
        ),
        migrations.AddField(
            model_name='oauth_ex',
            name='oauth_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='oauth.OAuth_type'),
        ),
    ]
