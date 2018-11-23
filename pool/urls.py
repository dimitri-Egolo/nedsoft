from django.conf.urls import url

from pool.views import addComment, sendRequest

app_name = 'pool'

urlpatterns = [
    url(r'^(?P<article_id>[0-9]+)/$', addComment, name='add-comment'),
    url(r'^sendRequest/$', sendRequest, name='send-request'),
    ]
