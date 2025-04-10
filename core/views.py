from django.shortcuts import render
from rest_framework import generics
from .models import Buyer, Farmer, Driver
from .serializers import ( RegisterBuyerSerializer, RegisterDriverSerializer, 
                          RegisterFarmerSerializer, FarmerSerializer,
                          DriverSerializer,  BuyerSerializer,
)  


# Create your views here.
class RegisterBuyerView(generics.CreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = RegisterBuyerSerializer 

class RegisterFarmerView(generics.CreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = RegisterFarmerSerializer 

class RegisterDriverView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = RegisterDriverSerializer 

class FarmerListAPIView(generics.ListAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class DriverListAPIView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class BuyerListAPIView(generics.ListAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer 
