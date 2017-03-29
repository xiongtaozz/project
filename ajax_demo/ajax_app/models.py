from django.db import models

# Create your models here.


class User(models.Model):
    uername = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class City(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Us(models.Model):
    name = models.CharField(max_length=20)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return self.name