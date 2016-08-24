from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class Object(models.Model):
    VISIBILITY = (
        (0, _('Just me')),
        (1, _('Partner')),
        (2, _('Friends')),
        (3, _('Friends & their friends')),
        (4, _('Public')),
        (5, _('Custom'))
    )

    owner = models.ForeignKey(User, related_name='owning')
    disposer = models.ForeignKey(User, related_name='disposing')
    visibility = models.PositiveSmallIntegerField(choices=VISIBILITY)


class ObjectPermissions(models.Model):
    PERMISSIONS = (
        (0, _('Can be lent before being returned.')),
    )

    user = models.ForeignKey(User)
    object = models.ForeignKey(Object)
    permission = models.PositiveSmallIntegerField(choices=PERMISSIONS)


class ObjectCustomVisibility(models.Model):
    user = models.ForeignKey(User, related_name='custom_allow')
    obj = models.ForeignKey(Object)
    friend = models.ForeignKey(User, related_name='custom_allowed')
