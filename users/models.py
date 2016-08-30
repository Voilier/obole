# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=255)
    profile_picture = models.ImageField(blank=True, null=True)

    def url(self):
        return reverse('user_detail', args=(self.pk, ))
