# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200, verbose_name='\u4e8b\u9879\u5185\u5bb9')),
                ('is_done', models.BooleanField(default=False, verbose_name='\u4e8b\u9879\u72b6\u6001')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5f85\u529e\u4e8b\u9879',
                'verbose_name_plural': '\u5f85\u529e\u4e8b\u9879',
            },
        ),
    ]
