# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pro_name', models.CharField(max_length=20, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('pro_city', models.CharField(max_length=20, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82')),
                ('pro_pwd', models.CharField(max_length=20, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('pro_pb', models.CharField(default=b'dahao', max_length=20, verbose_name=b'\xe5\x9e\x8b\xe5\x8f\xb7', choices=[(b'dahao', b'\xe5\xa4\xa7\xe5\x8f\xb7'), (b'zhonghao', b'\xe4\xb8\xad\xe5\x8f\xb7'), (b'xiaohao', b'\xe5\xb0\x8f\xe5\x8f\xb7')])),
                ('pro_style', models.CharField(default=b'sd', max_length=20, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'sd', b'\xe9\xa3\x9f\xe5\x93\x81'), (b'dq', b'\xe7\x94\xb5\xe5\x99\xa8'), (b'kg', b' ')])),
                ('pro_qty', models.IntegerField(default=0, verbose_name=b'\xe5\xba\x93\xe5\xad\x98')),
                ('pro_price', models.FloatField(default=0.0, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('pro_remark', models.TextField(max_length=200, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
            ],
        ),
    ]
