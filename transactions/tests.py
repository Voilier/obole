# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.test import TestCase

from groups.models import Group
from users.models import User
from objects.models import Object

from .models import Transaction


class TransactionTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(
            'test_user1', 'test@email1.com', 'test_password1')
        user2 = User.objects.create_user(
            'test_user2', 'test@email2.com', 'test_password2')
        object1 = Object.objects.create(
            owner=user1,
            disposer=user2,
            visibility=Object.Visibility.FRIENDS,
            name='test_object1',
            description='test_object1_description'
        )
        object2 = Object.objects.create(
            owner=user1,
            disposer=user2,
            visibility=Object.Visibility.FRIENDS,
            name='test_object2',
            description='test_object2_description'
        )
        Transaction.objects.create(
            group=Group.objects.create(name='test_group'),
            kind=Transaction.Type.GIFT,
            user1=user1,
            user2=user2,
            object1=object1,
            object2=object2,
            visibility1=Object.Visibility.JUST_ME,
            visibility2=Object.Visibility.FRIENDS,
        )

    def test_transaction_visibility(self):
        transaction = Transaction.objects.all()[0]
        self.assertEqual(transaction.visibility(), Object.Visibility.JUST_ME)
