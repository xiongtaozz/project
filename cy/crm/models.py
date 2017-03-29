# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from general.models import Company,Depts,Year,Month,Subject
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
#预算录入
class Budget(models.Model):
    TYPES = (
        (1, u'预算导入'),
        (2, u'预算录入'),
        (3, u'预算追加'),
        (4, u'预算调整'),
    )
    num = models.CharField(primary_key=True,max_length=20, verbose_name=u'单据号')
    company = models.ForeignKey(Company, verbose_name=u'所属公司')
    type = models.IntegerField(choices=TYPES, default=1, verbose_name=u'预算类型')
    year = models.ForeignKey(Year, verbose_name=u'预算年度')
    month = models.ForeignKey(Month, verbose_name=u'预算期间')
    cruser = models.ForeignKey(User, verbose_name=u'创建用户')
    crdate = models.DateField(verbose_name=u'创建日期')
    moduser = models.CharField(max_length=20, blank=True, null=True,verbose_name=u'修改用户')
    moddate = models.DateField( blank=True, null=True,verbose_name='u修改日期',)

    class Meta:
            verbose_name = u"预算头"

class Budgetd(Budget):
    line= models.IntegerField(verbose_name=u'行号')
    subject = models.ForeignKey(Subject, verbose_name=u'预算科目')
    dept = models.ForeignKey(Depts, verbose_name=u'预算部门')
    amt=models.DecimalField(max_digits=125,decimal_places=2,verbose_name=u'金额')
    class Meta:
            verbose_name = u"预算明细"
