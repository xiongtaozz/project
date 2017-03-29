from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'class_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    #url(r'index_find/$',''),
)
urlpatterns +=patterns('',
    url(r'^xt_blog/',include('xt_blog.xt_blog_urls')),
    url(r'^yr_blog/',include('yr_blog.yr_blog_url')),
)