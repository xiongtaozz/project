# -*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from form_app.model_forms import *
from form_app.models import *
# Create your views here.


# ProFrom --->From
def ProFrom(req):
    if req.method == 'GET':
        proFrom = ProductFrom()
        return render_to_response('product.html', {'proFrom': proFrom})
    else:
        proFrom = ProductFrom(req.POST)
        # print proFrom.is_valid()
        if proFrom.is_valid():
            print proFrom.cleaned_data
            print proFrom.cleaned_data['title']
            '''
              执行添加业务,可在这处理
            '''
        return render_to_response('product.html', {'proFrom': proFrom})


# ProFrom --->ModelFrom
def proModel(req):
    # 也可以判断这里到底是添加还是修改属性
    if req.method == 'GET':
        # 也可绑定数据库数据 则使用instance
        proFromModel = ProModel(instance=Product.objects.get(pk=2))
    else:
        # 注意,这里是创建文件,  而不是更改 .更改 也是创建
        proFromModel = ProModel(req.POST, req.FILES)
        if proFromModel.is_valid():
            proFromModel.save()
    return render_to_response('product1.html', {'proFromModel': proFromModel})


# 更改数据
def proModelUpdate(req):
    # 也可以判断这里到底是添加还是修改属性
    if req.method == 'GET':
        # 也可绑定数据库数据 则使用instance
        proFromModel = ProModel(instance=Product.objects.get(pk=2))
    else:
        proFromModel = ProModel(req.POST, instance=Product.objects.get(pk=2))
        if proFromModel.is_valid():
            proFromModel.save()
    return render_to_response('product1.html', {'proFromModel': proFromModel})