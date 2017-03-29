# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='techer',
            options={'ordering': ['-t_no'], 'verbose_name': '\u6559\u5e08\u8868', 'verbose_name_plural': 'techers'},
        ),
        migrations.AlterField(
            model_name='techer',
            name='t_bariy_date',
            field=models.DateField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5'),
        ),
        migrations.AlterModelTable(
            name='techer',
            table='',
        ),
    ]
