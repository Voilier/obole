# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import Group, BaseGroup

admin.site.unregister(BaseGroup)
admin.site.register(Group)
