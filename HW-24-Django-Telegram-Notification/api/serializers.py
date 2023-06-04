from rest_framework import serializers

from products.models import Product, Category
from main.models import Order


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "title", "description", "price", "discount_price"]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ["id", "title", "slug", "products"]
        
class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'order-detail'}
        }
    