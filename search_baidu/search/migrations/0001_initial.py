# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_value', models.CharField(max_length=30, verbose_name=b'\xe8\xaf\x8d\xe8\xaf\xad\xe5\x86\x85\xe5\xae\xb9')),
            ],
            options={
                'verbose_name': '\u8bcd\u8bed',
                'verbose_name_plural': '\u8bcd\u8bed',
            },
            bases=(models.Model,),
        ),
    ]
