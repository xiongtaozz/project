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
                ('city', models.CharField(default=b'CD', max_length=20, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82', choices=[(b'CD', b'\xe6\x88\x90\xe9\x83\xbd'), (b'SH', b'\xe4\xb8\x8a\xe6\xb5\xb7'), (b'BJ', b'\xe5\x8c\x97\xe4\xba\xac'), (b'SZ', b'\xe6\xb7\xb1\xe5\x9c\xb3')])),
                ('password', models.CharField(default=b'MIN', max_length=20, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81', choices=[(b'MIN', b'\xe5\xb0\x8f\xe5\x8f\xb7'), (b'MED', b'\xe4\xb8\xad\xe5\x8f\xb7'), (b'MAX', b'\xe5\xa4\xa7\xe5\x8f\xb7')])),
                ('pro_model', models.CharField(default=b'DQ', max_length=20, verbose_name=b'\xe5\x9e\x8b\xe5\x8f\xb7', choices=[(b'DQ', b'\xe7\x94\xb5\xe5\x99\xa8'), (b'SP', b'\xe9\xa3\x9f\xe5\x93\x81'), (b'KL', b'   ')])),
                ('pro_style', models.CharField(max_length=20, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab')),
                ('pro_price', models.FloatField(default=0.0, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('pro_remark', models.TextField(max_length=200, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key_word', models.CharField(max_length=20, verbose_name=b'\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='index.Tag'),
        ),
    ]
