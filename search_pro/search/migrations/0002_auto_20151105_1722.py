# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField(verbose_name=b'\xe7\xad\x94\xe6\xa1\x88\xe5\x86\x85\xe5\xae\xb9')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('count', models.IntegerField(default=0, null=True, verbose_name=b'\xe8\xae\xa1\xe6\x95\xb0')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': '\u7b54\u6848',
                'verbose_name_plural': '\u7b54\u6848',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.CharField(max_length=500, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('answer', models.ForeignKey(verbose_name=b'\xe7\xad\x94\xe6\xa1\x88', blank=True, to='search.Answer', null=True)),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('body', models.TextField(verbose_name=b'\xe9\x97\xae\xe9\xa2\x98\xe5\x86\x85\xe5\xae\xb9')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': '\u95ee\u9898',
                'verbose_name_plural': '\u95ee\u9898',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(verbose_name=b'\xe9\x97\xae\xe9\xa2\x98', blank=True, to='search.Question', null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name=b'\xe9\x97\xae\xe9\xa2\x98', blank=True, to='search.Question', null=True),
        ),
    ]
