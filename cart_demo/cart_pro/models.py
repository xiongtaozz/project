# -*- coding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.sessions.serializers import JSONSerializer
# Create your models here.


# 商品
class Product(models.Model):
    name = models.CharField('名称', max_length=255, unique=True)
    slug = models.SlugField(
        'SLug',
        max_length=50, unique=True,
        help_text='根据name生成的，用于生成页面url，必须唯一')
    brand = models.CharField('品牌', max_length=50)
    sku = models.CharField('计量单位', max_length=50)
    price = models.DecimalField('价格', max_digits=9, decimal_places=2)
    old_price = models.DecimalField('旧价格', max_digits=9, decimal_places=2, blank=True, default=0.00)
    image = models.ImageField('图片', max_length=50)
    is_active = models.BooleanField("设为激活", default=True)
    is_bestseller = models.BooleanField("标为畅销", default=False)
    is_featured = models.BooleanField("标为推荐", default=False)
    quantity = models.IntegerField("数量")
    description = models.TextField('描述')
    meta_keywords = models.CharField(
        "Meta关键词",
        max_length=255, help_text='meta 关键词标签，逗号分隔'
    )
    meta_description = models.TextField(
        'Meta描述',
        max_length=255, help_text='meta 描述标签')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    # categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog product', args=(self.slug,))

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None


# 购物车
class CartItem(models.Model):
    # cart_id = models.CharField(max_length=50)
    # date_added = models.DateTimeField(auto_now_add=True)
    unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, unique=False)

    class Meta:
        db_table = 'cart_items'  # 数据表名称
        # ordering = ['date_added']  #日期排序

import pickle
#
# class JsonSeria(PickleSerializer){
#
# }

class Cart(object):
    def __init__(self, *args, **kwargs):
        self.items = []
        self.total_price = 0

    def dumps(self, obj):
        return pickle.dumps(obj, pickle.HIGHEST_PROTOCOL)

    def loads(self, data):
        return pickle.loads(data)

    def add_product(self, product):
        self.total_price += product.price
        for item in iter(self.items):
            if item.product.slug == product.slug:
                item.quantity += 1
                return
        self.items.append(CartItem(product=product, unit_price=product.price, quantity=1))