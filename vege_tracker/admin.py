from django.contrib import admin
from .models import Order, Vegetable, OrderItem 
# Register your models here.
admin.site.register(Order)
admin.site.register(Vegetable)
admin.site.register(OrderItem)