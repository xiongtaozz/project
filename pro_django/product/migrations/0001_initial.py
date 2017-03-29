# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='\u5206\u7c7b\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u5206\u7c7b',
                'verbose_name_plural': '\u4ea7\u54c1\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='\u5173\u952e\u8bcd')),
            ],
            options={
                'verbose_name': '\u5173\u952e\u8bcd',
                'verbose_name_plural': '\u5173\u952e\u8bcd',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('stock', models.IntegerField(default=100, verbose_name='\u5e93\u5b58\u6570\u91cf')),
                ('price', models.DecimalField(default=10.0, verbose_name='\u4ea7\u54c1\u4ef7\u683c', max_digits=8, decimal_places=2)),
                ('desc', models.TextField(null=True, verbose_name='\u4ea7\u54c1\u63cf\u8ff0', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65e5\u671f')),
                ('cate', models.ForeignKey(verbose_name='\u4ea7\u54c1\u7c7b\u522b', to='product.Category')),
                ('key', models.ManyToManyField(to='product.Keyword', verbose_name='\u5173\u952e\u8bcd')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u4ea7\u54c1',
                'verbose_name_plural': '\u4ea7\u54c1',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe5\xa4\xa7\xe5\xb0\x8f')),
            ],
            options={
                'verbose_name': '\u578b\u53f7',
                'verbose_name_plural': '\u578b\u53f7',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='spec',
            field=models.ForeignKey(verbose_name='\u4ea7\u54c1\u578b\u53f7', to='product.Size'),
        ),
    ]
