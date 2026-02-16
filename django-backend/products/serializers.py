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
    category = serializers.CharField(max_length=100, required=False, allow_blank=True, default='')
    price = serializers.IntegerField(min_value=0)
    description = serializers.CharField()
    specs = serializers.DictField(required=False, default=dict)
    images = serializers.ListField(
        child=serializers.URLField(),
        required=False,
        allow_empty=True
    )
    image_url = serializers.URLField(required=False)  # Backward compatibility
    in_stock = serializers.BooleanField(default=True)
    stock_quantity = serializers.IntegerField(default=0, min_value=0)
    
    def validate(self, data):
        """Ensure either images or image_url is provided, and filter empty strings"""
        # Filter out empty strings from images list
        if 'images' in data:
            data['images'] = [img for img in data['images'] if img and img.strip()]
        
        # Check if we have at least one image
        if not data.get('images') and not data.get('image_url'):
            raise serializers.ValidationError(
                "At least one valid image URL must be provided"
            )
        
        return data
