# -*- coding:utf-8 -*-
from rest_framework import viewsets
from blog_2.models import *
from blog_2.serializer import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from chenyu_blog_2.settings import REST_FRAMEWORK

class PythonTitleViewSet(viewsets.ModelViewSet):
	queryset = PythonTitle.objects.all()
	serializer_class = PythonTitleSerializer
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	# permission_classes = REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES']

class PythonSubTitleViewSet(viewsets.ModelViewSet):
	queryset = PythonSubTitle.objects.all()
	serializer_class = PythonSubTitleSerializer
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	# permission_classes = REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES']