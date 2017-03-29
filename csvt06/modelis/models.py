from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name


class Book(models.Model):
    name=models.CharField(max_length=30)
    authors = models.ManyToManyField(Author)
    
    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=20)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return self.name