# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-06 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_mana', '0002_auto_20180205_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installdoc',
            name='doc_title',
            field=models.CharField(max_length=128, verbose_name='文章标题'),
        ),
    ]
