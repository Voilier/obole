# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import include, url
from .views import user_objects, user_object

urlpatterns = [
    url(r'^users/(?P<user>\w+)/objects/$', user_objects),
    url(r'^users/(?P<user>\w+)/objects/(?P<obj>\d+)/$', user_object),
]

