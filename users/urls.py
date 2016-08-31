# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import UserList, UserDetail, UserObjectsList, UserObjectsDetail

urlpatterns = [
    url(r'^$', UserList.as_view()),
    url(r'^(?P<username>\w+)/$', UserDetail.as_view()),
    url(r'^(?P<username>\w+)/objects/$', UserObjectsList.as_view()),
    url(r'^(?P<username>\w+)/objects/(?P<pk>\d+)/$', UserObjectsDetail.as_view())
]
