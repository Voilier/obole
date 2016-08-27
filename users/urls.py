# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from .views import (user_object, user_objects, user_object_add, user_object_delete,
        user_object_edit, user_info)

urlpatterns = [
    url(r'^users/(?P<user>\w+)/$', user_info),
    url(r'^users/(?P<user>\w+)/objects/$', user_objects),
    url(r'^users/(?P<user>\w+)/objects/add/$', user_object_add),
    url(r'^users/(?P<user>\w+)/objects/delete/$', user_object_delete),
    url(r'^users/(?P<user>\w+)/objects/edit/$', user_object_edit),
    url(r'^users/(?P<user>\w+)/objects/(?P<obj>\d+)/$', user_object),
]
