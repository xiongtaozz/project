# -*- coding:utf-8 -*-
from django.db import models


# Create your models here.


# 商品
class Product(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    description = models.TextField(verbose_name='描述')
    photo = models.ImageField(verbose_name='图片',)
    price = models.FloatField(verbose_name='价格')

    class Meta:
        db_table = 'product'

    def __unicode__(self):
        return self.title


# 作者表
class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name='作者姓名')
    age = models.IntegerField(verbose_name='年龄')
    address = models.CharField(max_length=30, verbose_name='地址')

    class Meta:
        db_table = 'author'

    def __unicode__(self):
        return self.name


# 书籍
class Book(models.Model):
    title = models.CharField(max_length=30, verbose_name='作者书名')
    price = models.FloatField(verbose_name='价格')
    authors = models.ManyToManyField(Author)
    # models.OneToOneField

    class Meta:
        db_table = 'book'

    def __unicode__(self):
        return self.title