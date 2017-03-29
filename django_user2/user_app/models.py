# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


'''
    在系统user表里面添加信息
    第一种方法:
    替换user
'''


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
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


class MyUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name='email', blank=True, unique=True)
    is_staff = models.BooleanField('staff status', default=True)
    description = models.TextField(max_length=256, default="", blank=True)
    headImage = models.ImageField(upload_to='/image/users/', null=True, blank=True)
    scope = models.IntegerField(default=100)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        # full_name = '%s %s' % (self.first_name, self.last_name)
        return self.email

    def get_short_name(self):
        "Returns the short name for the user."
        return self.email
    # REQUIRED_FIELDS = [USERNAME_FIELD]

'''
 第二种方法:从user 派生
'''


# class MyUser(User):
#
#     description = models.TextField(max_length=256, default="", blank=True)
#     headImage = models.ImageField(upload_to='/image/users/', null=True, blank=True)
#     scope = models.IntegerField(default=100)

    # objects = UserManager()


'''
    第三种方式:表关联方式  -->扩展user
'''


# class MyUser(models.Model):
#     user = models.OneToOneField(User)
#     description = models.TextField(max_length=256, default="", blank=True)
#     headImage = models.ImageField(upload_to='/image/users/', null=True, blank=True)
#     scope = models.IntegerField(default=100)


