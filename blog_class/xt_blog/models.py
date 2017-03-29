from django.db import models

# Create your models here.


class Techer(models.Model):
    name=models.CharField(max_length=30)

    def __unicode__(self):
        return self.name
class Student(models.Model):
    name=models.CharField(max_length=30)
    techers= models.ManyToManyField(Techer)

    def __unicode__(self):
        return self.name


