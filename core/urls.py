from django.urls import path
from .views import RegisterBuyerView, RegisterFarmerView, RegisterDriverView, BuyerListAPIView, FarmerListAPIView, DriverListAPIView

urlpatterns = [
    path('register/buyer/', RegisterBuyerView.as_view(), name='register-buyer'),
    path('register/farmer/', RegisterFarmerView.as_view(), name='register-farmer'),
    path('register/driver/', RegisterDriverView.as_view(), name='register-driver'),
    path('list/buyer/', BuyerListAPIView.as_view(), name='list-buyer'),
    path('list/farmer/', FarmerListAPIView.as_view(), name='list-farmer'),
    path('list/driver/', DriverListAPIView.as_view(), name='list-driver'),
]