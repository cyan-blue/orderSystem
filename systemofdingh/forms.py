#coding:utf-8
__author__ = 'yann'


from django import forms
from django.forms import ModelForm
from django import forms
from systemofdingh.models import orderModel
from django.contrib.admin import widgets

class orderForm(forms.Form):
    orderID = forms.CharField(label="采购单编号", max_length=10)   #采购单编号
    orderTitle = forms.CharField(label="订单标题", max_length=100)        #订单标题
    consigneeName = forms.CharField(label="收货人名字", max_length=10) #收货人名字
    supplierId = forms.CharField(label="供应商id", max_length=10)  #供应商id
    storehouseId = forms.CharField(label="仓库id", max_length=10)  #仓库id
    purchaseType = forms.CharField(label="采购类型", max_length=10) #采购类型
    businessDate = forms.CharField(label="采购日期",widget=widgets.AdminDateWidget())      #采购日期
    remarks = forms.CharField(label="备注", max_length=100) #备注


class orderModelForm(ModelForm):
    class Meta:
       model= orderModel
       exclude = ('staffName', 'orderStatus',)


class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

class orderDetailForm(forms.Form):
    purchaseGoodID = forms.CharField(max_length=10, label=u"商品ID")   #商品ID
    purchaseGoodName = forms.CharField(max_length=10, label=u"产品名")  #产品名
    standardID = forms.CharField(max_length=10, label=u"规格ID")   #规格ID
    standardName = forms.CharField(max_length=10, label=u"规格名")  #规格名
    unitPrice = forms.IntegerField(label=u"进价") #进价
    quantityGoods = forms.IntegerField(label=u"数量")  #数量
    totalPrice = forms.IntegerField(label=u"总价") #总价