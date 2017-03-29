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
                ('title', models.CharField(max_length=30, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('description', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('photo', models.ImageField(upload_to=b'', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('price', models.FloatField(verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
