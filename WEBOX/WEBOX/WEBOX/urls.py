"""WEBOX URL Configuration

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
from we30.views import we30_index
from we30p.views import we30p_index
from we30c.views import we30c_index
from WEBOX.views import index
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/',index),
    url(r'^we30/',we30_index),
    url(r'^we30p/',we30p_index),
    url(r'^we30c/',we30c_index),
    url(r'^index/we30c/',we30c_index),
]
