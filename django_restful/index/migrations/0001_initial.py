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
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('style', models.CharField(default=b'ZH', max_length=20, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'DH', b'\xe5\xa4\xa7\xe5\x8f\xb7'), (b'ZH', b'\xe4\xb8\xad\xe5\x8f\xb7'), (b'XH', b'\xe5\xb0\x8f\xe5\x8f\xb7')])),
                ('qty', models.IntegerField(default=1, verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
                ('price', models.FloatField(default=0.0, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('city', models.CharField(max_length=20, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82')),
                ('remark', models.TextField(verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
            ],
            options={
                'ordering': ['pk'],
                'db_table': 'Product',
                'verbose_name': '\u4ea7\u54c1\u8868',
                'verbose_name_plural': '\u4ea7\u54c1\u8868',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=20, verbose_name=b'\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97')),
            ],
            options={
                'ordering': ['pk'],
                'db_table': 'Tag',
                'verbose_name': '\u5173\u952e\u5b57\u8868',
                'verbose_name_plural': '\u5173\u952e\u5b57\u8868',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='keys',
            field=models.ForeignKey(verbose_name=b'\xe5\x85\xb3\xe8\x81\x94id', to='index.Tag'),
        ),
    ]
