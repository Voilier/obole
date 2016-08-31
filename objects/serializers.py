# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from .models import Object


class ObjectSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username')
    disposer = serializers.CharField(source='disposer.username')

    class Meta:
        model = Object
        fields = ('id', 'owner', 'disposer', 'visibility',
                  'name', 'description', 'picture')

