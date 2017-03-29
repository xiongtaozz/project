from django.db import models

# Create your models here.


class Product(models.Model):

    title = models.CharField(max_length=20)
    pubmark = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'product'

    def __unicode__(self):
        return self.title