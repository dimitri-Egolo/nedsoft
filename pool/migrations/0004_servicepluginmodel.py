# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-15 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('pool', '0003_comment_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='pool_servicepluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.TextField()),
                ('delay', models.CharField(blank=True, default='05', max_length=50)),
                ('icon', models.CharField(blank=True, default='mbri-responsive', max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
