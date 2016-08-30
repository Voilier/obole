# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db.models import QuerySet


def object_serializer(obj):
    if isinstance(obj, QuerySet):
        return [{
            'owner': o.owner,
            'disposer': o.disposer,
            'visibility': o.visibility,
            'name': o.name,
            'description': o.description,
            'picture': o.picture
        } for o in obj]
    else:
        return {
            'owner': obj.owner,
            'disposer': obj.disposer,
            'visibility': obj.visibility,
            'name': obj.name,
            'description': obj.description,
            'picture': obj.picture
        }

