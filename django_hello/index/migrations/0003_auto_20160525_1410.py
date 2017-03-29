# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20160525_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pro_qty',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f'),
        ),
    ]
