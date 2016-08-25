# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models
from django.contrib.auth.models import User as BaseUser


class User(BaseUser):
    nickname = models.CharField(max_length=255)
