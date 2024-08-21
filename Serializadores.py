# backend/app/serializers.py
from rest_framework import serializers
from .models import Product, Sale, User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProductSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity_in_stock', 'owner']

class SaleSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True)
    product = ProductSerializer()

    class Meta:
        model = Sale
        fields = ['id', 'product', 'quantity', 'sale_date', 'total_price', 'seller']

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product = Product.objects.get(id=product_data['id'])
        sale = Sale.objects.create(product=product, **validated_data)
        return sale
