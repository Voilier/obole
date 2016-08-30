# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json

from django.http import HttpResponse

from core.http import JSONResponse

from .models import Object
from .serializers import object_serializer


def public_objects(request):
    queryset = Object.public()
    return JSONResponse(queryset)
