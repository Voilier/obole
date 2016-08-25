# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from groups.models import Group
from objects.models import Object


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
    user1 = models.ForeignKey(User, related_name='transactions_from')
    user2 = models.ForeignKey(User, related_name='transations_to')
    object1 = models.ForeignKey(Object, related_name='transactions_from')
    object2 = models.ForeignKey(Object, related_name='transations_to')
    visibility1 = models.PositiveSmallIntegerField(
        choices=Object.Visibility.CHOICES)
    visibility2 = models.PositiveSmallIntegerField(
        choices=Object.Visibility.CHOICES)

    def visibility(self):
        return  # the most restrictive visibility
