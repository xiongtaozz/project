# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
import time

'''
  用户信息表
'''


# 用户模型.
# 第一种：采用的继承方式扩展用户信息（本系统采用）
# 扩展：关联的方式去扩展用户信息
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png',
                               max_length=200, blank=True, null=True, verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username


'''
   基础信息管理表
'''


# 款式信息表 style
class Style(models.Model):

    name = models.CharField(max_length=10, blank=True, null=True, verbose_name='款式名称')
    is_start = models.BooleanField(default=True, verbose_name='是否启用')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '款式信息表'
        verbose_name_plural = 'styles'
        ordering = ['-create_time']
        db_table = 'style'

    def __unicode__(self):   # 3.x ---> __str__
        return self.name


# 特殊款信息表 SpecialStyle
class SpecialStyle(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True, verbose_name='特殊款名称')
    is_start = models.BooleanField(default=True, verbose_name='是否启用')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '特殊款信息表'
        verbose_name_plural = 'SpecialStyles'
        ordering = ['-create_time']
        db_table = 'specialStyles'

    def __unicode__(self):
        return self.name


# 系列信息表 series
class Series(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True, verbose_name='系列名称')
    is_start = models.BooleanField(default=True, verbose_name='是否启用')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '系列信息表'
        verbose_name_plural = 'series'
        ordering = ['-create_time']
        db_table = 'series'

    def __unicode__(self):
        return self.name


# 主石信息表 stone
class Stone(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True, verbose_name='主石名称')
    is_start = models.BooleanField(default=True, verbose_name='是否启用')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '主石信息表'
        verbose_name_plural = 'stones'
        ordering = ['-create_time']
        db_table = 'stone'

    def __unicode__(self):
        return self.name


# 工艺信息表
class Technology(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True, verbose_name='工艺名称')
    is_start = models.BooleanField(default=True, blank=True, verbose_name='是否启用')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '工艺信息表'
        verbose_name_plural = 'technologys'
        ordering = ['-create_time']
        db_table = 'sechnology'

    def __unicode__(self):
        return self.name


# 属性信息表
class Attribute(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True, verbose_name='属性名称')
    is_start = models.BooleanField(default=True, verbose_name='是否启用')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '属性信息表'
        verbose_name_plural = 'attrbutes'
        ordering = ['-create_time']
        db_table = 'attribute'


# 金成色信息表
class JinChengshai(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True, verbose_name='金成色信息表')
    is_start = models.BooleanField(default=True, blank=True, verbose_name='是否启用')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '金成色信息表'
        verbose_name_plural = 'jcs'
        ordering = ['-create_time']
        db_table = 'jin_cheng_shai'


# 款式类型
class StyleType(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name='类型名称')
    is_start = models.BooleanField(default=True, blank=True, verbose_name='是否启用')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '款式类型信息表'
        verbose_name_plural = 'styleTypes'
        ordering = ['-create_time']
        db_table = 'style_type'


# 分类信息表 Classified
class Classified(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True, verbose_name='分类名称')
    is_start = models.BooleanField(default=True, blank=True, verbose_name='是否启用')
    create_time = models.DateTimeField(auto_now_add=True,  verbose_name='创建时间')

    class Meta:
        verbose_name = '分类信息表'
        verbose_name_plural = 'classfieds'
        ordering = ['-create_time']
        db_table = 'class_fied'


# 供应商 supplier
class Supplier(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True, verbose_name='供应名称')
    is_start = models.BooleanField(default=True, blank=True, verbose_name='是否启用')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '供应商信息表'
        verbose_name_plural = 'supplier'
        ordering = ['-create_time']
        db_table = 'supplier'


