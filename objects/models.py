from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _

User = get_user_model()


class Object(models.Model):
    owner = models.ForeignKey(User)
    disposer = models.ForeignKey(User)


class ObjectPermissions(models.Model):
    PERMISSIONS = (
        (0, _('Can be lent before being returned.'))
    )

    object = models.ForeignKey(Object)
    permission = models.PositiveSmallIntegerField(choices=PERMISSIONS)