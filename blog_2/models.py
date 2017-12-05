# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PythonTitle(models.Model):
	title = models.CharField(null=False, max_length=30, verbose_name='章节名称')

class PythonSubTitle(models.Model):
	python_title = models.ForeignKey(PythonTitle, related_name='python_sub_title')
	sub_title = models.CharField(null=False, max_length=30, verbose_name='子章节名称')
	detail = models.CharField(null=False, verbose_name='详情', max_length=3000)