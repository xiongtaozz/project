from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.static import serve
from xt_blog.views import *
import settings





urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'begin_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index,{'tem':'index.html'},name='index'),
    #url(r'^mod/(P<num>.*)/$')
    #url(r'blog/detail/$','',name='detail')
)
#urlpatterns += patterns('',
#    (r'^static/$',serve,{'document_root':settings.STATIC_ROOT}),
#    (r'^site_img/(P<year>.*)\d{4}/$',serve,{'document_root':settings.STATIC_ROOT}),
#)