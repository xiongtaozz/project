from django.conf.urls import patterns, include, url

from django.contrib import admin
#from modelis.views import show_anthor

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/show_author/$','modelis.views.show_anthor'),
    url(r'^blog/show_book/$','modelis.views.show_book'),
    
)
