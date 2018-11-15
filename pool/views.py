# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from aldryn_newsblog.models import Article
# Create your views here.


def addComment(request, article_id):
    pass
