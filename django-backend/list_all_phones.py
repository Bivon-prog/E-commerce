#!/usr/bin/env python3

import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from products.astra_models import AstraProduct

def list_all_phones():
    """List all phone models in the database"""
    try:
        products = AstraProduct.get_all()
        
        print(f"Total products: {len(products)}")
        print("\nAll phone models:")
        print("=" * 50)
        
        for i, product in enumerate(products, 1):
            print(f"{i:2d}. {product['name']} ({product['brand']})")
            print(f"    Current images: {len(product.get('images', []))} images")
            if product.get('images'):
                for j, img in enumerate(product['images'][:2], 1):  # Show first 2 images
                    print(f"      {j}. {img}")
            print()
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_all_phones()