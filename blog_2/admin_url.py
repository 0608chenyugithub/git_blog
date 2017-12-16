# -*- coding:utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from blog_2 import admin_views, viewset
from rest_framework import routers, serializers, viewsets

router = routers.SimpleRouter()
router.register(r'pythontitle', viewset.PythonTitleViewSet)
router.register(r'pythonsubtitle', viewset.PythonSubTitleViewSet)


urlpatterns = [
    url(r'^/$', admin_views.admin),
    url(r'^/python/$', admin_views.python, name="python"),
    url(r'^/python/add/$', admin_views.python_add, name="python_add"),
    url(r'^/python/add_sub/', admin_views.python_add_sub, name="python_add_sub"),
    url(r'^/python/edit/(?P<title_id>\d+)/$', admin_views.python_edit, name="python_edit"),
    url(r'^/python/edit_sub/(?P<subtitle_id>\d+)/$', admin_views.python_edit_sub, name="python_edit_sub"),
    url(r'^/api/', include(router.urls)),
]