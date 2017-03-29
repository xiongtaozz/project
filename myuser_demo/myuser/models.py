# coding: utf-8
from django.db import models
from django.contrib.auth.models import User, AbstractUser, \
    AbstractBaseUser, PermissionsMixin, UserManager, BaseUserManager
from django.utils import six, timezone

# Create your models here.
# 希望在原有用户模型上扩展出QQ和Phone的字段信息
# 方式一（推荐方式）：生成的用户信息在一张表里面，适用于用户信息字段比较少的时候
# User：用户类 （swappable = 'AUTH_USER_MODEL' 插拔配置的内容）
# AnonymousUser：匿名用户类（游客）
# AbstractUser：抽象用户类
# AbstractBaseUser：抽象用户基类
# PermissionsMixin：权限管理（混合）类
# from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
# 采用继承方式扩展用户资料（1、从AbstractUser；2、从AbstractBaseUser）
#
# 定义自定义用户model
# AUTH_USER_MODEL

# class UserProfile(AbstractUser):
#     qq = models.CharField(max_length=13, null=True, blank=True, verbose_name="qq")
#     phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="phone")


class UserProfileManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError(u'email不能为空')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


# 我可能不是想扩展用户信息，而是想缩减用户信息
class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', blank=True, unique=True)
    qq = models.CharField(max_length=13, null=True, blank=True, verbose_name="qq")
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="phone")
    is_staff = models.BooleanField('staff status', default=False,)
    is_active = models.BooleanField('active', default=True,)
    date_joined = models.DateTimeField('date joined', default=timezone.now,)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

# 方式二：
# 采用Profile方式(关联的方式)进行用户信息拓展
# 其实就是有一个新的用户model关联（一对一关联）上django原有的User
# 会产生多张用户信息的表
# 不是首要推荐的方式，这种方式适用于用户信息字段特别多的时候。

# class UserProfile(User):
#     qq = models.CharField(max_length=13, null=True, blank=True, verbose_name="qq")
#     phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="phone")
#     # user = models.ForeignKey(User, unique=True)
#     # user = models.OneToOneField(User)

# 方式三 继承user
# class UserProfile(User):
#     pass


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"标题")
    content = models.TextField(verbose_name=u"内容")

    class Meta:
        permissions = (
            ("view_article", "can view article"),
        )