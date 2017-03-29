# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-04 04:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_month_des'),
        ('crm', '0004_auto_20160702_0619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budgetmx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=20, verbose_name='\u5355\u636e\u53f7')),
                ('line', models.IntegerField(verbose_name='\u884c\u53f7')),
                ('amt', models.DecimalField(decimal_places=2, max_digits=125, verbose_name='\u91d1\u989d')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Depts', verbose_name='\u9884\u7b97\u90e8\u95e8')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Subject', verbose_name='\u9884\u7b97\u79d1\u76ee')),
            ],
            options={
                'verbose_name': '\u9884\u7b97\u660e\u7ec6',
            },
        ),
        migrations.RemoveField(
            model_name='budgetd',
            name='budget_ptr',
        ),
        migrations.RemoveField(
            model_name='budgetd',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='budgetd',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Budgetd',
        ),
    ]
