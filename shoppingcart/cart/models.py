from django.db import models

# Create your models here.
class User(models.Model):
     username = models.CharField(max_length=30)
     password = models.CharField(max_length=30)

     def __unicode__(self):
         return self.username

class Author(models.Model):
    name=models.CharField(max_length=30)
    address= models.CharField(max_length=30)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

class Book(models.Model):
    book_name = models.CharField(max_length=30)
    book_path =models.CharField(max_length=30)
    book_price = models.FloatField(max_length=10)
    authors = models.ForeignKey(Author)

    def __unicode__(self):
        return self.book_name

class Cart(models.Model):
    name = models.ForeignKey(User)
    books = models.ForeignKey(Book)
    qty = models.IntegerField(max_length=10)

