# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import PublicObjects

urlpatterns = [
    url(r'^$', PublicObjects.as_view()),
]
