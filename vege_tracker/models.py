from django.db import models
from core.models import Buyer, Farmer, Driver 

# Create your models here.
class Vegetable(models.Model):
    name = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    vegetables = models.ManyToManyField(Vegetable, through='OrderItem')
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in_transit', 'In_Transit'),
        ('delivered', 'Delivered')
    ])
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    vegetable = models.ForeignKey(Vegetable, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
