# coding:utf-8
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
