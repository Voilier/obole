# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import public_objects

urlpatterns = [
    url(r'^$', public_objects),
]
