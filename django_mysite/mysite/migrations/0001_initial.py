# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('counter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'answers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'Email address', db_index=True)),
                ('username', models.CharField(unique=True, max_length=50, db_index=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('sex', models.IntegerField(default=1)),
                ('url', models.URLField(null=True)),
                ('desc', models.CharField(max_length=2000, null=True)),
                ('avatar', models.CharField(max_length=500, null=True)),
                ('token', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('publish', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('answers', models.ManyToManyField(to='mysite.Answer')),
                ('questioner', models.ForeignKey(to='mysite.MyUser')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Questions',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answer',
            name='respondent',
            field=models.ForeignKey(to='mysite.MyUser'),
            preserve_default=True,
        ),
    ]
