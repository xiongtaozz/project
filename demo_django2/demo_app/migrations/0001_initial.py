# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u4f5c\u8005\u540d\u79f0')),
                ('address', models.TextField(verbose_name='\u4f5c\u8005\u5730\u5740')),
                ('city', models.CharField(max_length=50, verbose_name='\u6240\u5728\u57ce\u5e02')),
            ],
            options={
                'db_table': 'author',
                'verbose_name': '\u4f5c\u8005\u8868',
                'verbose_name_plural': '\u4f5c\u8005\u8868',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20, verbose_name='\u6807\u7b7e')),
                ('name', models.CharField(max_length=20, verbose_name='\u4e66\u540d')),
                ('price', models.FloatField(verbose_name='\u4ef7\u683c')),
                ('publishing', models.CharField(default=b'CD', max_length=50, verbose_name='\u51fa\u7248\u793e', choices=[(b'CD', b'\xe5\x9b\x9b\xe5\xb7\x9d\xe5\xa4\xa7\xe5\xad\xa6'), (b'SH', b'\xe4\xb8\x8a\xe6\xb5\xb7\xe5\xa4\xa7\xe5\xad\xa6'), (b'BJ', b'\xe5\x8c\x97\xe4\xba\xac\xe5\xa4\xa7\xe5\xad\xa6')])),
                ('product_date', models.DateTimeField(max_length=30, verbose_name='\u51fa\u7248\u65f6\u95f4')),
                ('book_img', models.ImageField(upload_to=b'cart/%Y/%M', verbose_name='\u5c01\u9762')),
                ('author', models.ForeignKey(to='demo_app.Author')),
            ],
            options={
                'ordering': ['-product_date'],
                'db_table': 'book',
                'verbose_name': '\u4e66\u7c4d\u8868',
                'verbose_name_plural': '\u4e66\u7c4d\u8868',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField(default=1, verbose_name='\u8d2d\u4e70\u6570\u91cf')),
                ('username', models.CharField(max_length=30, verbose_name='\u7528\u6237\u540d')),
                ('book', models.ManyToManyField(to='demo_app.Book')),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'cart',
                'verbose_name': '\u8d2d\u7269\u8f66',
                'verbose_name_plural': '\u8d2d\u7269\u8f66',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=20, verbose_name='\u7528\u6237\u5bc6\u7801')),
            ],
            options={
                'db_table': 'user',
                'verbose_name': '\u7528\u6237\u8868',
                'verbose_name_plural': '\u7528\u6237\u8868',
            },
        ),
    ]
