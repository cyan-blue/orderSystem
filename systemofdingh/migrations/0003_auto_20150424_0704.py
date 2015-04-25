# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systemofdingh', '0002_orderdetailmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetailmodel',
            name='quantityGoods',
            field=models.IntegerField(verbose_name='\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='orderdetailmodel',
            name='totalPrice',
            field=models.IntegerField(verbose_name='\u603b\u4ef7'),
        ),
        migrations.AlterField(
            model_name='orderdetailmodel',
            name='unitPrice',
            field=models.IntegerField(verbose_name='\u8fdb\u4ef7'),
        ),
    ]
