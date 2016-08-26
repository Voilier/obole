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

    group = models.ForeignKey(Group, verbose_name=_('Group'))
    kind = models.PositiveSmallIntegerField(_('Type'), choices=Type.CHOICES)

    user1 = models.ForeignKey(
        User, verbose_name=_('First user'),
        related_name='transactions_initiated')
    user2 = models.ForeignKey(
        User, verbose_name=_('Second user'),
        related_name='transactions_received')
    object1 = models.ForeignKey(
        Object, verbose_name=_('Second object'),
        related_name='transacted_from')
    object2 = models.ForeignKey(
        Object, verbose_name=_('Second object'),
        related_name='transacted_to', null=True)
    visibility1 = models.PositiveSmallIntegerField(
        verbose_name=_("First user's visibility"),
        choices=Object.Visibility.CHOICES)
    visibility2 = models.PositiveSmallIntegerField(
        verbose_name=_("Second user's visibility"),
        choices=Object.Visibility.CHOICES)

    def __str__(self):
        return '%s: %s / %s: %s' % (self.user1, self.object1,
                                    self.user2, self.object2)

    def visibility(self):
        for v in (Object.Visibility.JUST_ME,
                  Object.Visibility.PARTNER,
                  Object.Visibility.FRIENDS,
                  Object.Visibility.FRIENDS_AND_FRIENDS,
                  Object.Visibility.PUBLIC):
            if v in (self.visibility1, self.visibility2):
                return v
        return Object.Visibility.PUBLIC
