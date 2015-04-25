# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orderModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('staffName', models.CharField(max_length=10, verbose_name='\u4e70\u624b')),
                ('orderID', models.CharField(max_length=10, verbose_name='\u91c7\u8d2d\u5355\u7f16\u53f7')),
                ('orderTitle', models.CharField(max_length=100, verbose_name='\u8ba2\u5355\u6807\u9898')),
                ('consigneeName', models.CharField(max_length=10, verbose_name='\u6536\u8d27\u4eba\u540d\u5b57')),
                ('supplierId', models.CharField(max_length=10, verbose_name='\u4f9b\u5e94\u5546id')),
                ('storehouseId', models.CharField(max_length=10, verbose_name='\u4ed3\u5e93id')),
                ('purchaseType', models.CharField(max_length=10, verbose_name='\u91c7\u8d2d\u7c7b\u578b')),
                ('businessDate', models.DateField(verbose_name='\u91c7\u8d2d\u65e5\u671f', blank=True)),
                ('remarks', models.CharField(max_length=100, verbose_name='\u5907\u6ce8')),
                ('orderStatus', models.CharField(max_length=10, verbose_name='\u8ba2\u5355\u72b6\u6001')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=10, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=20, verbose_name='\u5bc6\u7801')),
            ],
        ),
    ]
