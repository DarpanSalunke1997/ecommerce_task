from django.contrib import admin
from shop.models import Product, Discount, Order, OrderItem
# Register your models here.

admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Order)
admin.site.register(OrderItem)