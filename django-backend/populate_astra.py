#!/usr/bin/env python
"""
Populate Astra database with sample products
"""
import os
import sys
import requests
import json

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
import django
django.setup()

def create_product(product_data):
    """Create a product via API"""
    try:
        response = requests.post(
            'http://localhost:8080/api/v1/products',
            json=product_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 201:
            result = response.json()
            print(f"✅ Created: {product_data['name']}")
            return True
        else:
            print(f"❌ Failed to create {product_data['name']}: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error creating {product_data['name']}: {e}")
        return False

def main():
    print("=" * 60)
    print("  POPULATING ASTRA DATABASE")
    print("=" * 60)
    
    # Sample products with multiple images
    products = [
        {
            "name": "iPhone 15 Pro",
            "brand": "Apple",
            "category": "Phone",
            "price": 14999900,  # KES in cents
            "description": "The most advanced iPhone ever with titanium design and A17 Pro chip.",
            "specs": {
                "screen_size": "6.1 inch Super Retina XDR",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "Up to 23 hours video playback",
                "camera": "48MP Main | Ultra Wide | Telephoto",
                "processor": "A17 Pro chip"
            },
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-naturaltitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-naturaltitanium_AV2?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-naturaltitanium_AV3?wid=400&hei=300&fmt=p-jpg&qlt=80"
            ],
            "in_stock": True,
            "stock_quantity": 25
        },
        {
            "name": "Samsung Galaxy S24 Ultra",
            "brand": "Samsung",
            "category": "Phone",
            "price": 13999900,
            "description": "The ultimate Galaxy experience with S Pen and AI features.",
            "specs": {
                "screen_size": "6.8 inch Dynamic AMOLED 2X",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "200MP Main | Ultra Wide | Telephoto",
                "processor": "Snapdragon 8 Gen 3"
            },
            "images": [
                "https://images.samsung.com/is/image/samsung/p6pim/in/2401/gallery/in-galaxy-s24-ultra-s928-sm-s928bztqins-thumb-539573828?$344_344_PNG$",
                "https://images.samsung.com/is/image/samsung/p6pim/in/2401/gallery/in-galaxy-s24-ultra-s928-sm-s928bztqins-thumb-539573829?$344_344_PNG$"
            ],
            "in_stock": True,
            "stock_quantity": 18
        },
        {
            "name": "Google Pixel 8 Pro",
            "brand": "Google",
            "category": "Phone",
            "price": 11999900,
            "description": "The most advanced Pixel phone with Google AI and the best Pixel Camera.",
            "specs": {
                "screen_size": "6.7 inch Super Actua display",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "5050 mAh",
                "camera": "50 MP Octa PD wide camera",
                "processor": "Google Tensor G3"
            },
            "images": [
                "https://lh3.googleusercontent.com/Nu3a6F80WfixUqf_ec_vgXy_c0-0r4VLJRXjVFF_X_Yk3ijzE5UHc8S53EQVQ8k0wHSjigZzNA=s0-e365-rw",
                "https://lh3.googleusercontent.com/Nu3a6F80WfixUqf_ec_vgXy_c0-0r4VLJRXjVFF_X_Yk3ijzE5UHc8S53EQVQ8k0wHSjigZzNA=s0-e365-rw"
            ],
            "in_stock": True,
            "stock_quantity": 12
        },
        {
            "name": "OnePlus 12",
            "brand": "OnePlus",
            "category": "Phone",
            "price": 8999900,
            "description": "Never Settle with flagship performance and fast charging.",
            "specs": {
                "screen_size": "6.82 inch LTPO AMOLED",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "5400 mAh",
                "camera": "50MP Triple Camera",
                "processor": "Snapdragon 8 Gen 3"
            },
            "images": [
                "https://oasis.opstatics.com/content/dam/oasis/page/2023/global/products/12/specs/green-img.png",
                "https://oasis.opstatics.com/content/dam/oasis/page/2023/global/products/12/specs/black-img.png"
            ],
            "in_stock": True,
            "stock_quantity": 15
        },
        {
            "name": "Xiaomi 14 Ultra",
            "brand": "Xiaomi",
            "category": "Phone",
            "price": 10999900,
            "description": "Photography flagship with Leica cameras and premium design.",
            "specs": {
                "screen_size": "6.73 inch LTPO AMOLED",
                "ram": "12GB",
                "storage": "512GB",
                "battery": "5300 mAh",
                "camera": "50MP Leica Quad Camera",
                "processor": "Snapdragon 8 Gen 3"
            },
            "images": [
                "https://i02.appmifile.com/mi-com-product/fly-birds/xiaomi-14-ultra/pc/black.png",
                "https://i02.appmifile.com/mi-com-product/fly-birds/xiaomi-14-ultra/pc/white.png"
            ],
            "in_stock": True,
            "stock_quantity": 8
        }
    ]
    
    # Create products
    success_count = 0
    for product in products:
        if create_product(product):
            success_count += 1
    
    print(f"\n✅ Successfully created {success_count}/{len(products)} products")
    
    # Test retrieval
    print("\n📋 Testing product retrieval...")
    try:
        response = requests.get('http://localhost:8080/api/v1/products')
        if response.status_code == 200:
            products = response.json()
            print(f"✅ Retrieved {len(products)} products from Astra")
            for product in products:
                print(f"   - {product['name']} ({len(product.get('images', []))} images)")
        else:
            print(f"❌ Failed to retrieve products: {response.text}")
    except Exception as e:
        print(f"❌ Error retrieving products: {e}")

if __name__ == '__main__':
    main()