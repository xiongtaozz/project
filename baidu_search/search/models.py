# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Word(models.Model):
    word_value = models.CharField(max_length=30, verbose_name='词语内容')

    class Meta:
        verbose_name = '词语'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.word_value