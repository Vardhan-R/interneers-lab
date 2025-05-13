# serializers.py

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "price", "brand", "quality", "imported_date", "sold_date"]
