# -*- coding:utf-8
from django.db import models

# Create your models here.


class Tag(models.Model):
    key_word = models.CharField('关键字', max_length=20)


class Product(models.Model):
    CHENGDU = 'CD'
    SHANGHAO = 'SH'
    BEIJIN = 'BJ'
    SHENZHEN = 'SZ'
    CITY = (
        (CHENGDU, '成都'),
        (SHANGHAO, '上海'),
        (BEIJIN, '北京'),
        (SHENZHEN, '深圳'),
    )

    PROMODEL = (
        ('MIN', '小号'),
        ('MED', '中号'),
        ('MAX', '大号'),
    )
    PROSTYLE = (
        ('DQ', '电器'),
        ('SP', '食品'),
        ('KL', '   '),
    )
    pro_name = models.CharField('产品名称', max_length=20)
    city = models.CharField('城市', max_length=20, choices=CITY, default=CHENGDU)
    password = models.CharField('密码', max_length=20)
    pro_model = models.CharField('型号', max_length=20, choices=PROMODEL, default='MIN')
    pro_style = models.CharField('类别', max_length=20, choices=PROSTYLE, default='DQ')
    pro_qty = models.IntegerField('数量', default=1)
    pro_price = models.FloatField('价格', default=0.0)
    pro_remark = models.TextField('描述', max_length=200)
    tags = models.ManyToManyField(Tag, verbose_name='关键字')



