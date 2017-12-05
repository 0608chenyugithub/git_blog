# -*- coding:utf-8 -*-
from django.shortcuts import render
from blog_2.models import *
def index(request):
	return render(request, 'index.html')

def admin(request):
	return render(request, 'admin.html')

def python_list(request):
	context = {}
	context_list = []
	python_title = PythonTitle.objects.all()
	for item in python_title:
		if item.python_sub_title.all().__len__() > 0:
			for sub_item in item.python_sub_title.all():
				context_list.append([str(item.id) + '-' + str(sub_item.id), item.title, sub_item.sub_title, sub_item.detail])
		else:
			context_list.append([str(item.id) + '-', item.title, '', ''])
	context.update({'context_list': context_list})
	# python_sub_title = PythonSubTitle.objects.all()
	return render(request, 'python_list.html', context)


def python_list_add(request):
	return render(request, 'python.html')


def python_list_add_sub(request, title_id):
	python_title = PythonTitle.objects.get(id=title_id)
	return render(request, 'python_sub.html', locals())


def python_list_edit(request, subtitle_id):
	python_subtitle = PythonSubTitle.objects.get(id=subtitle_id)
	return render(request, 'python.html', locals())