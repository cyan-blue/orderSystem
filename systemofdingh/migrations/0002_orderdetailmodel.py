# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systemofdingh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderDetailModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderID', models.CharField(max_length=10, verbose_name='\u91c7\u8d2d\u5355\u7f16\u53f7')),
                ('purchaseGoodID', models.CharField(max_length=10, verbose_name='\u5546\u54c1ID')),
                ('purchaseGoodName', models.CharField(max_length=10, verbose_name='\u4ea7\u54c1\u540d')),
                ('standardID', models.CharField(max_length=10, verbose_name='\u89c4\u683cID')),
                ('standardName', models.CharField(max_length=10, verbose_name='\u89c4\u683c\u540d')),
                ('unitPrice', models.DateField(max_length=10, verbose_name='\u8fdb\u4ef7')),
                ('quantityGoods', models.DateField(max_length=1000, verbose_name='\u6570\u91cf')),
                ('totalPrice', models.DateField(max_length=1000, verbose_name='\u603b\u4ef7')),
            ],
        ),
    ]
