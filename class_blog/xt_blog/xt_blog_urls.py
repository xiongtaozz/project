from django.conf.urls import patterns, include, url
from django.contrib import admin
from xt_blog.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'class_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/$',index,{'tem':'xt_blog_templates/xt_index.html'}),
    url(r'show_techer/$',show_techer,{'tem':'xt_blog_templates/show_techer.html'}),
    url(r'show_stu/$',show_stu,{'tem':'xt_blog_templates/show_stu.html'}),
)
