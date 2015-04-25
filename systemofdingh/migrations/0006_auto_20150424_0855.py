# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systemofdingh', '0005_auto_20150424_0719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='orderID',
            field=models.CharField(max_length=10, serialize=False, verbose_name='\u91c7\u8d2d\u5355\u7f16\u53f7', primary_key=True),
        ),
    ]
