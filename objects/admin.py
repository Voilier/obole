# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import Object, ObjectCustomVisibility, ObjectPermissions


class VisibilityInline(admin.TabularInline):
    model = ObjectCustomVisibility
    extra = 0


class PermissionInline(admin.TabularInline):
    model = ObjectPermissions
    extra = 0


class ObjectAdmin(admin.ModelAdmin):
    inlines = (VisibilityInline, PermissionInline)


admin.site.register(Object, ObjectAdmin)
admin.site.register(ObjectCustomVisibility)
admin.site.register(ObjectPermissions)
