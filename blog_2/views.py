# -*- coding:utf-8 -*-
from django.shortcuts import render
from blog_2.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


def index(request):
	return render(request, 'index.html')


def admin(request):
	return render(request, 'admin.html')


def python(request):
	python_title_list = PythonTitle.objects.all()

	def getPage(request, python_title_list):
		paginator = Paginator(python_title_list, 6)
		try:
			page = int(request.GET.get('page', 1))
			title_list = paginator.page(page)

		except (EmptyPage, InvalidPage, PageNotAnInteger):
			title_list = paginator.page(1)
		return title_list

	python_title_list = getPage(request, python_title_list)
	return render(request, 'python.html', locals())


def python_add(request):
	return render(request, 'python_edit.html')


def python_add_sub(request):
	python_title = PythonTitle.objects.all()
	return render(request, 'python_edit_sub.html', locals())


def python_edit(request, title_id):
	python_title = PythonTitle.objects.get(id=title_id)
	return render(request, 'python_edit.html', locals())


def python_edit_sub(request, subtitle_id):
	python_subtitle = PythonSubTitle.objects.get(id=subtitle_id)
	return render(request, 'python_edit_sub.html', locals())