#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: render_tmp.py
@time: 2017/7/27 13:58
"""

from django.template import loader
from django.http import HttpResponse
from django.conf import settings

def render_template(request, path, data={}):
    t = loader.get_template(path)
    user = request.user
    data['user'] = user
    data['settings'] = settings
    s = t.render(data, request)
    return HttpResponse(s)