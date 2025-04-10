from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny 
from .models import Vegetable, Order, OrderItem
from core.models import Buyer, Farmer, Driver
from .permissions import IsBuyer, IsFarmer, IsDriver  
from core.serializers import (
    VegetableSerializer, OrderSerializer, OrderItemSerializer,
    BuyerSerializer, FarmerSerializer, DriverSerializer
)

# Create your views here.


class VegetableViewSet(viewsets.ModelViewSet):
    queryset = Vegetable.objects.all()
    serializer_class = VegetableSerializer
    permission_classes = [AllowAny] 

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [AllowAny]

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [AllowAny]

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [AllowAny] 

