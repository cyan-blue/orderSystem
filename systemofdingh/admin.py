from django.contrib import admin
from systemofdingh.models import orderModel, User, orderDetailModel, Product
# Register your models here.

admin.site.register(orderModel)
admin.site.register(User)
admin.site.register(orderDetailModel)
admin.site.register(Product)
