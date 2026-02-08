"""
Serializers for product data validation and transformation.
"""
from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    """Serializer for product responses"""
    _id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    brand = serializers.CharField()
    category = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    specs = serializers.DictField(required=False)
    images = serializers.ListField(
        child=serializers.URLField(),
        required=False
    )
    image_url = serializers.URLField(required=False)  # Backward compatibility
    in_stock = serializers.BooleanField(default=True)
    stock_quantity = serializers.IntegerField(default=0)


class CreateProductSerializer(serializers.Serializer):
    """Serializer for creating/updating products"""
    name = serializers.CharField(max_length=255)
    brand = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=100)
    price = serializers.IntegerField(min_value=0)
    description = serializers.CharField()
    specs = serializers.DictField(required=False, default=dict)
    images = serializers.ListField(
        child=serializers.URLField(),
        required=False,
        allow_empty=False
    )
    image_url = serializers.URLField(required=False)  # Backward compatibility
    in_stock = serializers.BooleanField(default=True)
    stock_quantity = serializers.IntegerField(default=0, min_value=0)
    
    def validate(self, data):
        """Ensure either images or image_url is provided"""
        if 'images' not in data and 'image_url' not in data:
            raise serializers.ValidationError(
                "Either 'images' (list) or 'image_url' (string) must be provided"
            )
        return data
