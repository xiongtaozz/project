# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-04 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_month_des'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='year',
            name='id',
        ),
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='\u4f1a\u8ba1\u5e74\u5ea6'),
        ),
    ]
