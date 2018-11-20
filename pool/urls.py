from django.conf.urls import url

from pool.views import addComment

app_name = 'pool'

urlpatterns = [
    url(r'^(?P<article_id>[0-9]+)/$', addComment, name='add-comment'),
    ]
