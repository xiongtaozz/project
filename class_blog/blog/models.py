#-*- coding: UTF-8 -*-
from django.db import models

#创建用户账号 ---》数据表
class User(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def __unicode__(self):
        return self.username

class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state_provice = models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    website= models.URLField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()

    def __unicode__(self):
        return self.first_name

class Book(models.Model):
    title=models.CharField(max_length=30)
    book_name=models.CharField(max_length=30)
    #书可以由多个作者来完成，作者也有可能完成多本书
    authors=models.ManyToManyField(Author)
    #一本书 对应的作者
    publisher=models.ForeignKey(Publisher)
    publication_date=models.DateField()

    def __unicode__(self):
        return self.title