# 版号信息管理表
class VersionManagement(models.Model):

    vern_number = models.CharField(max_length=13, unique=True, blank=True, null=True, verbose_name='版号')
    price = models.FloatField(default=0.0, blank=True, null=True, verbose_name='价格')
    vern_img = models.ImageField(upload_to='version/%Y/%m', default='version/default.png', verbose_name='图片')
    class_fied = models.OneToOneField(Classified, blank=False, null=False, verbose_name='分类ID')
    supplier = models.OneToOneField(Supplier, blank=False, null=False, verbose_name='供应商ID')
    styleType = models.OneToOneField(StyleType, blank=False, null=False, verbose_name='款式类型ID')
    jinChengshais = models.ManyToManyField(JinChengshai, verbose_name='金成色关联ID')
    attribute = models.OneToOneField(Attribute, blank=False, null=False, verbose_name='属性ID')
    thls = models.OneToOneField(Technology, blank=False, null=False, verbose_name='工艺ID')
    stone = models.OneToOneField(Stone, blank=False, null=False, verbose_name='主石ID')
    series = models.OneToOneField(Series, blank=False, null=False, verbose_name='系列ID')
    specialStyle = models.OneToOneField(SpecialStyle, blank=False, null=False, verbose_name='特殊款ID')
    style = models.OneToOneField(Style, blank=False, null=False, verbose_name='特殊ID')
    is_start = models.BooleanField(default=True, verbose_name='版号是否启用')

    class Meta:
        verbose_name = '版号管理表'
        verbose_name_plural = 'vers'
        db_table = 'veriosn_manage'

    def __unicode__(self):
        return self.vern_number


# 购物车信息管理表
class ShoppingCart(models.Model):
    name = models.ForeignKey(User, blank=False, null=False, verbose_name='用户关联')
    ver_num = models.OneToOneField(VersionManagement, blank=True, null=True, verbose_name='关联商品(版号)')
    qty = models.IntegerField(default=1, blank=False, null=True, verbose_name='购买数量')

    class Meta:
        verbose_name = '购物车信息管理表'
        verbose_name_plural = 'shops'
        ordering = ['-pk']
        db_table = 'shopping_cart'

    def __unicode__(self):
        return self.name


# manager管理器 为定判断订单编号
# class OrderDetailsTableManager(models.Manager):
#
#     def ver_no(self):
#         # 查询出所有数据
#         oderTable = self.filter(order_date__icontains=
#                                 time.strftime('%Y%m%d', time.localtime(time.time()))).order_by('-order_date')
#         # oderTable = super(OrderDetailsTableManager, self).get_query_set().\
#         #     filter(order_date__icontains=time.strftime('%Y%m%d', time.localtime(time.time()))).order_by('-order_date')
#         if oderTable:
#             str_no = oderTable[0].order_no[8:]
#             str_int = int(str_no)
#             if str_int < 10:
#                 return oderTable[0].order_no[:8] + '000' + (str_int + 1)
#             elif str_int < 100:
#                 return oderTable[0].order_no[:8] + '00' + (str_int + 1)
#             elif str_int < 1000:
#                 return oderTable[0].order_no[:8] + '0' + (str_int + 1)
#             elif str_int < 10000:
#                 return oderTable[0].order_no[:8] + (str_int + 1)
#         else:
#             return time.strftime('%Y%m%d', time.localtime(time.time())) + '0001'
#
#
# # 订单详情表
# class OrderDetailsTable(models.Model):
#
#     type1 = '1'
#     type2 = '2'
#     type3 = '3'
#     type4 = '4'
#     type5 = '5'
#     type6 = '6'
#
#     order_types = (
#         (type1, '订单提交'),
#         (type2, '客户付费'),
#         (type3, '等待发货'),
#         (type4, '发货途中'),
#         (type5, '客户验收'),
#         (type6, '订单完成'),
#     )
#
#     shop = models.OneToOneField(ShoppingCart, blank=True, null=True, verbose_name='购物车信息ID')
#     is_state = models.CharField(default=type1, choices=order_types, blank=True, null=True, verbose_name='订单状态')
#     order_no2 = models.CharField(blank=False, null=False, verbose_name='第二订单编号')
#     order_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='订单日期')
#     objects = models.Manager()
#     order_objects = OrderDetailsTableManager()
#     order_no = models.CharField(default=order_objects.ver_no(), blank=True, null=True, verbose_name='订单号')
#
#     class Meta:
#         verbose_name = 'orderDetail'
#         verbose_name_plural = 'orderds'
#         db_table = 'order_details_table'
#
#     def __unicode__(self):
#         return self.order_no
#
#
# # 订单送货地址
# class Address(models.Model):
#
#     name = models.OneToOneField(User, blank=True, null=True, unique=False, verbose_name='关联用户ID')
#     from_addr = models.CharField(max_length=100, blank=True, null=True, verbose_name='送货地址')
#     oder_table = models.CharField(OrderDetailsTable, blank=False, null=False, verbose_name='关联地址ID')
#
#     class Meta:
#         verbose_name = '订单送货表'
#         verbose_name_plural = 'addresses'
#         db_table = 'address'
#
#     def __unicode__(self):
#         return self.from_addr


