# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='we30p_1st',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=10)),
                ('order_number', models.CharField(max_length=50, blank=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('SN', models.CharField(max_length=30)),
                ('MAC', models.CharField(max_length=30, blank=True)),
                ('question', models.CharField(max_length=300, blank=True)),
                ('phenomenon', models.CharField(max_length=50, blank=True)),
                ('question_type', models.CharField(max_length=10)),
                ('reason', models.CharField(max_length=20)),
                ('ranges', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
