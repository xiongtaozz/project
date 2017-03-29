# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pro_qty',
            field=models.ImageField(default=1, upload_to=b'', verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='product',
            name='password',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pro_model',
            field=models.CharField(default=b'MIN', max_length=20, verbose_name=b'\xe5\x9e\x8b\xe5\x8f\xb7', choices=[(b'MIN', b'\xe5\xb0\x8f\xe5\x8f\xb7'), (b'MED', b'\xe4\xb8\xad\xe5\x8f\xb7'), (b'MAX', b'\xe5\xa4\xa7\xe5\x8f\xb7')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='pro_style',
            field=models.CharField(default=b'DQ', max_length=20, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab', choices=[(b'DQ', b'\xe7\x94\xb5\xe5\x99\xa8'), (b'SP', b'\xe9\xa3\x9f\xe5\x93\x81'), (b'KL', b'   ')]),
        ),
    ]
