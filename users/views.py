# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import json
from django.http import HttpResponse

# from django.shortcuts import render


def user_objects(request, user):
     
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    return None

def user_info(request, user):
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



def user_object(request, user, obj):
    if request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        pass
    return None

def user_object_add(request, user):
    if request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        pass
    return None

def user_object_delete(request, user):
    if request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        pass
    return None

def user_object_edit(request, user):
    if request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        pass
    return None
