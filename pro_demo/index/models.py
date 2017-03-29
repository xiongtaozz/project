# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.


class Product(models.Model):

    d = 'dahao'
    z = 'zhonghao'
    s = 'xiaohao'

    PB = (
        (d, '大号'),
        (z, '中号'),
        (s, '小号'),
    )

    pro_name = models.CharField(verbose_name='产品名称', max_length=20)
    pro_city = models.CharField('城市', max_length=20)
    pro_pwd = models.CharField('密码', max_length=20)
    pro_pb = models.CharField('型号', choices=PB, default=d, max_length=20)
    pro_style = models.CharField('类型', choices=(('sd', '食品'),('dq', '电器'),('kg', ' ')), default='sd', max_length=20)
    pro_qty = models.IntegerField('库存', default=0)
    pro_price = models.FloatField('价格', default=0.0)
    pro_remark = models.TextField('备注', max_length=200)

    class Meta:
        verbose_name = '产品表'
        verbose_name_plural = verbose_name
        db_table = 'product'
        ordering = ['-pk']

    def __unicode__(self):
        return self.pro_name

