# -*- coding:utf-8 -*-
from rest_framework import viewsets, permissions
from blog_2.models import *
from blog_2.serializer import *
from blog_2.models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class PythonTitleViewSet(viewsets.ModelViewSet):
	queryset = PythonTitle.objects.all()
	serializer_class = PythonTitleSerializer
	authentication_classes = (BasicAuthentication, )
	permission_classes = (permissions.IsAuthenticated,)


class PythonSubTitleViewSet(viewsets.ModelViewSet):
	queryset = PythonSubTitle.objects.all()
	serializer_class = PythonSubTitleSerializer
	authentication_classes = (BasicAuthentication, )
	permission_classes = (permissions.IsAuthenticated,)

	def perform_create(self, serializer):
		parent_id = self.request.POST.get('parentId', None)
		sub_title = self.request.POST.get('sub_title', None)
		detail = self.request.POST.get('detail', None)
		PythonSubTitle.objects.create(python_title_id=parent_id,
									  sub_title=sub_title, detail=detail)

