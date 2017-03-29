# -*- coding:utf-8 -*-
from django.db import models
from django import forms
# Create your models here.
class Word(models.Model):
    # id
    word_value = models.CharField(max_length=30, verbose_name='词语内容')
    class Meta:
        verbose_name = '词语'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.word_value

# class quesForm(forms.ModelForm):
#     class Meta:
#         models=Question
#         fields=['__all__']


class Question(models.Model):
    title = models.CharField('标题', max_length=150)
    body = models.TextField('问题内容')
    created = models.DateTimeField('创建时间', auto_now_add=True)
    modified = models.DateTimeField('修改时间', auto_now=True)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = '问题'
        verbose_name_plural = '问题'
        ordering = ['-created']
class Answer(models.Model):
    body = models.TextField('答案内容')
    created = models.DateTimeField('创建时间', auto_now_add=True)
    modified = models.DateTimeField('修改时间', auto_now=True)
    count = models.IntegerField('计数', default=0,null=True)
    question = models.ForeignKey(Question, blank=True, null=True, verbose_name='问题')
    def __unicode__(self):
        return self.body
    class Meta:
        verbose_name = '答案'
        verbose_name_plural = '答案'
        ordering = ['-created']
class Comment(models.Model):
    body = models.CharField('评论内容', max_length=500)
    question = models.ForeignKey(Question, blank=True, null=True, verbose_name='问题')
    answer = models.ForeignKey(Answer, blank=True, null=True, verbose_name='答案')
    def __unicode__(self):
        return self.body

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'