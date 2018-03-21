########################################################################################################################
## Django 自带模块导入
########################################################################################################################

########################################################################################################################
## 系统自带模块导入
########################################################################################################################
import xadmin

########################################################################################################################
## 自建模块导入
########################################################################################################################
from .models import *


########################################################################################################################
## 注册用户记录到后台
########################################################################################################################
class FaultRecordAdmin(object):
    list_display = ['platform', 'incident']

xadmin.site.register(FaultRecord, FaultRecordAdmin)


########################################################################################################################
## 注册用户标签到后台
########################################################################################################################
class RecordTagsAdmin(object):
    list_display = ['name']

xadmin.site.register(RecordTags, RecordTagsAdmin)


########################################################################################################################
## 注册省到后台
########################################################################################################################
class ProvincesAdmin(object):
    list_display = ['name', 'province_code']

xadmin.site.register(Provinces, ProvincesAdmin)


########################################################################################################################
## 注册市到后台
########################################################################################################################
class CitiesAdmin(object):
    list_display = ['province', 'name', 'city_code']

xadmin.site.register(Cities, CitiesAdmin)



########################################################################################################################
## 注册区到后台
########################################################################################################################
class AreasAdmin(object):
    list_display = ['city', 'name', 'area_code']

xadmin.site.register(Areas, AreasAdmin)


