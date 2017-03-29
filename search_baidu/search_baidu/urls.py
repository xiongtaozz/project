from django.conf.urls import patterns, include, url
from django.contrib import admin
from search.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'search_baidu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auto_complete/$', auto_complete),
    url(r'^validate/word/$', validate_word, name="validate_word"),
)
