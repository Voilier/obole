# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 14:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visibility', models.PositiveSmallIntegerField(choices=[(0, 'Just me'), (1, 'Friends'), (2, 'Public'), (3, 'Custom')])),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('disposer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disposing', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owning', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ObjectCustomVisibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_allowed', to=settings.AUTH_USER_MODEL)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Object')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_allow', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ObjectPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.PositiveSmallIntegerField(choices=[(0, 'Can be lent before being returned')])),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Object')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
