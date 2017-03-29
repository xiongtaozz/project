# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.



# 公司
class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'描述')
    upcompany = models.ForeignKey('self', blank=True, null=True,verbose_name=u'上级公司')
    address = models.CharField(max_length=100, blank=True, verbose_name=u'地址')
    cruser = models.CharField(max_length=20, verbose_name=u'创建用户')
    crdate = models.DateField(verbose_name=u'创建日期')
    moduser = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'修改用户')
    moddate = models.DateField(verbose_name=u'修改日期', blank=True, null=True)

    def __unicode__(self):
        return self.name
    class Meta:
            verbose_name = "公司"


# 地点
class Fcy(models.Model):
    company = models.ForeignKey(Company, verbose_name=u'所属公司')
    num = models.CharField(max_length=100,verbose_name=u'地点')
    des = models.CharField(max_length=100, verbose_name=u'描述')
    address = models.CharField(max_length=50, blank=True, verbose_name=u'地址')
    cruser = models.CharField(max_length=20, verbose_name=u'创建用户')
    crdate = models.DateField(verbose_name=u'创建日期')
    moduser = models.CharField(max_length=20, blank=True, null=True,verbose_name=u'修改用户')
    moddate = models.DateField(verbose_name=u'修改日期', blank=True,null=True)

    def __unicode__(self):
        return self.des
    class Meta:
            verbose_name = u"地点"
# 部门
class Depts(models.Model):
    TYPES = (
        (1, u'行政部门'),
        (2, u'销售部门'),
        (3, u'生产部门'),
        (4, u'生产辅助部门'),
    )
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name=u'上级部门')
    id = models.CharField(u'部门编码',max_length=30,primary_key=True)
    name = models.CharField('部门名称',max_length=30)
    admin = models.ForeignKey(User, verbose_name=u'部门负债人')
    type = models.IntegerField(choices=TYPES, default=1, verbose_name=u'部门类型')
    cruser = models.CharField(max_length=20, verbose_name=u'创建用户')
    crdate = models.DateField(verbose_name=u'创建日期')
    moduser = models.CharField(max_length=20, blank=True, null=True,verbose_name=u'修改用户')
    moddate = models.DateField(verbose_name=u'修改日期', blank=True, null=True)
    company = models.ForeignKey(Company, verbose_name=u'所属公司')

    def __unicode__(self):
        return self.name
    class Meta:
            verbose_name = u"部门"
# 科目
class Subject(models.Model):
    TYPES = (
        (1, u'资产类'),
        (2, u'负债类'),
        (3, u'所有者权益类'),
        (4, u'成本类'),
        (5, u'损益类'),
        (6, u'其他类'),
    )
    num = models.CharField(primary_key=True,max_length=20,verbose_name=u'科目')
    des = models.CharField(max_length=20, verbose_name=u'描述')
    upnum = models.ForeignKey('self', blank=True, null=True, verbose_name=u'上级科目')
    type = models.IntegerField(choices=TYPES, default=1, verbose_name=u'科目类型')
    bpsflag = models.BooleanField(verbose_name=u'商业伙伴必填')
    Progressflag = models.BooleanField(verbose_name=u'在建工程必填')
    deptflag = models.BooleanField(verbose_name=u'部门必填')
    itmflag = models.BooleanField(verbose_name=u'产品必填')
    cruser = models.ForeignKey(User, verbose_name=u'创建用户')
    crdate = models.DateField(verbose_name=u'创建日期')
    moduser = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'修改用户')
    moddate = models.DateField(verbose_name=u'修改日期', blank=True, null=True)
    company = models.ForeignKey(Company, verbose_name=u'所属公司')

    def __unicode__(self):
        return self.des
    class Meta:
            verbose_name = u"科目"



# 商业伙伴类别
class Bptype(models.Model):
    num = models.IntegerField(verbose_name=u'编码')
    des = models.CharField(max_length=20, verbose_name=u'描述')
    acc = models.ForeignKey(Subject, verbose_name=u'往来科目')
    cruser = models.CharField(max_length=20, verbose_name=u'创建用户')
    crdate = models.DateField(verbose_name=u'创建日期')
    moduser = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'修改用户')
    moddate = models.DateField(verbose_name=u'修改日期', blank=True, null=True)
    company = models.ForeignKey(Company, verbose_name=u'所属公司')


    def __unicode__(self):
        return self.des
    class Meta:
            verbose_name = u"商业伙伴类别"


# 商业伙伴
class Bps(models.Model):
    num = models.IntegerField(verbose_name=u'商业伙伴')
    des = models.CharField(max_length=20, verbose_name=u'描述')
    shorter_des = models.CharField(max_length=15, verbose_name=u'简称')
    type = models.ForeignKey(Bptype, verbose_name=u'类别')
    acc = models.ForeignKey(Subject, verbose_name=u'往来科目')
    tax = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=u'税率')
    cruser = models.CharField(max_length=20, verbose_name=u'创建用户')
    crdate = models.DateField(verbose_name=u'创建日期')
    moduser = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'修改用户')
    moddate = models.DateField(verbose_name=u'修改日期', blank=True, null=True)
    company = models.ForeignKey(Company, verbose_name=u'所属公司')


    def __unicode__(self):
        return self.des
    class Meta:
            verbose_name = u"商业伙伴"





# 会计年度
class Year(models.Model):
    year = models.IntegerField(primary_key=True,verbose_name=u'会计年度')
    des = models.CharField(max_length=20, verbose_name=u'描述')
    cruser = models.CharField(max_length=20, verbose_name=u'创建用户')
    crdate = models.DateField(verbose_name=u'创建日期')
    moduser = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'修改用户')
    moddate = models.DateField(verbose_name=u'修改日期', blank=True, null=True)


    def __unicode__(self):
        return self.des
    class Meta:
            verbose_name = u"年度"


# 会计期间
class Month(models.Model):
    year = models.ForeignKey(Year, verbose_name=u'会计年度')
    month = models.IntegerField(verbose_name=u'期间')
    des = models.CharField(max_length=20, verbose_name=u'描述')
    datedeb = models.DateField(verbose_name=u'开始日期')
    datefin = models.DateField(verbose_name=u'结束日期')
    cruser = models.CharField(max_length=20, verbose_name=u'创建用户')
    crdate = models.DateField(verbose_name=u'创建日期')
    moduser = models.CharField(max_length=20, blank=True, null=True,verbose_name=u'修改用户')
    moddate = models.DateField(verbose_name=u'修改日期', blank=True, null=True)
    company = models.ForeignKey(Company, verbose_name=u'所属公司')
    def __unicode__(self):
        return self.des
    class Meta:
            verbose_name = u"期间"



