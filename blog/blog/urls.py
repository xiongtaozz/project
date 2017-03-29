# coding:utf-8
"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import settings
# import xadmin
# from xadmin.plugins import xversion
from blog_app.views import index, login_view, find_blog_id
# xversion.register_models()

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^xadmin/', include(xadmin.site.urls)),            # 添加该行
    # views
    url(r'^login/$', login_view, name='login'),
    url(r'^index/$', index, name='index'),
    url(r'^find-blog/(?P<id>\d+)$', find_blog_id, name='find'),

    # 媒体文件和静态文件URL路径配置
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
