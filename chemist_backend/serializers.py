from rest_framework import serializers
from .models import Products, Categories, Sales, Expenses

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['id','name','category','instock','price']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields=['id','name']

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sales
        fields=['id','name','category','unit_price','quantity','total','date']

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sales
        fields=['id','name','category','unit_price','quantity','total']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expenses
        fields=['id','name','amount', 'date']

class CategoryTotalSerializer(serializers.Serializer):
    category = serializers.CharField()
    total_price = serializers.IntegerField()
