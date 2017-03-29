# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-pk'], 'verbose_name': '\u4ea7\u54c1\u8868', 'verbose_name_plural': '\u4ea7\u54c1\u8868'},
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
