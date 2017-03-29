from django.conf.urls import patterns, include, url
from django.contrib import admin
from django_app.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_form.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    url(r'^text/modelsform/$',create_pro,name='create'),
    url(r'^text/update/$',update,name='update'),

)
urlpatterns += patterns('',
    url(r'^text/careate_book/$',createBook,name='create'),
    url(r'^text/find_book/$',findAll,name='findall'),
    url(r'^text/(?P<id>\w)/update/$',updateBook,name='update'),
    url(r'^text/update_book/$',updateBooSuc,name='update_success'),
)
#login user
urlpatterns += patterns('',
     # url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
     url(r'^login/$',login_view),
     url(r'^logout/$',logout_view),
)
