# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systemofdingh', '0004_auto_20150424_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetailmodel',
            name='orderID',
            field=models.ForeignKey(verbose_name=b'\xe9\x87\x87\xe8\xb4\xad\xe5\x8d\x95\xe7\xbc\x96\xe5\x8f\xb7', to='systemofdingh.orderModel'),
        ),
    ]
