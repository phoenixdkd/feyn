# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 02:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feyn_admin', '0003_auto_20151224_0154'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SystemUser',
            new_name='User',
        ),
    ]