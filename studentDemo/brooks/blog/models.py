#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Author(models.Model):
    #作者
    name = models.CharField(max_length=200)

class Category(models.Model):
    #分类
    cat_name = models.CharField(max_length=200)

class Article(models.Model):
    #文章
    title = models.CharField(max_length=300)
    content = models.TextField()
    portal = models.ImageField(default='article/img')
    url = models.URLField()
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Category)

