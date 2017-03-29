# coding:utf-8
from django.shortcuts import render,render_to_response
from from_app.forms import *
# Create your views here.


def login(req):
    lfrom = None
    if req.method == 'GET':
        lfrom = loginFrom()
    else:
        lfrom = loginFrom(req.POST)
        # print lfrom.is_bound()  # 是否绑定成功
        print lfrom.is_valid()  # 绑定是否合法
        # print lfrom.cleaned_data['username']
        # print req.POST.get('username', '')
        # xxx.objects.get()
    return render_to_response('login.html', {'lfrom':lfrom})


def proModel(req):
    if req.method == 'GET':
        promodel = proFromModel()
    else:
        promodel = proFromModel(req.POST or None, req.FILES)
        if promodel.is_valid():
            promodel.save()
    return render_to_response('pro.html', locals())


def proaddModel(req):
    if req.method == 'GET':
        promodel = proFromModel(instance=Product.objects.get(pk=2))
    else:
        promodel = proFromModel(req.POST or None, instance=Product.objects.get(pk=2))
        if promodel.is_valid():
            promodel.save()
    return render_to_response('pro.html', locals())