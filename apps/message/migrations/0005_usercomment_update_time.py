# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-07 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_auto_20180107_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercomment',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
