from django.conf.urls import url, include
from django.contrib import admin
from blog_2 import views, viewset
from rest_framework import routers, serializers, viewsets

router = routers.SimpleRouter()
router.register(r'pythontitle', viewset.PythonTitleViewSet)
router.register(r'pythonsubtitle', viewset.PythonSubTitleViewSet)


urlpatterns = [
    url(r'^index/', views.index),
    url(r'^admin/', views.admin),
    url(r'^python/$', views.python, name="python"),
    url(r'^python/add/$', views.python_add, name="python_add"),
    url(r'^python/add_sub/', views.python_add_sub, name="python_add_sub"),
    url(r'^python/edit/(?P<title_id>\d+)/$', views.python_edit, name="python_edit"),
    url(r'^python/edit_sub/(?P<subtitle_id>\d+)/$', views.python_edit_sub, name="python_edit_sub"),
    url(r'^api/', include(router.urls)),
]