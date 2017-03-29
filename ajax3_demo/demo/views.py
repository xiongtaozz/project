# coding: utf-8
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core import serializers
import simplejson

import json


# Create your views here.
@csrf_exempt
def reg(request):
    return render(request, "reg.html", locals())


def validate_username(request):

    user_list = User.objects.all()
    print user_list
    # print json.dumps(user_list)
    print serializers.serialize("json", user_list)
    # [{'fields':{username},}]

    # result = {"code": "failure", "message": "该账号已经存在"}
    # username = request.REQUEST.get("username")
    # try:
    #     User.objects.get(username=username)  # get 如果则返回,如果没有值,则异常 filter
    # except User.DoesNotExist:
    #     result["code"] = "success"
    #     result["message"] = "该账号可以注册"
    #
    # return HttpResponse(json.dumps(result), content_type="application/json")

    result = '<?xml version="1.0" encoding="utf-8"?>'
    result += '<result>'
    username = request.POST.get("username")
    try:
        User.objects.get(username=username)
        result += '<code>failure</code>'
        result += '<message>该账号已经存在</message>'
    except User.DoesNotExist:
        result += '<code>success</code>'
        result += '<message>该账号可以注册</message>'
    result += '</result>'
    return HttpResponse(result, content_type="text/xml")


def js_ajax(request):
    return render(request, 'js-ajax.html')


def do_js_ajax(request):
    # callback = request.GET.get('jsoncallback')
    # return HttpResponse('%s(%s)' % (callback, json.dumps({'data': '嗨，我是服务端传回的内容哦'})),
    #                     content_type='application/json')
    response = HttpResponse(json.dumps({'data': '嗨，我是服务端传回的内容哦'}),
                            content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response

import re
re.match()