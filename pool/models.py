# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from cms.models.pluginmodel import CMSPlugin
from aldryn_newsblog.models import Article

from django.db import models


# Create your models here.
@python_2_unicode_compatible
class SkillPluginModel(CMSPlugin):
    name = models.CharField(max_length=50, default='', blank=False)
    percentage = models.IntegerField()

    def __str__(self):
        # return self.safe_translation_getter('title', any_language=True)
        return self.name


@python_2_unicode_compatible
class ServicePluginModel(CMSPlugin):
    name = models.CharField(max_length=50, default='', blank=False)
    description = models.TextField()
    delay = models.CharField(max_length=50, default='05', blank=True)
    icon = models.CharField(max_length=50, blank=True, default="mbri-responsive")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=50, blank=False)
    content = models.TextField(blank=False)
    article = models.ForeignKey(Article, blank=False, related_name="comments")
    parent = models.ForeignKey('self', blank=True, null=True, related_name="replies")

    def __str__(self):
        return self.name
