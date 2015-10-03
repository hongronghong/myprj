# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.BooleanField(default=True, verbose_name='\u6027\u522b'),
            preserve_default=False,
        ),
    ]
