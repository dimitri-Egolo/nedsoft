# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-14 21:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 11, 14, 21, 5, 6, 166806, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
