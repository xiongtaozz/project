# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
'''
  @author XT
  @date 2016-4-19
  @path 所有数据模型表
  @makemigrations
  @migrate  只同步数据,不创建超级用户(数据更改)
  @syncdb   同步数据而且还会创建超级用户(同步更改,并创建)
'''


class Techer(models.Model):

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    t_no = models.IntegerField(primary_key=True, verbose_name='教师编号')
    t_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='教师名称')
    t_email = models.EmailField(unique=True, verbose_name='教师邮箱')
    t_sh = models.CharField(max_length=30, choices=YEAR_IN_SCHOOL_CHOICES, default=FRESHMAN, verbose_name='学校')
    t_frist_date = models.DateTimeField(auto_now_add=True, verbose_name='入职时间')
    t_bariy_date = models.DateField(verbose_name='生日')
    t_remark = models.TextField(max_length=200, blank=True, null=True, verbose_name='备注')
    t_photo = models.ImageField(upload_to='techer/%Y/%m', default='/techer/default.jpg', verbose_name='教师图片')
    t_url = models.URLField(default='http://www.maiziedu.com', verbose_name='教师主页')

    class Meta:
        verbose_name = '教师表'
        verbose_name_plural = verbose_name
        ordering = ['-t_no']
        # 如果不添加   默认生成的格式:app_table
        db_table = 'techer'

    def __unicode__(self):
        return self.t_name

'''
 @ForeignKey 多的一方 我可以通过本身的关联属性去查询另外一张的结果
 一的一方他有table_set属性去查询
 @onetoone 本身的关联属性去查询另外一张的结果
 @ManytoMany 双方都用table_set属性去查询
'''


class Student(models.Model):
    stu_name = models.CharField(max_length=20, verbose_name='学生名称')
    techer = models.ForeignKey(Techer, verbose_name='关联教师ID')

    class Meta:
        verbose_name = '学生表'
        verbose_name_plural = verbose_name
        db_table = 'student'

    def __unicode__(self):
        return self.stu_name
