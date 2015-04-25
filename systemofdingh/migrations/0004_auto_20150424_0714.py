# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systemofdingh', '0003_auto_20150424_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetailmodel',
            name='orderID',
            field=models.ForeignKey(to='systemofdingh.orderModel'),
        ),
    ]
