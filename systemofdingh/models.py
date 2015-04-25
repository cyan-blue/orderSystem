#coding:utf-8
__author__ = 'yann'

from django.db import models
import  datetime, json

class orderModel(models.Model):
    staffName = models.CharField(max_length=10, verbose_name=u"买手")              #输入订单的人
    orderID = models.CharField(primary_key=True, max_length=10, verbose_name=u"采购单编号")   #采购单编号
    orderTitle = models.CharField(max_length=100, verbose_name=u"订单标题")        #订单标题
    consigneeName = models.CharField(max_length=10, verbose_name=u"收货人名字") #收货人名字
    supplierId = models.CharField(max_length=10, verbose_name=u"供应商id")  #供应商id
    storehouseId = models.CharField(max_length=10, verbose_name=u"仓库id")  #仓库id
    purchaseType = models.CharField(max_length=10, verbose_name=u"采购类型") #采购类型
    businessDate = models.DateField(blank=True, verbose_name=u"采购日期")      #采购日期
    remarks = models.CharField(max_length=100, verbose_name=u"备注") #备注
    orderStatus = models.CharField(max_length=10, verbose_name=u"订单状态")   #订单状态
    # goodsID = models.CharField(max_length=100, verbose_name=u"商品ID")       #商品名字
    # unitPrice = models.IntegerField(default=0, verbose_name=u"单价")           #单价
    # quantityOfItem = models.IntegerField(default=10, verbose_name=u"数量")     #数量
    # totalAmount = models.IntegerField(verbose_name=u"总价")                  #总价
    def __unicode__(self):
        return self.orderTitle

class User(models.Model):
    username = models.CharField(max_length=10, verbose_name=u"用户名")
    password = models.CharField(max_length=20,  verbose_name=u"密码")
    def __unicode__(self):
        return self.username

class orderDetailModel(models.Model):
    orderID = models.ForeignKey(orderModel, verbose_name="采购单编号")   #采购单编号
    purchaseGoodID = models.CharField(max_length=10, verbose_name=u"商品ID")   #商品ID
    purchaseGoodName = models.CharField(max_length=10, verbose_name=u"产品名")  #产品名
    standardID = models.CharField(max_length=10, verbose_name=u"规格ID")   #规格ID
    standardName = models.CharField(max_length=10, verbose_name=u"规格名")  #规格名
    unitPrice = models.IntegerField(verbose_name=u"进价") #进价
    quantityGoods = models.IntegerField(verbose_name=u"数量")  #数量
    totalPrice = models.IntegerField(verbose_name=u"总价") #总价
    def __unicode__(self):
        return self.purchaseGoodName


class ProductDefectException(Exception):
    pass

class Product(models.Model):
    """ 系统商品（根据淘宝外部编码) """
    outer_id     = models.CharField(max_length=64, unique=True,null=False,
                                    blank=True, verbose_name=u'外部编码')
    name         = models.CharField(max_length=64, blank=True,verbose_name=u'商品名称')

    barcode      = models.CharField(max_length=64, blank=True,db_index=True,verbose_name=u'条码')
    category     = models.CharField(max_length=64,null=True,blank=True, verbose_name=u'内部分类')
    pic_path     = models.CharField(max_length=256,blank=True,verbose_name=u'商品主图')

    collect_num  = models.IntegerField(default=0,verbose_name=u'库存数')  #库存数
    warn_num     = models.IntegerField(null=True,default=0,verbose_name=u'警告数')  #警戒库位
    remain_num   = models.IntegerField(null=True,default=0,verbose_name=u'预留数')  #预留库存
    wait_post_num   = models.IntegerField(null=True,default=0,verbose_name=u'待发数')  #待发数
    sale_num  = models.IntegerField(null=True,default=0,verbose_name=u'日出库数')  #日出库
    reduce_num   = models.IntegerField(null=True,default=0,verbose_name=u'预减数')  #下次入库减掉这部分库存

    cost         = models.FloatField(default=0,verbose_name=u'成本价')
    std_purchase_price = models.FloatField(default=0,verbose_name=u'标准进价')
    std_sale_price     = models.FloatField(default=0,verbose_name=u'吊牌价')
    agent_price        = models.FloatField(default=0,verbose_name=u'出售价')
    staff_price        = models.FloatField(default=0,verbose_name=u'员工价')

    weight       = models.CharField(max_length=10,blank=True,verbose_name=u'重量(g)')

    created      = models.DateTimeField(null=True,blank=True,
                                        auto_now_add=True,verbose_name=u'创建时间')
    modified     = models.DateTimeField(null=True,blank=True,
                                        auto_now=True,verbose_name=u'修改时间')
    sale_time    = models.DateField(null=True,blank=True,verbose_name=u'上架日期')

    is_split   = models.BooleanField(default=False,verbose_name=u'需拆分')
    is_match   = models.BooleanField(default=False,verbose_name=u'有匹配')

    sync_stock   = models.BooleanField(default=True,verbose_name=u'库存同步')
    is_assign    = models.BooleanField(default=False,verbose_name=u'取消警告')

    post_check   = models.BooleanField(default=False,verbose_name=u'需扫描')
    status       = models.CharField(max_length=16,db_index=True,
                                    verbose_name=u'商品状态')

    match_reason = models.CharField(max_length=80,blank=True,verbose_name=u'匹配原因')
    buyer_prompt = models.CharField(max_length=60,blank=True,verbose_name=u'客户提示')
    memo         = models.TextField(max_length=1000,blank=True,verbose_name=u'备注')

    sale_charger = models.CharField(max_length=32,db_index=True,blank=True,verbose_name=u'归属采购员')
    storage_charger = models.CharField(max_length=32,db_index=True,blank=True,verbose_name=u'归属仓管员')

    class Meta:
        db_table = 'shop_items_product'
        verbose_name = u'库存商品'
        verbose_name_plural = u'库存商品列表'
        permissions = [("change_product_skunum", u"修改库存信息"),]

    def __unicode__(self):
        return '<%s,%s>'%(self.outer_id, self.name)

    def clean(self):
        for field in self._meta.fields:
            if isinstance(field, (models.CharField, models.TextField)):
                setattr(self, field.name, getattr(self, field.name).strip())

    @property
    def json(self):

        skus_json = []
        for sku in self.pskus:
            skus_json.append(sku.json)

        return {
                'id':self.id,
                'outer_id':self.outer_id,
                'name':self.name,
                'category':self.category or {},
                'collect_num':self.collect_num,
                'remain_num':self.remain_num,
                'warn_num':self.warn_num,
                'wait_post_num':self.wait_post_num,
                'cost':self.cost,
                'std_purchase_price':self.std_purchase_price,
                'std_sale_price':self.std_sale_price,
                'agent_price':self.agent_price,
                'staff_price':self.staff_price,
                'weight':self.weight,
                'sync_stock':self.sync_stock,
                'is_split':self.is_split,
                'is_match':self.is_match,
                'is_assign':self.is_assign,
                'is_stock_warn':self.is_stock_warn,
                'is_warning':self.is_warning,
                'post_check':self.post_check,
                'status':self.status,
                'buyer_prompt':self.buyer_prompt,
                'memo':self.memo,
                'districts':self.get_district_list(),
                'barcode':self.BARCODE,
                'match_reason':self.match_reason,
                'skus':skus_json
                }
