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
## 注册任务到后台
########################################################################################################################
class UserWorkTaskAdmin(object):
    list_display = ['create_user', 'send_to', 'content']

xadmin.site.register(UserWorkTask, UserWorkTaskAdmin)








