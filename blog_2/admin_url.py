# -*- coding:utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from blog_2 import admin_views, viewset
from rest_framework import routers, serializers, viewsets

router = routers.SimpleRouter()
router.register(r'pythontitle', viewset.PythonTitleViewSet, base_name='python_title')
router.register(r'pythonsubtitle', viewset.PythonSubTitleViewSet, base_name='python_subtitle')


urlpatterns = [
    url(r'^handle_login/$', admin_views.handle_login, name='handle_login'),
    url(r'^login/$', admin_views.init_login, name='init_login'),
    url(r'^logout/$', admin_views.handle_logout, name='handle_logout'),
    url(r'^python/$', admin_views.python, name="python"),
    url(r'^python/add/$', admin_views.python_add, name="python_add"),
    url(r'^python/add_sub/', admin_views.python_add_sub, name="python_add_sub"),
    url(r'^python/edit/(?P<title_id>\d+)/$', admin_views.python_edit, name="python_edit"),
    url(r'^python/edit_sub/(?P<subtitle_id>\d+)/$', admin_views.python_edit_sub, name="python_edit_sub"),
    url(r'^api/', include(router.urls, namespace='admin-api')),
    url(r'^profile/', admin_views.profile, name='profile'),
    url(r'^profile_edit/(?P<user_id>\d+)/$', admin_views.profile_edit, name='profile_edit'),
    url(r'^password_edit/(?P<user_id>\d+)/$', admin_views.password_edit, name='password_edit'),
    url(r'^profile_save/$', admin_views.profile_save, name='profile_save'),
    # url(r'^register/', admin_views.register)
]