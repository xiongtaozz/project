from django.conf.urls import patterns, include, url
from django.contrib import admin
from model.views import *
#from django.views.static import serve
#import settings

#print settings.STATIC_ROOT

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cart.views.home', name='home'),
    url(r'^index/$',index_d1,name='index'),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^cart/loginis/$',loginis),
    url(r'^cart/login/$',login),
    url(r'^cart/index/$',index),
    url(r'^cart/addcart/$',addcart),
    url(r'^cart/findcart/$',find_cart),
    url(r'^cart/(?P<id>\w+)/cartupdate',update_cart),
    url(r'^cart/(?P<id>\w+)/cartdel',del_cart),
    url(r'^cart/get_json/$',get_json),
    url(r'^cart/logout/$',logout)
    #(r'^site_media/(?P<path>.*)',serve,{'document_root':'F:/Program Files/Workbase/webase/cart/cart/img'}),
    #(r'^static/(?P<path>.*)',serve, {'document_root':settings.STATIC_ROOT}),
)
urlpatterns +=patterns('this_html',
    url(r'^basehtml/$',base_html)
)