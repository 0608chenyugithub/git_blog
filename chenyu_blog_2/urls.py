"""chenyu_blog_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from chenyu_blog_2 import settings
from blog_2.upload import upload_image
from django.views.static import serve
from blog_2 import web_views
# from django.conf import settings

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', web_views.index),
    url(r'^admin/', include('blog_2.admin_url', namespace='admin-urls')),
    # url(r'^web', include('blog_2.url')),
    url(r'^uploads/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$',\
        upload_image, name='upload_image'),
]
