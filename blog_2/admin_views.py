# -*- coding:utf-8 -*-
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

from blog_2.models import *
from django.http import HttpResponseRedirect, JsonResponse, response
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


def init_login(request):
	return render(request, 'login.html')


# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
@csrf_exempt
def handle_login(request):
	if request.method == "POST":
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return JsonResponse({'redirect_url': reverse("admin-urls:python")})
		else:
			return JsonResponse({'info': u'用户名或密码错误'})
	else:
		return JsonResponse({'info': u'用户名或密码错误'})


def handle_logout(request):
	logout(request)
	return HttpResponseRedirect('/admin/login/')


@login_required(login_url="/admin/login/")
def admin(request):
	user_name = request.user.username
	return render(request, 'admin.html', locals())


@login_required(login_url="/admin/login/")
def python(request):
	u = request.user
	python_title_list = PythonTitle.objects.all()

	def getPage(request, python_title_list):
		paginator = Paginator(python_title_list, 3)
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
	u = request.user
	return render(request, 'python_edit.html',locals())


@login_required(login_url="/login/")
def python_add_sub(request):
	u = request.user
	python_title = PythonTitle.objects.all()
	return render(request, 'python_edit_sub.html', locals())


@login_required(login_url="/login/")
def python_edit(request, title_id):
	u = request.user
	python_title = PythonTitle.objects.get(id=title_id)
	return render(request, 'python_edit.html', locals())


@login_required(login_url="/login/")
def python_edit_sub(request, subtitle_id):
	u = request.user
	python_subtitle = PythonSubTitle.objects.get(id=subtitle_id)
	return render(request, 'python_edit_sub.html', locals())


def profile(request):
	u = request.user
	return render(request, 'profile.html', locals())


def profile_edit(request, user_id):
	u = User.objects.get(id=user_id)
	return render(request, 'profile_edit.html', locals())


def password_edit(request, user_id):
	u = User.objects.get(id=user_id)
	return render(request, 'profile_edit.html', locals())


def profile_save(request):
	# upload_image(request, '')
	u = request.user
	data = request.POST
	if data.has_key('username'):
		username = data.get('username')
		u.username = username
	if data.has_key('gender'):
		gender = data.get('gender')
		u.gender = gender
	if data.has_key('age'):
		age = data.get('age')
		u.age = age
	if data.has_key('school'):
		school = data.get('school')
		u.school = school
	if data.has_key('desc'):
		desc = data.get('desc')
		u.desc = desc
	if request.FILES.has_key('imgFile'):
		img = request.FILES.get('imgFile')
		u.img = img
	u.save()
	return JsonResponse({'msg': 'success'})


# @csrf_exempt
# def register(request):
# 	username = request.POST.get('username')
# 	password = request.POST.get('password')
# 	u = User()
# 	u.username = username
# 	u.set_password(password)
# 	u.save()
# 	return JsonResponse({'msg': 'sucess'})