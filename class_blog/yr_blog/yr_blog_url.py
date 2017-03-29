from django.conf.urls import patterns, include, url
from django.contrib import admin
from yr_blog.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'class_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/$',login,{'tem':'yr_blog_templates/login.html'}),
)
