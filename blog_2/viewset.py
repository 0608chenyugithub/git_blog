# -*- coding:utf-8 -*-
from rest_framework import viewsets
from blog_2.models import *
from blog_2.serializer import *
from blog_2.models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from chenyu_blog_2.settings import REST_FRAMEWORK


class PythonTitleViewSet(viewsets.ModelViewSet):
	queryset = PythonTitle.objects.all()
	serializer_class = PythonTitleSerializer
	# authentication_classes = (SessionAuthentication, BasicAuthentication)
	# permission_classes = REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES']


class PythonSubTitleViewSet(viewsets.ModelViewSet):
	queryset = PythonSubTitle.objects.all()
	serializer_class = PythonSubTitleSerializer

	def perform_create(self, serializer):
		parent_id = self.request.POST.get('parentId', None)
		sub_title = self.request.POST.get('sub_title', None)
		detail = self.request.POST.get('detail', None)
		PythonSubTitle.objects.create(python_title_id=parent_id,
									  sub_title=sub_title, detail=detail)

