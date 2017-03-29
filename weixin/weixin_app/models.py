# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class KeyWord(models.Model):
    keyWord = models.CharField(max_length=256, primary_key=True, help_text='用户发送的关键字', verbose_name='关键词')
    content = models.TextField(null=True, blank=True, help_text='回复用户内容', verbose_name='内容')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    published = models.BooleanField(default=True, verbose_name='发布状态')

    def __unicode__(self):
        return self.keyWord

    class Meta:
        verbose_name = '关键词'
        verbose_name_plural = verbose_name

