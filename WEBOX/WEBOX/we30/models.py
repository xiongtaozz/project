from django.db import models


# Create your models here.

class we30_1st(models.Model):
    type = models.CharField(max_length=10)
    order_number = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100, blank=True)
    SN = models.CharField(max_length=30)
    MAC = models.CharField(max_length=30, blank=True)
    question = models.CharField(max_length=300, blank=True)
    phenomenon = models.CharField(max_length=50, blank=True)
    question_type = models.CharField(max_length=10)
    reason = models.CharField(max_length=20)
    ranges = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')

    def time(self):
        return self.pub_date

    def __unicode__(self):
        return self.SN


class we30_2nd(models.Model):
    type = models.CharField(max_length=10)
    order_number = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100, blank=True)
    SN = models.CharField(max_length=30)
    MAC = models.CharField(max_length=30, blank=True)
    question = models.CharField(max_length=300, blank=True)
    phenomenon = models.CharField(max_length=50, blank=True)
    question_type = models.CharField(max_length=10)
    reason = models.CharField(max_length=20)
    ranges = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')

    def time(self):
        return self.pub_date

    def __unicode__(self):
        return self.SN

class we30_3th(models.Model):
    type = models.CharField(max_length=10)
    order_number = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100, blank=True)
    SN = models.CharField(max_length=30)
    MAC = models.CharField(max_length=30, blank=True)
    question = models.CharField(max_length=300, blank=True)
    phenomenon = models.CharField(max_length=50, blank=True)
    question_type = models.CharField(max_length=10)
    reason = models.CharField(max_length=20)
    ranges = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')

    def time(self):
        return self.pub_date

    def __unicode__(self):
        return self.SN


class we30_4th(models.Model):
    type = models.CharField(max_length=10)
    order_number = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100, blank=True)
    SN = models.CharField(max_length=30)
    MAC = models.CharField(max_length=30, blank=True)
    question = models.CharField(max_length=300, blank=True)
    phenomenon = models.CharField(max_length=50, blank=True)
    question_type = models.CharField(max_length=10)
    reason = models.CharField(max_length=20)
    ranges = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    def time(self):
        return self.pub_date

    def __unicode__(self):
        return self.SN

class we30_5th(models.Model):
    type = models.CharField(max_length=10)
    order_number = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100, blank=True)
    SN = models.CharField(max_length=30)
    MAC = models.CharField(max_length=30, blank=True)
    question = models.CharField(max_length=300, blank=True)
    phenomenon = models.CharField(max_length=50, blank=True)
    question_type = models.CharField(max_length=10)
    reason = models.CharField(max_length=20)
    ranges = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')

    def time(self):
        return self.pub_date

    def __unicode__(self):
        return self.SN

class we30_6th(models.Model):
    type = models.CharField(max_length=10)
    order_number = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100, blank=True)
    SN = models.CharField(max_length=30)
    MAC = models.CharField(max_length=30, blank=True)
    question = models.CharField(max_length=300, blank=True)
    phenomenon = models.CharField(max_length=50, blank=True)
    question_type = models.CharField(max_length=10)
    reason = models.CharField(max_length=20)
    ranges = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')

    def time(self):
        return self.pub_date

    def __unicode__(self):
        return self.SN

class we30_7th(models.Model):
    type = models.CharField(max_length=10)
    order_number = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100, blank=True)
    SN = models.CharField(max_length=30)
    MAC = models.CharField(max_length=30, blank=True)
    question = models.CharField(max_length=300, blank=True)
    phenomenon = models.CharField(max_length=50, blank=True)
    question_type = models.CharField(max_length=10)
    reason = models.CharField(max_length=20)
    ranges = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')

    def time(self):
        return self.pub_date

    def __unicode__(self):
        return self.SN

class we30_8th(models.Model):
    type = models.CharField(max_length=10)
    order_number = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100, blank=True)
    SN = models.CharField(max_length=30)
    MAC = models.CharField(max_length=30, blank=True)
    question = models.CharField(max_length=300, blank=True)
    phenomenon = models.CharField(max_length=50, blank=True)
    question_type = models.CharField(max_length=10)
    reason = models.CharField(max_length=20)
    ranges = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    def time(self):
        return self.pub_date

    def __unicode__(self):
        return self.SN

class we30_9th(models.Model):
    type = models.CharField(max_length=10)
    order_number = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100, blank=True)
    SN = models.CharField(max_length=30)
    MAC = models.CharField(max_length=30, blank=True)
    question = models.CharField(max_length=300, blank=True)
    phenomenon = models.CharField(max_length=50, blank=True)
    question_type = models.CharField(max_length=10)
    reason = models.CharField(max_length=20)
    ranges = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')

    def time(self):
        return self.pub_date

    def __unicode__(self):
        return self.SN

class we30_10th(models.Model):
    type = models.CharField(max_length=10)
    order_number = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100, blank=True)
    SN = models.CharField(max_length=30)
    MAC = models.CharField(max_length=30, blank=True)
    question = models.CharField(max_length=300, blank=True)
    phenomenon = models.CharField(max_length=50, blank=True)
    question_type = models.CharField(max_length=10)
    reason = models.CharField(max_length=20)
    ranges = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    def time(self):
        return self.pub_date

    def __unicode__(self):
        return self.SN