# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0002_auto_20160419_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stu_name', models.CharField(max_length=20, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'db_table': 'student',
                'verbose_name': '\u5b66\u751f\u8868',
                'verbose_name_plural': 'stus',
            },
        ),
        migrations.AlterModelTable(
            name='techer',
            table='techer',
        ),
        migrations.AddField(
            model_name='student',
            name='techer',
            field=models.ForeignKey(verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe6\x95\x99\xe5\xb8\x88ID', to='orm_app.Techer'),
        ),
    ]
