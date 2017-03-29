from django.db import models

# Create your models here.


class FileUrl(models.Model):
    url = models.FileField(upload_to='/xls')

    def __unicode__(self):
        return self.url
