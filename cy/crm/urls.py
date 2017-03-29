__author__ = 'hunter'
from django.conf.urls import url
from views import budget,add_budget,ret,test,remark
urlpatterns = [
    url(r'^input/$',budget,{'url':'test.html'}),
    url(r'^post/$',remark,{'url':'test1.html'}),
    url(r'^test/$',test,{'url':'test2.html'}),
    url(r'^ret/$',ret),
]