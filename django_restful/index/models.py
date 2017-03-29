# -*- coding:utf-8 -*-
from django.db import models


class Tag(models.Model):
    key = models.CharField('关键字', max_length=20)

    class Meta:
        db_table = 'Tag'
        ordering = ['pk']
        verbose_name = '关键字表'
        verbose_name_plural = '关键字表'

    def __unicode__(self):
        return self.key


class Product(models.Model):
    name = models.CharField('名称', max_length=20, null=False)
    style = models.CharField('类型', max_length=20, choices=(('DH', '大号'), ('ZH', '中号'), ('XH', '小号')), default='ZH')
    qty = models.IntegerField('数量', default=1)
    price = models.FloatField('价格', default=0.0)
    city = models.CharField('城市', max_length=20)
    keys = models.ForeignKey(Tag, verbose_name='关联id')
    remark = models.TextField('备注')

    class Meta:
        db_table = 'Product'
        ordering = ['pk']
        verbose_name = '产品表'
        verbose_name_plural = '产品表'

    def __unicode__(self):
        return self.name

