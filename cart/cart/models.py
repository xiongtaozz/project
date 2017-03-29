# coding:utf-8
from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def __unicode__(self):
        return self.username

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    book_name=models.CharField(max_length=30)
    book_path=models.CharField(max_length=30)
    authors=models.ForeignKey(Author)

    def __unicode__(self):
        return self.book_name

class Cart(models.Model):
    # id 增长
     book_name=models.CharField(max_length=30)
     qty=models.IntegerField(max_length=10)
     price =models.FloatField(max_length=10)

     def __unicode__(self):
         return self.book_name

