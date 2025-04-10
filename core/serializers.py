from rest_framework import serializers
from .models import User, Farmer, Driver, Buyer
from vege_tracker.models import Vegetable, Order, OrderItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'full_name']

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'full_name']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class RegisterBuyerSerializer(serializers.ModelSerializer):
    user = RegisterUserSerializer()

    class Meta:
        model = Buyer
        fields = ['user', 'company_name']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(role='buyer',**user_data)
        return Buyer.objects.create(user=user, **validated_data)
    
class RegisterFarmerSerializer(serializers.ModelSerializer):
    user = RegisterUserSerializer()

    class Meta:
        model = Farmer
        fields = ['user', 'farm_name']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(role='farmer', **user_data)
        return Farmer.objects.create(user=user, **validated_data)
    

class RegisterDriverSerializer(serializers.ModelSerializer):
    user = RegisterUserSerializer()

    class Meta:
        model = Driver
        fields = ['user', 'truck_plate_number']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(role='driver', **user_data)
        return Driver.objects.create(user=user, **validated_data)

class FarmerSerializer(serializers.ModelSerializer):
    #user = UserSerializer()

    class Meta:
        model = Farmer
        fields = ['id', 'farm_name']

class DriverSerializer(serializers.ModelSerializer):
    #user = UserSerializer()

    class Meta:
        model = Driver
        fields = ['id', 'truck_plate_number']

class BuyerSerializer(serializers.ModelSerializer):
    #user = UserSerializer()

    class Meta:
        model = Buyer
        fields = ['id', 'company_name']

class VegetableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vegetable 
        fields = ['id', 'name', 'unit_price']

class OrderItemSerializer(serializers.ModelSerializer):
    vegetable = VegetableSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'vegetable', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    buyer = BuyerSerializer()
    farmer = FarmerSerializer()
    driver = DriverSerializer(required=False, allow_null=True)
    vegetables = OrderItemSerializer(source='orderitem_set', many=True)

    class Meta:
        model = Order
        fields = ['id', 'buyer', 'farmer', 'driver', 'vegetables', 'status', 'order_date', 'delivery_date']