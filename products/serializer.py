from rest_framework import serializers
from products.models import Product, User, Category, Type


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    type_name = serializers.CharField(source='type.name', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'type', 'type_name', 'is_active',
                  'created_at', 'updated_at', 'image')
        read_only_fields = ('id', 'created_at', 'updated_at')
