# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json
from itertools import chain

from django.db.models import Q
from django.http import HttpResponse
from rest_framework import generics

from core.http import JSONResponse

from objects.models import Object
from objects.serializers import ObjectSerializer

from .models import User, UserProfile
from .serializers import UserSerializer
from .permissions import ObjectPermission


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class UserObjectsList(generics.ListCreateAPIView):
    serializer_class = ObjectSerializer

    def get_queryset(self):
        return Object.user(self.request.user)


class UserObjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ObjectSerializer

    def get_queryset(self):
        return Object.user(self.request.user)

