# coding: utf-8
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10, verbose_name=u'分类名称')

    class Meta:
        verbose_name = u'产品分类'
        verbose_name_plural = verbose_name
        # db_table = 'category'

    def __unicode__(self):   # 3.x __str__
        return self.name  # <name>


class Keyword(models.Model):
    name = models.CharField(max_length=10, verbose_name=u'关键词')

    class Meta:
        verbose_name = u'关键词'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Size(models.Model):
    class Meta:
        verbose_name = '型号'
        verbose_name_plural = verbose_name

    name = models.CharField(max_length=100, verbose_name='大小')

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=10, verbose_name=u'产品名称')
    spec = models.ForeignKey(Size, verbose_name=u'产品型号')
    cate = models.ForeignKey(Category, verbose_name=u'产品类别')
    stock = models.IntegerField(default=100, verbose_name=u'库存数量')
    price = models.DecimalField(default=10.00, decimal_places=2, max_digits=8, verbose_name=u'产品价格')
    key = models.ManyToManyField(Keyword, verbose_name=u'关键词')
    desc = models.TextField(null=True, blank=True, verbose_name=u'产品描述')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'更新日期')

    class Meta:
        verbose_name = u'产品'
        verbose_name_plural = verbose_name
        ordering = ["-id"]

    def __unicode__(self):
        return self.name