from django.contrib import admin
from .models import Farmer, Buyer, Driver 
# Register your models here.
#admin.site.register(UserManager)
admin.site.register(Farmer)
admin.site.register(Buyer)
admin.site.register(Driver)
# admin.site.register(Vegetable)
# admin.site.register(Order)
# admin.site.register(OrderItem)