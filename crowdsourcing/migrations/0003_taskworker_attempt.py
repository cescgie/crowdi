# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0002_merge_20170726_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskworker',
            name='attempt',
            field=models.SmallIntegerField(default=0),
        ),
    ]
