# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creater',
            name='ago',
            field=models.IntegerField(default=27, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='creater',
            name='editer',
            field=models.CharField(max_length=200, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='main',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='main',
            name='title',
            field=models.CharField(max_length=200, verbose_name='标题'),
        ),
    ]
