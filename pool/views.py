# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from aldryn_newsblog.models import Article
from pool.models import Comment, Request
from django.core.mail import send_mail
# Create your views here.


def addComment(request, article_id):
    article = Article.objects.get(id=article_id)
    name = request.POST.get('name', None)
    email = request.POST.get('email', None)
    content = request.POST.get('comment', None)
    comment = Comment(name=name, email=email, content=content, article=article)
    comment.save()
    queryset = Article.objects.all()
    context = {'article': article}
    url = article.get_absolute_url()
    prev_objs = queryset.filter(
            publishing_date__lt=article.publishing_date
        ).order_by(
            '-publishing_date'
        )[:1]
    if prev_objs:
        context['prev_article'] = prev_objs[0]
    else:
        context['prev_article'] = None

    next_objs = queryset.filter(
            publishing_date__gt=article.publishing_date
        ).order_by(
            'publishing_date'
        )[:1]
    if next_objs:
        context['next_article'] = next_objs[0]
    else:
        context['next_article'] = None
    return HttpResponseRedirect(url)


def sendRequest(request):
    req = Request()
    try:
        req.name = request.POST.get('name', None)
        req.email = request.POST.get('email', None)
        req.phone = request.POST.get('phone', None)
        req.message = request.POST.get('message', None)
        if 'attachment' in request.FILES:
            attachment = request.FILES['attachment']
            fs = FileSystemStorage()
            filename = fs.save(attachment.name, attachment)
            uploaded_file_url = fs.url(filename)
            req.attachment = uploaded_file_url
        req.save()
        # sending email to admin
        url = '/'
        send_mail(
            'New request for quote',
            'You have received a new request %s for a quote.' % req.id,
            'nedsoft2018@gmail.com',
            ['nedimitri@gmail.com'],
            fail_silently=False,
        )
        return HttpResponseRedirect(url)
    except KeyError:
        return HttpResponseRedirect('/')
