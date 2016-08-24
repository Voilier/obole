from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from groups.models import Group
from objects.models import Object

User = get_user_model()


class Transaction(models.Model):
    TRANSACTION = (
        (0, _('Gift')),
        (1, _('Lend')),
        (2, _('Exchange')),
    )

    group = models.ForeignKey(Group)
    kind = models.PositiveSmallIntegerField(choices=TRANSACTION)
    user1 = models.ForeignKey(User)
    user2 = models.ForeignKey(User)
    object1 = models.ForeignKey(Object)
    object2 = models.ForeignKey(Object)
    visibility1 = models.PositiveSmallIntegerField(choices=Object.VISIBILITY)
    visibility2 = models.PositiveSmallIntegerField(choices=Object.VISIBILITY)

    def visibility(self):
        return  # the most restrictive visibility
