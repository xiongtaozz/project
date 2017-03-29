# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'用户名')
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png',
                               max_length=200, blank=True, null=True, verbose_name=u'用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'QQ号')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name=u'手机号码')

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(default='个人博客',
                            max_length=30, verbose_name=u'标签名称')

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'分类名称')
    index = models.IntegerField(default=999, verbose_name=u'分类排序')

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    class Meta:
        verbose_name = u'作者'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name


class Article(models.Model):
    caption = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'文章标题')
    desc = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'文章描述')
    content = models.TextField(verbose_name=u'文章内容', blank=True, null=True,)
    click_count = models.IntegerField(default=0, verbose_name=u'点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name=u'是否推荐')
    date_publish = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name=u'发布时间')
    date_update = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name=u'更新时间')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name=u'分类')
    tag = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')
    author = models.ForeignKey(Author, blank=True, null=True, verbose_name=u'文章作者')

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']



