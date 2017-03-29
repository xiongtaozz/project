# coding:utf=8
from django.db import models

class creater(models.Model):
    editer = models.CharField(u'作者', max_length=200)
    ago = models.IntegerField(u'年龄', default=27)

    def __str__(self):
        return self.editer

class main(models.Model):
    title = models.CharField(u'标题', max_length=200)
    content = models.TextField(u'内容')
    editer = models.ForeignKey(creater)

    def __str__(self):
        return self.title


