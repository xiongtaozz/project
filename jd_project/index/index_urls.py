from django.conf.urls import patterns, include, url
from index.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jd_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'index/$',index,name='index'),
)

