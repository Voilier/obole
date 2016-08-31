# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from rest_framework import generics

from .models import Object
from .serializers import ObjectSerializer


class PublicObjects(generics.ListAPIView):
    queryset = Object.public()
    serializer_class = ObjectSerializer
