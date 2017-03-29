from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xtblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index,{'template_name':'index.html'}),
    url(r'^index/$',index,{'template_name':'index1.html'}),
)

