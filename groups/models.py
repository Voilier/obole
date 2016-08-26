# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import Group as BaseGroup
from django.utils.translation import ugettext as _
from django.db import models


class Group(BaseGroup):
    description = models.TextField(_('Description'))
