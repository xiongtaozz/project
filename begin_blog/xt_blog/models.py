#coding=utf-8
from django.db import models

class User(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def __unicode__(self):
        return self.username

class Author(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=40)
    email=models.EmailField()

    def __unicode__(self):
        return self.first_name

class Publicsher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state_provice = models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    website= models.URLField()


    def __unicode__(self):
        return  self.name
class Book(models.Model):
    title=models.CharField(max_length=30)
    book_name=models.CharField(max_length=30)
    #书可以由多个作者来完成，作者也有可能完成多本书
    authors=models.ManyToManyField(Author)
    #一本书 对应的作者
    publisher=models.ForeignKey(Publicsher)
    publication_date=models.DateField()

    def __unicode__(self):
        return self.title


class Blog(models.Model):
    name=models.CharField(max_length=100)
    tagline=models.TextField()

    def __unicode__(self):
        return self.name

class Entry(models.Model):
    blog=models.ForeignKey(Blog)
    headline=models.CharField(max_length=255)
    body_text=models.TextField()
    pub_date=models.DateField()
    mod_date=models.DateField()
    authors=models.ManyToManyField(Author)
    n_comments=models.IntegerField()
    n_pingbacks=models.IntegerField()
    rating=models.IntegerField()

    def __str__(self):
        return self.headline





