# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-14 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
