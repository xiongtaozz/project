# coding:utf-8
from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20, help_text=_('userName'))
    password = models.CharField(_('password'), max_length=20)