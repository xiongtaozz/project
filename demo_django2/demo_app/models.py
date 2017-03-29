# coding:utf-8
from django.db import models
import time
# Create your models here.


class User(models.Model):

    username = models.CharField(verbose_name=u'用户名', max_length=20)
    password = models.CharField(verbose_name=u'用户密码', max_length=20)

    class Meta:
        verbose_name = u'用户表'
        verbose_name_plural = verbose_name
        # ordering = ['id']
        db_table = 'user'

    def __unicode__(self):
        return self.username


class Author(models.Model):
    name = models.CharField(verbose_name=u'作者名称', max_length=20)
    address = models.TextField(verbose_name=u'作者地址')
    city = models.CharField(verbose_name=u'所在城市', max_length=50)

    class Meta:
        verbose_name = u'作者表'
        verbose_name_plural = verbose_name
        db_table = 'author'

    def __str__(self):
        return self.name


class Book(models.Model):

    CHENGDU = 'CD'
    SHANGHAI = 'SH'
    BEIJIN = 'BJ'

    PRODUCT_TYPES = (
        (CHENGDU, '四川大学'),
        (SHANGHAI, '上海大学'),
        (BEIJIN, '北京大学'),
    )

    title = models.CharField(verbose_name=u'标签', max_length=20)
    name = models.CharField(verbose_name=u'书名', max_length=20)
    price = models.FloatField(verbose_name=u'价格')
    publishing = models.CharField(verbose_name=u'出版社', choices=PRODUCT_TYPES, default=CHENGDU, max_length=50)
    product_date = models.DateTimeField(verbose_name=u'出版时间',
                                        # default=time.strftime('%Y%m%d', time.localtime(time.time())),
                                        max_length=30)
    # 2015-12-23 20:51:27
    book_img = models.ImageField(u'封面', upload_to='cart/%Y/%M')
    author = models.ForeignKey(Author)
    # cart = models.ForeignKey(Cart)

    class Meta:
        verbose_name = u'书籍表'
        verbose_name_plural = verbose_name
        ordering = ['-product_date']
        db_table = 'book'

    def __unicode__(self):
        return self.name


class Cart(models.Model):
    qty = models.IntegerField(verbose_name=u'购买数量', default = 1)
    username = models.CharField(verbose_name=u'用户名', max_length=30)
    book = models.ManyToManyField(Book)

    class Meta:
        verbose_name = u'购物车'
        verbose_name_plural = verbose_name
        db_table = 'cart'
        ordering = ['-id']

    # def __str__(self):
    #     return self.username


