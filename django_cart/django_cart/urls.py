# -*- coding:utf-8 -*-
"""django_cart URL Configuration

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
from cart.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login, name='login'),
    url(r'^index/', index, name='index'),
    url(r'^addcart/(?P<id>\w+)$', addCart, name='add'),
    url(r'^findcart/', findCart, name='find'),

    # 媒体文件和静态文件URL路径配置
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
