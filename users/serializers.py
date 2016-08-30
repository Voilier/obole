# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db.models import QuerySet


def user_serializer(user):
    if isinstance(user, QuerySet):
        return [{
            'username': u.username,
            'first_name': u.first_name,
            'last_name': u.last_name,
            'email': u.email,
            'is_staff': u.is_staff,
            'is_active': u.is_active,
            'date_joined': u.date_joined,
            'profile': u.profile.url()
        } for u in user]
    else:
        return {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
            'date_joined': user.date_joined,
            'profile': user.profile.url()
        }

