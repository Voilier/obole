# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from groups.models import Group
from objects.models import Object
from users.models import User


class Transaction(models.Model):
    class Type(object):
        GIFT = 0
        LEND = 1
        EXCHANGE = 2

        CHOICES = (
            (GIFT, _('Gift')),
            (LEND, _('Lend')),
            (EXCHANGE, _('Exchange')),
        )

    group = models.ForeignKey(Group)
    kind = models.PositiveSmallIntegerField(choices=Type.CHOICES)
    user1 = models.ForeignKey(User, related_name='transactions_initiated')
    user2 = models.ForeignKey(User, related_name='transactions_received')
    object1 = models.ForeignKey(Object, related_name='transacted_from')
    object2 = models.ForeignKey(Object, related_name='transacted_to', null=True)
    visibility1 = models.PositiveSmallIntegerField(
        choices=Object.Visibility.CHOICES)
    visibility2 = models.PositiveSmallIntegerField(
        choices=Object.Visibility.CHOICES)

    def visibility(self):
        for v in (Object.Visibility.JUST_ME,
                  Object.Visibility.PARTNER,
                  Object.Visibility.FRIENDS,
                  Object.Visibility.FRIENDS_AND_FRIENDS,
                  Object.Visibility.PUBLIC):
            if v in (self.visibility1, self.visibility2):
                return v
        return Object.Visibility.PUBLIC
