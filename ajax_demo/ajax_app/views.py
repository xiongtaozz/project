# coding:utf-8
from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from django.core.serializers import serialize
import json
import simplejson
from django.http import JsonResponse
from ajax_app.models import *

# Create your views here.


# django 1.74 版本以上才出现的 ,1.73以前默认只有syncdb
# model --->只需要执行 magite 第一次使用的时候,他是不会给我们创建超级用户
# syncdb --->关联关系的时候
def index(req):
    user = ''
    return render(req, 'js_index.html', locals())


def login(req):
    username = req.POST.get('username', None)
    password = req.POST.get('password', None)
    print username, password
    if username == '1111' and password == '12345':

        # users = User.objects.get(username == username)
        # # user_t = {}
        # # for u in users:
        # #     user_t['username']
        #
        # user = serialize('json', users)  # 1.serialize 2.自己构造 3.django_formwork
        # print type(users)
        start = {'success': 'success', 'statrs': 200}
        return HttpResponse(json.dumps(start), content_type='application/json')
        # return HttpResponse('ok')
    else:
        return HttpResponseRedirect('/index/')  # 302


def the_ajax(req):

    print req.POST.get('start', None)

    st = {'start': True, 'success': 'success'}

    return HttpResponse(json.dumps(st), content_type='application/json')


def jsonp_ajax(req):

    return HttpResponse(simplejson.dumps({"jsonp": False, "aa": "callbackName"}))


def ajax_users(req):
    users = Us.objects.all()
    # users = Us.objects.raw('select * from ajax_app_us as u left JOIN ajax_app_city as c on u.')
    user = []
    for u in users:
        user.append({'fields':{'name': u.name, 'city_name': u.city.name}}) # {'fields':[{},{}]}
    data = {'success': '成功', 'user': user}
    return HttpResponse(simplejson.dumps(data), content_type='application/json')