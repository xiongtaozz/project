# -*- coding:utf-8 -*-
from django.shortcuts import render,HttpResponse
from cart_pro.models import *

import json
# Create your views here.


def add_session(req):
    cart =Cart()
    req.session['cart'] = cart


def add_cart(req):

    pro = Product.objects.get(pk=1)

    # 得到前端传来的product slug

    print pro.price
    print pro.brand
    # del request.session['cart']
    cart = req.session.get("cart", None)
    # request.session['cart'] = 'hello'
    print cart
    if cart is None:
        cart = Cart()
        print(cart)
        # print(serialize('json', cart))
        # req.session['cart'] = cart
    cart.add_product(pro)
    # print(type(request.session.get('name')))
    req.session['cart'] = cart
    # 将cart写入session
    # print cart.total_price

    # print serialize('json', Product.objects.all())
    # req.session['cart'] = [{'cart': cart}]

    return HttpResponse(json.dumps({'messange': '成功'}), content_type='Application/json')
