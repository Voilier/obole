# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visibility', models.PositiveSmallIntegerField(choices=[(0, 'Just me'), (1, 'Partner'), (2, 'Friends'), (3, 'Friends & their friends'), (4, 'Public'), (5, 'Custom')])),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('disposer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disposing', to='users.User')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owning', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectCustomVisibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_allowed', to='users.User')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Object')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_allow', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.PositiveSmallIntegerField(choices=[(0, 'Can be lent before being returned.')])),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Object')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
    ]