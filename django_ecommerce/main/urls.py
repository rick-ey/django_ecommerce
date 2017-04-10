# main/urls.py

from django.conf.urls import patterns, url
from main import json_views

urlpatterns = patterns(
    'main.json_views',
    url(r'^status_reports/$', json_views.StatusCollection.as_view()),
    url(r'^status_reports/(?P<pk>[0-9]+)/$', json_views.StatusMember.as_view())
)
