# - * - coding:utf8 - * -
from django.db import models

# Create your models here.

class Item(models.Model):
    content = models.CharField(max_length=200,verbose_name= u'待办事项内容')
    flag = models.BooleanField(default=False,verbose_name=u'待办事项状态')
    pubdate = models.DateTimeField(auto_now_add=True,verbose_name=u'发布时间')

    class Meta:
        verbose_name = u'待办事项'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content




