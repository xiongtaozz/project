# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cno', models.CharField(max_length=5, serialize=False, verbose_name='\u7f16\u53f7', primary_key=True)),
                ('cname', models.CharField(max_length=20, verbose_name='\u8bfe\u7a0b\u540d')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='OptionalCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True, verbose_name='\u9009\u4fee\u65f6\u95f4')),
                ('cno', models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='demo.Course')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u9009\u4fee',
                'verbose_name_plural': '\u8bfe\u7a0b\u9009\u4fee',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.DecimalField(default=60, verbose_name='\u5206\u6570', max_digits=3, decimal_places=1)),
                ('cno', models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='demo.Course')),
            ],
            options={
                'verbose_name': '\u6210\u7ee9',
                'verbose_name_plural': '\u6210\u7ee9',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sname', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('ssex', models.CharField(default='\u4fdd\u5bc6', max_length=4, verbose_name='\u59d3\u540d', choices=[(1, '\u7537'), (2, '\u5973'), (3, '\u4fdd\u5bc6')])),
                ('sbirthday', models.DateField(null=True, verbose_name='\u751f\u65e5', blank=True)),
                ('classno', models.CharField(max_length=5, verbose_name='\u73ed\u7ea7')),
            ],
            options={
                'verbose_name': '\u5b66\u751f',
                'verbose_name_plural': '\u5b66\u751f',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tname', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('tsex', models.CharField(default='\u4fdd\u5bc6', max_length=4, verbose_name='\u59d3\u540d', choices=[(1, '\u7537'), (2, '\u5973'), (3, '\u4fdd\u5bc6')])),
                ('tbirthday', models.DateField(null=True, verbose_name='\u751f\u65e5', blank=True)),
                ('depart', models.CharField(max_length=20, verbose_name='\u6240\u5728\u7cfb')),
            ],
            options={
                'verbose_name': '\u8001\u5e08',
                'verbose_name_plural': '\u8001\u5e08',
            },
        ),
        migrations.AddField(
            model_name='score',
            name='sno',
            field=models.ForeignKey(verbose_name='\u5b66\u751f', to='demo.Student'),
        ),
        migrations.AddField(
            model_name='optionalcourse',
            name='sno',
            field=models.ForeignKey(verbose_name='\u5b66\u751f', to='demo.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='sno',
            field=models.ManyToManyField(to='demo.Student', verbose_name='\u9009\u4fee\u5b66\u751f', through='demo.OptionalCourse'),
        ),
        migrations.AddField(
            model_name='course',
            name='tno',
            field=models.ForeignKey(verbose_name='\u6388\u8bfe\u8001\u5e08', to='demo.Teacher'),
        ),
    ]
