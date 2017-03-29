#coding: utf-8
from django.shortcuts import render
from blog.models import *

# Create your views here.

# 首页
def view_index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', locals())

# 具体的文章
def view_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'article.html', locals())