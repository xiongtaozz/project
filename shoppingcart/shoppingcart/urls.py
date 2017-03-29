from django.conf.urls import patterns, include, url
from django.contrib import admin
from cart.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^cart/loginis/$',loginis),
    url(r'^cart/login/$',login),
    url(r'^cart/index/$',index),
    url(r'^cart/addcart/$',addcart),
    url(r'^cart/findcart/$',findcart),
    url(r'^cart/(?P<id>\w+)/cartupdate',updatecart),
    url(r'^cart/(?P<id>\w+)/cartdel',delcart),
    #(r'^site_media/(?P<path>.*)',serve,{'document_root':'F:/Program Files/Workbase/webase/cart/cart/img'}),
    #(r'^static/(?P<path>.*)',serve, {'document_root':settings.STATIC_ROOT}),
)