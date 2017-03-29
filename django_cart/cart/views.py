# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response,HttpResponseRedirect
from cart.models import *
# Create your views here.


# 登陆
def login(req):

    if req.method == 'POST':
        username = req.POST.get('username', None)
        password = req.POST.get('password', None)
        print username, password
        try:
            user = User.objects.get(username=username, password=password)
        except Exception as e:
            print e
        else:
            if user is not None:
                req.session['username'] = username  # session 不支存储对象 建议存字典
                return HttpResponseRedirect('/index/')

    return render_to_response('login.html', locals())


# 首页
def index(req):
    username = req.session['username']
    books = Book.objects.all()
    return render_to_response('index.html', locals())


# 加入购物车
def addCart(req, id):
    book = Book.objects.get(pk=id)
    # print id
    # cart = Cart.objects.filter(book_id=id)
    # print cart is None
    # if cart is None:
    cart = Cart()
    cart.username = req.session['username']
    cart.book = book
    cart.save()
    return HttpResponseRedirect('/index/')


# 查询cart
def findCart(req):
    username = req.session['username']
    carts = Cart.objects.filter(username=username)
    return render_to_response('cart.html', locals())
