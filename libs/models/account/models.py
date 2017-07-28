#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: models.py
@time: 2017/7/27 11:44
"""

from django.db import models
from django.contrib.auth.models import User

class ProfileBase(type):
    def __new__(cls, name, bases, attrs):
        module = attrs.pop('__module__')

        parents = [b for b in bases if isinstance(b, ProfileBase)]

        if parents:
            fields = []
            for obj_name, obj in attrs.items():
                if isinstance(obj, models.Field): fields.append(obj_name)
                User.add_to_class(obj_name, obj)
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)

class ProfileUser(object):
    __metaclass__ = ProfileBase

class MyProfile(ProfileUser):
    """
    功能说明:auth_user 扩展属性
    ---------------------------------------------------------------------------
    修改人              修改时间
    ------------------------------------------------------------------------------
    张帅男            2017-7-28
    """
    real_name = models.CharField(max_length=255)               # 用户真实姓名
    sex = models.IntegerField(u'性别')                         # 1男 2女
    home = models.CharField(u'住址', max_length=255)           # 住址
    company = models.CharField(u'公司', max_length=255)        # 公司
    relpwd = models.IntegerField(u'明文密码')                  # 明文密码