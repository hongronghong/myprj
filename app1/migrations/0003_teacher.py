# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_student_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u540d\u5b57')),
                ('number', models.IntegerField(verbose_name='\u7f16\u53f7')),
                ('sex', models.BooleanField(verbose_name='\u6027\u522b')),
            ],
        ),
    ]
