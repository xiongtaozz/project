from django.conf.urls import patterns, include, url
from django.contrib import admin
from search.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'search_pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index,name='index'),
    url(r'^search/$',search,name='search'),
    url(r'^ques/$',questionDetail,name='ques'),
    url(r'^ques/(?P<cid>\w+)/comm/(?P<qid>\w+)/$',quesComm),
)
