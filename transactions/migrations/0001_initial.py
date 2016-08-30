# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 16:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('objects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.PositiveSmallIntegerField(choices=[(0, 'Gift'), (1, 'Lend'), (2, 'Exchange')], verbose_name='Type')),
                ('visibility1', models.PositiveSmallIntegerField(choices=[(0, 'Just me'), (1, 'Partner'), (2, 'Friends'), (3, 'Public'), (4, 'Custom')], verbose_name="First user's visibility")),
                ('visibility2', models.PositiveSmallIntegerField(choices=[(0, 'Just me'), (1, 'Partner'), (2, 'Friends'), (3, 'Public'), (4, 'Custom')], verbose_name="Second user's visibility")),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Group', verbose_name='Group')),
                ('object1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacted_from', to='objects.Object', verbose_name='Second object')),
                ('object2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transacted_to', to='objects.Object', verbose_name='Second object')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions_initiated', to=settings.AUTH_USER_MODEL, verbose_name='First user')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions_received', to=settings.AUTH_USER_MODEL, verbose_name='Second user')),
            ],
        ),
    ]
