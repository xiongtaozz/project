#coding:utf-8
from django.db import models
from django.contrib.auth.models import User,AbstractUser,AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import  timezone


# Create your models here.

# class UserManager(BaseUserManager):
#
#     use_in_migrations=True
#     def _create_user(self, email, password,is_supperuser,**extra_fields):
#         """
#         Creates and saves a User with the given username, email and password.
#         """
#         now = timezone.now()
#         if not email:
#             raise ValueError('The given username must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email,is_active=True,
#                             is_supperuser=is_supperuser,
#                             last_login=now,
#                             **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email=None, password=None, **extra_fields):
#         return self._create_user(email,password, False, **extra_fields)
#
#     def create_superuser(self, username, email, password, **extra_fields):
#         return self._create_user(username, email, password,  True,
#                                  **extra_fields)
#
class MyUser(AbstractUser):
    address = models.CharField(max_length=30)




# class Profile(models.Model):
#     user = models.OneToOneField(User)
#
#     blog = models.CharField(max_length=128,blank=True)
#     location = models.CharField(max_length=128,blank=True)
#     occupation= models.CharField(max_length=128,blank=True)
#
#     reward = models.IntegerField(default=0,blank=True)
#     topic_count = models.IntegerField(default=0,blank=True)
#     post_count = models.IntegerField(default=0,blank=True)
#
#     class Admin:
#         list_display = ('user', 'blog', 'location', 'occupation', 'reward', 'topic_count', 'post_count')



class Product(models.Model):
    title = models.CharField(max_length=30,verbose_name='标题')
    description = models.TextField(verbose_name='描述')
    photo = models.ImageField(verbose_name='图片')
    price = models.FloatField(verbose_name='价格')

    def __unicode__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=30,verbose_name='作者姓名')
    age = models.IntegerField(verbose_name='年龄')
    address= models.CharField(max_length=30,verbose_name='地址')
    # class Meta:
    #     db_table='verbose_name'

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=30,verbose_name='作者书名')
    price = models.FloatField(verbose_name='价格')
    authors = models.ManyToManyField(Author)
    # models.OneToOneField

    def __unicode__(self):
        return self.title
