# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blog', models.CharField(max_length=128, blank=True)),
                ('location', models.CharField(max_length=128, blank=True)),
                ('occupation', models.CharField(max_length=128, blank=True)),
                ('reward', models.IntegerField(default=0, blank=True)),
                ('topic_count', models.IntegerField(default=0, blank=True)),
                ('post_count', models.IntegerField(default=0, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
