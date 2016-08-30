# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json
from django.http import HttpResponse
from django.contrib.auth.models import User

from core.http import JSONResponse

from objects.models import Object

from .serializers import user_serializer
from .permissions import ObjectPermission


def user_list(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        data = user_serializer(queryset)
        return JSONResponse(data)
    else:
        return HttpResponse(status_code=400)


def user_detail(request, user):

    info_mock = {
        'name': 'Toto',
        'bio': 'I\'m the coolest guy on earth',
        'total_sharing': 50,
        'current_sharing': 2,
        'current_borrow': 4
    }
    if request.method == 'GET':
        return HttpResponse(json.dumps(info_mock), content_type="application/json")
        pass
    elif request.method == 'POST':
        return HttpResponse(json.dumps(info_mock), content_type="application/json")
    return None


def user_objects(request, user):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    return None


def user_object(request, user, obj):
    if request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        pass
    return None
