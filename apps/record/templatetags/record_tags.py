########################################################################################################################
## Django 自带模块导入
########################################################################################################################
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.db.models import Q
from django import template
from django.db.models import Count


########################################################################################################################
## 系统自带模块导入
########################################################################################################################
import json
import datetime

########################################################################################################################
## 自建模块导入
########################################################################################################################
from record.models import *


register = template.Library()

########################################################################################################################
## 获取省名字
########################################################################################################################
@register.simple_tag
def get_city_name(cid):
    return Cities.objects.get(id=int(cid))


########################################################################################################################
## 获取市名字
########################################################################################################################
@register.simple_tag
def get_area_name(aid):
    return Areas.objects.get(id=int(aid))


########################################################################################################################
## 获取区名字
########################################################################################################################
@register.simple_tag
def get_province_name(pid):
    return Provinces.objects.get(id=int(pid))


########################################################################################################################
## 获取记录数量
########################################################################################################################
@register.simple_tag
def get_record_nums():
    return FaultRecord.objects.all().count()


########################################################################################################################
## 获取所有记录
########################################################################################################################
@register.simple_tag
def get_all_record():
    return FaultRecord.objects.all().order_by('-start_time')


########################################################################################################################
## 获取标签归档记录
########################################################################################################################
@register.simple_tag
def get_tag_record():
    return RecordTags.objects.annotate(record_count=Count('faultrecord')).filter(record_count__gt=0)


########################################################################################################################
## 省份归档记录
########################################################################################################################
@register.simple_tag
def get_province_record():
    return Provinces.objects.annotate(record_count=Count('faultrecord')).filter(record_count__gt=0)


########################################################################################################################
## 用户归档记录
########################################################################################################################
@register.simple_tag
def get_user_record():
    return UserProfile.objects.annotate(record_count=Count('faultrecord')).filter(record_count__gt=0)




