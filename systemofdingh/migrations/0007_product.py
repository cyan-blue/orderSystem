# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systemofdingh', '0006_auto_20150424_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('outer_id', models.CharField(unique=True, max_length=64, verbose_name='\u5916\u90e8\u7f16\u7801', blank=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u5546\u54c1\u540d\u79f0', blank=True)),
                ('barcode', models.CharField(db_index=True, max_length=64, verbose_name='\u6761\u7801', blank=True)),
                ('category', models.CharField(max_length=64, null=True, verbose_name='\u5185\u90e8\u5206\u7c7b', blank=True)),
                ('pic_path', models.CharField(max_length=256, verbose_name='\u5546\u54c1\u4e3b\u56fe', blank=True)),
                ('collect_num', models.IntegerField(default=0, verbose_name='\u5e93\u5b58\u6570')),
                ('warn_num', models.IntegerField(default=0, null=True, verbose_name='\u8b66\u544a\u6570')),
                ('remain_num', models.IntegerField(default=0, null=True, verbose_name='\u9884\u7559\u6570')),
                ('wait_post_num', models.IntegerField(default=0, null=True, verbose_name='\u5f85\u53d1\u6570')),
                ('sale_num', models.IntegerField(default=0, null=True, verbose_name='\u65e5\u51fa\u5e93\u6570')),
                ('reduce_num', models.IntegerField(default=0, null=True, verbose_name='\u9884\u51cf\u6570')),
                ('cost', models.FloatField(default=0, verbose_name='\u6210\u672c\u4ef7')),
                ('std_purchase_price', models.FloatField(default=0, verbose_name='\u6807\u51c6\u8fdb\u4ef7')),
                ('std_sale_price', models.FloatField(default=0, verbose_name='\u540a\u724c\u4ef7')),
                ('agent_price', models.FloatField(default=0, verbose_name='\u51fa\u552e\u4ef7')),
                ('staff_price', models.FloatField(default=0, verbose_name='\u5458\u5de5\u4ef7')),
                ('weight', models.CharField(max_length=10, verbose_name='\u91cd\u91cf(g)', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4', null=True)),
                ('sale_time', models.DateField(null=True, verbose_name='\u4e0a\u67b6\u65e5\u671f', blank=True)),
                ('is_split', models.BooleanField(default=False, verbose_name='\u9700\u62c6\u5206')),
                ('is_match', models.BooleanField(default=False, verbose_name='\u6709\u5339\u914d')),
                ('sync_stock', models.BooleanField(default=True, verbose_name='\u5e93\u5b58\u540c\u6b65')),
                ('is_assign', models.BooleanField(default=False, verbose_name='\u53d6\u6d88\u8b66\u544a')),
                ('post_check', models.BooleanField(default=False, verbose_name='\u9700\u626b\u63cf')),
                ('status', models.CharField(max_length=16, verbose_name='\u5546\u54c1\u72b6\u6001', db_index=True)),
                ('match_reason', models.CharField(max_length=80, verbose_name='\u5339\u914d\u539f\u56e0', blank=True)),
                ('buyer_prompt', models.CharField(max_length=60, verbose_name='\u5ba2\u6237\u63d0\u793a', blank=True)),
                ('memo', models.TextField(max_length=1000, verbose_name='\u5907\u6ce8', blank=True)),
                ('sale_charger', models.CharField(db_index=True, max_length=32, verbose_name='\u5f52\u5c5e\u91c7\u8d2d\u5458', blank=True)),
                ('storage_charger', models.CharField(db_index=True, max_length=32, verbose_name='\u5f52\u5c5e\u4ed3\u7ba1\u5458', blank=True)),
            ],
            options={
                'db_table': 'shop_items_product',
                'verbose_name': '\u5e93\u5b58\u5546\u54c1',
                'verbose_name_plural': '\u5e93\u5b58\u5546\u54c1\u5217\u8868',
                'permissions': [('change_product_skunum', '\u4fee\u6539\u5e93\u5b58\u4fe1\u606f')],
            },
        ),
    ]
