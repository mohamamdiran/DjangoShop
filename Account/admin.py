from django.contrib import admin
from .models import Order, Cart



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id','User','IsPaid','DateOfPay','get_order_price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','CartOrder','Product','Price','Count','get_products_price')
