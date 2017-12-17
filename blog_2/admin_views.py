# -*- coding:utf-8 -*-
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

from blog_2.models import *
from django.http import HttpResponseRedirect, JsonResponse, response
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


def home(request):
	return render(request, 'home.html')


# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
@csrf_exempt
def handleLogin(request):
	if request.method == "POST":
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect('/admin/')
		else:
			return JsonResponse({'info': u'用户名或密码错误'})
	else:
		return JsonResponse({'info': u'用户名或密码错误'})


def handleLogout(request):
	logout(request)
	return HttpResponseRedirect('/')


@login_required(login_url="/login/")
def admin(request):
	user_name = request.user.username
	return render(request, 'admin.html', locals())


@login_required(login_url="/login/")
def python(request):
	user_name = request.user.username
	python_title_list = PythonTitle.objects.all()

	def getPage(request, python_title_list):
		paginator = Paginator(python_title_list,3)
		try:
			page = int(request.GET.get('page', 1))
			title_list = paginator.page(page)

		except (EmptyPage, InvalidPage, PageNotAnInteger):
			title_list = paginator.page(1)
		return title_list

	python_title_list = getPage(request, python_title_list)
	return render(request, 'python.html', locals())


@login_required(login_url="/login/")
def python_add(request):
	user_name = request.user.username
	return render(request, 'python_edit.html',locals())


@login_required(login_url="/login/")
def python_add_sub(request):
	user_name = request.user.username
	python_title = PythonTitle.objects.all()
	return render(request, 'python_edit_sub.html', locals())


@login_required(login_url="/login/")
def python_edit(request, title_id):
	user_name = request.user.username
	python_title = PythonTitle.objects.get(id=title_id)
	return render(request, 'python_edit.html', locals())


@login_required(login_url="/login/")
def python_edit_sub(request, subtitle_id):
	user_name = request.user.username
	python_subtitle = PythonSubTitle.objects.get(id=subtitle_id)
	return render(request, 'python_edit_sub.html', locals())