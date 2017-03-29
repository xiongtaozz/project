#coding: utf-8
from django.shortcuts import render
from django.conf import settings
from blog.models import *
from datetime import date

# Create your views here.

# 首页
def view_index(request):
    articles = Article.objects.all()
    return render(request, 'index_1.html', locals())

# 具体的文章
def view_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'article.html', locals())

def index(request):
    dt = date.today()
    blogs = Article.objects.all().order_by('-date_publish')
    return render(request, 'index.html', locals())

def detail(request, p):
    details = Article.objects.get(id=p)
    return render(request, 'detail.html', locals())


def global_setting(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC,
        'SITE_EMAIL': settings.SITE_EMAIL,
        'SITE_MORE': settings.SITE_MORE,
    }