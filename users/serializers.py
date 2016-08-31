# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from .models import User, UserProfile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('nickname', 'profile_picture')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # http://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active', 'is_staff',
                  'date_joined', 'profile')
        lookup_field = 'username'

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        # Unless the application properly enforces that this field is
        # always set, the follow could raise a `DoesNotExist`, which
        # would need to be handled.
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.nickname = profile_data.get(
            'nickname', profile.nickname)
        profile.profile_picture = profile_data.get(
            'profile_picture', profile.profile_picture)
        profile.save()

        return instance
