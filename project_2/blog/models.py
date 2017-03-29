#coding: utf-8
from django.db import models

# Create your models here.
# 作者类
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=18)

# 文章类
class Article(models.Model):
    title = models.CharField(max_length=52)
    content = models.TextField()
    date = models.TimeField()
    author = models.ForeignKey(Author)