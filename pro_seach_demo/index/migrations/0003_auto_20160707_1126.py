# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20160707_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileurl',
            name='url',
            field=models.FileField(upload_to=b'xls'),
        ),
    ]
