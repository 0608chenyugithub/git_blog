from django.conf.urls import url, include
from django.contrib import admin
from blog_2 import views, viewset
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'pythontitle', viewset.PythonTitleViewSet)
router.register(r'pythonsubtitle', viewset.PythonSubTitleViewSet)

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^admin/', views.admin),
    url(r'^python_list/$', views.python_list, name="python_list"),
    url(r'^python_list/add/$', views.python_list_add, name="python_list_add"),
    url(r'^python_list/add_sub/(?P<title_id>\d+)/$', views.python_list_add_sub, name="python_list_add_sub"),
    url(r'^python_list/edit/(?P<subtitle_id>\d+)/$', views.python_list_edit, name="python_list_edit"),
    url(r'^api/', include(router.urls)),
    # url(r'^python_sub/', views.python_sub, name="python_sub"),
]