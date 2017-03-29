# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField('关键字', max_length=20)

    def __unicode__(self):  # __str__ -->3.x
        return self.name


class Product(models.Model):
    CHENGDU = 'CD'
    BEIJING = 'BJ'
    SHANGHAI = 'SH'
    SHENZHEN = 'SZ'

    CITY = (
        (CHENGDU, '成都'),
        (BEIJING, '北京'),
        (SHANGHAI, '上海'),
        (SHENZHEN, '深圳'),
    )

    PROMODEL = (
        ('MIN', '小号'),
        ('MID', '中号'),
        ('MAX', '大号'),
    )
    PROSTYLE = (
        ('SP', '食品'),
        ('DQ', '电器'),
        ('KK', '   '),
    )
    pro_name = models.CharField('产品名称', max_length=20)
    city = models.CharField('城市',  max_length=20, choices=CITY, default=BEIJING)
    password = models.CharField('密码', max_length=20)
    pro_model = models.CharField('型号',  max_length=20, choices=PROMODEL, default='MIN')
    pro_style = models.CharField('类型',  max_length=20, choices=PROSTYLE, default='KK')
    qty = models.IntegerField('数量', default=1)
    price = models.FloatField('价格', default=0.0)
    tags = models.ManyToManyField(Tag, verbose_name='关键字')
    remake = models.TextField('备注', max_length=200)

    def __unicode__(self):
        return self.pro_name

