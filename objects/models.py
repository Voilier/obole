# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from users.models import User


class Object(models.Model):
    class Visibility(object):
        JUST_ME = 0
        PARTNER = 1
        FRIENDS = 2
        FRIENDS_AND_FRIENDS = 3
        PUBLIC = 4
        CUSTOM = 5

        CHOICES = (
            (JUST_ME, _('Just me')),
            (PARTNER, _('Partner')),
            (FRIENDS, _('Friends')),
            (FRIENDS_AND_FRIENDS, _('Friends & their friends')),
            (PUBLIC, _('Public')),
            (CUSTOM, _('Custom'))
        )

    owner = models.ForeignKey(User, related_name='owning')
    disposer = models.ForeignKey(User, related_name='disposing')
    visibility = models.PositiveSmallIntegerField(choices=Visibility.CHOICES)

    name = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.ImageField(blank=True, null=True)


class ObjectPermissions(models.Model):
    class Permission(object):
        LEND_WO_RETURN = 0

        CHOICES = (
            (LEND_WO_RETURN, _('Can be lent before being returned.')),
        )

    user = models.ForeignKey(User)
    object = models.ForeignKey(Object)
    permission = models.PositiveSmallIntegerField(choices=Permission.CHOICES)


class ObjectCustomVisibility(models.Model):
    user = models.ForeignKey(User, related_name='custom_allow')
    obj = models.ForeignKey(Object)
    friend = models.ForeignKey(User, related_name='custom_allowed')
