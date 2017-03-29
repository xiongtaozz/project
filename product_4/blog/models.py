from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)

    def __unicode__(self):
        return self.name

class Artile(models.Model):
    title=models.CharField(max_length=50)
    text_detail=models.TextField()
    author = models.ForeignKey(Author)

    def __unicode__(self):
        return self.title





