# products/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'sku', 'name', 'description', 'price', 'quantity', 'added_on']
        read_only_fields = ['added_on'] # This field should not be user-editable