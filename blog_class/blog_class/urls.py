from django.conf.urls import patterns, include, url
from django.contrib import admin
import xt_blog.views as v
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog_class.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^show_techer/$',v.show_techer,{'tem':'show_techer.html'}),
    url(r'^show_stur/$',v.show_stu,{'tem':'show_stu.html'}),
)
