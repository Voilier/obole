# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from .views import user_list, user_detail

urlpatterns = [
    url(r'^$', user_list),
    url(r'^(?P<pk>\d+)/$', user_detail, name='user_detail'),
    # url(r'^(?P<pk>\d+)/objects/$', UserObjectsList.as_view()),
    # url(r'^(?P<pk>\d+)/objects/(?P<obj>\d+)/$', UserObjectDetail.as_view()),
]
