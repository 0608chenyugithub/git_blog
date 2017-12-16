# -*- coding:utf-8 -*-
from django.conf.urls import url
from blog_2 import web_views


urlpatterns = [
    url(r'^/index/', web_views.index),
]