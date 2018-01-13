# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	GENDER = (('1', '男'), ('2', '女'))
	nickname = models.CharField(max_length=30, default='', blank=True)
	gender = models.CharField(choices=GENDER, default='1', blank=True, max_length=4)
	age = models.CharField(default='18', blank=True, max_length=3)
	school = models.CharField(default='', blank=True, max_length=40)
	desc = models.TextField(default='', max_length=200, blank=True)
	img = models.ImageField(upload_to='img', blank=True)


class PythonTitle(models.Model):
	title = models.CharField(null=False, max_length=300, verbose_name='章节名称')


class PythonSubTitle(models.Model):
	python_title = models.ForeignKey(PythonTitle, related_name='python_sub_title', on_delete=models.CASCADE)
	sub_title = models.CharField(null=False, max_length=300, verbose_name='子章节名称')
	detail = models.TextField(null=False, verbose_name='详情', max_length=3000)