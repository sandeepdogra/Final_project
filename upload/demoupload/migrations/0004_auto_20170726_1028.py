# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 04:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoupload', '0003_auto_20170720_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='user_name',
            new_name='username',
        ),
    ]
