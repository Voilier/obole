# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from rest_framework import permissions

from objects.models import Object


class ObjectPermission(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit it."""

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return (
                obj.visibility == Object.Visibility.PUBLIC or
                obj.owner == request.user or
                obj.disposer == request.user or (
                    obj.visibility == Object.Visibility.FRIENDS and (
                        obj.owner in request.user.friends() or
                        obj.disposer in request.user.friends()
                    )
                )
            )

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
