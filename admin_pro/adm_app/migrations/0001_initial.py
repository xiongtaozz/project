# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
                'verbose_name_plural': '\u5b66\u751f\u8868',
            },
        ),
        migrations.CreateModel(
            name='Techer',
            fields=[
                ('t_no', models.IntegerField(serialize=False, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88\xe7\xbc\x96\xe5\x8f\xb7', primary_key=True)),
                ('t_name', models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('t_email', models.EmailField(unique=True, max_length=254, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88\xe9\x82\xae\xe7\xae\xb1')),
                ('t_sh', models.CharField(default=b'FR', max_length=30, verbose_name=b'\xe5\xad\xa6\xe6\xa0\xa1', choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior')])),
                ('t_frist_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x85\xa5\xe8\x81\x8c\xe6\x97\xb6\xe9\x97\xb4')),
                ('t_bariy_date', models.DateField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5')),
                ('t_remark', models.TextField(max_length=200, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('t_photo', models.ImageField(default=b'/techer/default.jpg', upload_to=b'techer/%Y/%m', verbose_name=b'\xe6\x95\x99\xe5\xb8\x88\xe5\x9b\xbe\xe7\x89\x87')),
                ('t_url', models.URLField(default=b'http://www.maiziedu.com', verbose_name=b'\xe6\x95\x99\xe5\xb8\x88\xe4\xb8\xbb\xe9\xa1\xb5')),
            ],
            options={
                'ordering': ['-t_no'],
                'db_table': 'techer',
                'verbose_name': '\u6559\u5e08\u8868',
                'verbose_name_plural': '\u6559\u5e08\u8868',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='techer',
            field=models.ForeignKey(verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe6\x95\x99\xe5\xb8\x88ID', to='adm_app.Techer'),
        ),
    ]
