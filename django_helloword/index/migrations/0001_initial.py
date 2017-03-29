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
                ('city', models.CharField(default=b'BJ', max_length=20, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82', choices=[(b'CD', b'\xe6\x88\x90\xe9\x83\xbd'), (b'BJ', b'\xe5\x8c\x97\xe4\xba\xac'), (b'SH', b'\xe4\xb8\x8a\xe6\xb5\xb7'), (b'SZ', b'\xe6\xb7\xb1\xe5\x9c\xb3')])),
                ('password', models.CharField(max_length=20, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('pro_model', models.CharField(default=b'MIN', max_length=20, verbose_name=b'\xe5\x9e\x8b\xe5\x8f\xb7', choices=[(b'MIN', b'\xe5\xb0\x8f\xe5\x8f\xb7'), (b'MID', b'\xe4\xb8\xad\xe5\x8f\xb7'), (b'MAX', b'\xe5\xa4\xa7\xe5\x8f\xb7')])),
                ('pro_style', models.CharField(default=b'KK', max_length=20, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'SP', b'\xe9\xa3\x9f\xe5\x93\x81'), (b'DQ', b'\xe7\x94\xb5\xe5\x99\xa8'), (b'KK', b'   ')])),
                ('qty', models.IntegerField(default=1, verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
                ('price', models.FloatField(default=0.0, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('remake', models.TextField(max_length=200, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='index.Tag', verbose_name=b'\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97'),
        ),
    ]
