# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-30 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20160629_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name=u'budget',
            name=u'num',
            field=models.CharField(default=1, max_length=20, verbose_name=u'\u5355\u636e\u53f7'),
            preserve_default=False,
        ),
    ]