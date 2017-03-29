#-*- coding:utf-8 -*-
from django.shortcuts import render
from models import *
from datetime import date
# Create your views here.

#首页
def list(request):
    day = date.today()
    path = request.get_full_path()
    articles = Article.objects.all()
    return render(request, 'index.html',locals())
#文章页
def article(request,pid):
    day = date.today()
    path = request.get_full_path()
    article = Article.objects.get(id=pid)
    return render(request,'article.html',locals())
#分类页
def category(request,cate):
    day = date.today()
    path = request.get_full_path()
    global cat
    if cate == 'yunying':
        cat = 1
    elif cate == 'kandian':
        cat = 2
    elif cate == 'tuijian':
        cat = 3
    articles = Article.objects.filter(category=cat)
    return render(request,'index.html',locals())

