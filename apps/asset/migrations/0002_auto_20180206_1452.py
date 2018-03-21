# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-06 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serverinfo',
            name='service_name',
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='disk',
            field=models.SmallIntegerField(default=50, verbose_name='磁盘'),
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='memory',
            field=models.SmallIntegerField(default=8, verbose_name='内存'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '关机'), (1, '开机'), (2, '其它')], default=1, verbose_name='主机状态'),
        ),
    ]
