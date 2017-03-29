from django.conf.urls import include, url
from mysite.views import *
from mysite.models import *
from django.contrib import admin
# product_info = {
#     'queryset': UserManager.objects.all(),
# }
urlpatterns = [
    # Examples:
    url(r'^$', index, name='index'),
    url(r'^index/$', index, name='index'),
    url(r'^login/', login, name='login'),
    url(r'^regist/', regist, name='regist'),
    url(r'^logout/', logout, name='logout'),
    url(r'^question_list/', QuestionList.as_view(), name='question_list'),
    url(r'^question/(?P<pk>\d+)/$', QuestionDetail.as_view(), name='question_detail'),
    url(r'^question/add/$', QuestionCreate.as_view(), name='question_add'),
    url(r'^question/(?P<pk>\d+)/$', QuestionUpdate.as_view(), name='question_update'),
    url(r'^question/(?P<pk>\d+)/$', QuestionDelete.as_view(), name='question_delete'),
    # url(r'^admin/$',include(admin.site.urls))
]
