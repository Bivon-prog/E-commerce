#!/usr/bin/env python
"""
Create a comprehensive categorized phone catalog
"""
import os
import sys
import requests
import json
import time

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
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        
        if response.status_code == 201:
            result = response.json()
            print(f"✅ Created: {product_data['name']} ({product_data['price_category']})")
            return True
        else:
            print(f"❌ Failed to create {product_data['name']}: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error creating {product_data['name']}: {e}")
        return False

def clear_existing_products():
    """Clear existing products"""
    try:
        response = requests.get('http://localhost:8080/api/v1/products')
        if response.status_code == 200:
            products = response.json()
            print(f"🗑️  Clearing {len(products)} existing products...")
            
            for product in products:
                delete_response = requests.delete(f"http://localhost:8080/api/v1/products/{product['_id']}")
                if delete_response.status_code == 204:
                    print(f"   ✅ Deleted: {product['name']}")
                else:
                    print(f"   ❌ Failed to delete: {product['name']}")
            
            print("✅ All existing products cleared\n")
        else:
            print("❌ Failed to get existing products")
    except Exception as e:
        print(f"❌ Error clearing products: {e}")

def main():
    print("=" * 80)
    print("  CREATING COMPREHENSIVE CATEGORIZED PHONE CATALOG")
    print("=" * 80)
    
    # Clear existing products first
    clear_existing_products()
    
    # Comprehensive categorized phone catalog
    products = [
        # FLAGSHIP PHONES (Above KES 120,000)
        {
            "name": "iPhone 15 Pro Max",
            "brand": "Apple",
            "category": "Phone",
            "price_category": "Flagship",
            "performance_tier": "Premium",
            "brand_series": "iPhone Pro Max",
            "target_audience": "Professionals",
            "price": 16999900,
            "description": "The ultimate iPhone with titanium design, A17 Pro chip, and advanced camera system.",
            "specs": {
                "screen_size": "6.7 inch Super Retina XDR",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "Up to 29 hours video playback",
                "camera": "48MP Main | Ultra Wide | Telephoto",
                "processor": "A17 Pro chip",
                "price_category": "Flagship",
                "performance_tier": "Premium",
                "brand_series": "iPhone Pro Max",
                "target_audience": "Professionals"
            },
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-naturaltitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-bluetitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-blacktitanium?wid=400&hei=300&fmt=p-jpg&qlt=80"
            ],
            "in_stock": True,
            "stock_quantity": 15
        },
        {
            "name": "iPhone 15 Pro",
            "brand": "Apple",
            "category": "Phone",
            "price_category": "Flagship",
            "performance_tier": "Premium",
            "brand_series": "iPhone Pro",
            "target_audience": "Professionals",
            "price": 14999900,
            "description": "Pro performance with titanium design and A17 Pro chip.",
            "specs": {
                "screen_size": "6.1 inch Super Retina XDR",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "Up to 23 hours video playback",
                "camera": "48MP Main | Ultra Wide | Telephoto",
                "processor": "A17 Pro chip",
                "price_category": "Flagship",
                "performance_tier": "Premium",
                "brand_series": "iPhone Pro",
                "target_audience": "Professionals"
            },
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-naturaltitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-bluetitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-blacktitanium?wid=400&hei=300&fmt=p-jpg&qlt=80"
            ],
            "in_stock": True,
            "stock_quantity": 20
        },
        {
            "name": "Galaxy S24 Ultra",
            "brand": "Samsung",
            "category": "Phone",
            "price_category": "Flagship",
            "performance_tier": "Premium",
            "brand_series": "Galaxy S Ultra",
            "target_audience": "Professionals",
            "price": 13999900,
            "description": "The ultimate Galaxy with S Pen, AI features, and 200MP camera.",
            "specs": {
                "screen_size": "6.8 inch Dynamic AMOLED 2X",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "200MP Main | Ultra Wide | Telephoto",
                "processor": "Snapdragon 8 Gen 3",
                "price_category": "Flagship",
                "performance_tier": "Premium",
                "brand_series": "Galaxy S Ultra",
                "target_audience": "Professionals"
            },
            "images": [
                "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1580910051074-3eb694886505?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 12
        },
        {
            "name": "iPhone 14 Pro",
            "brand": "Apple",
            "category": "Phone",
            "price_category": "Flagship",
            "performance_tier": "Premium",
            "brand_series": "iPhone Pro",
            "target_audience": "Professionals",
            "price": 12999900,
            "description": "iPhone 14 Pro with Dynamic Island and A16 Bionic chip.",
            "specs": {
                "screen_size": "6.1 inch Super Retina XDR",
                "ram": "6GB",
                "storage": "256GB",
                "battery": "Up to 23 hours video playback",
                "camera": "48MP Main | Ultra Wide | Telephoto",
                "processor": "A16 Bionic chip",
                "price_category": "Flagship",
                "performance_tier": "Premium",
                "brand_series": "iPhone Pro",
                "target_audience": "Professionals"
            },
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-naturaltitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-bluetitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-blacktitanium?wid=400&hei=300&fmt=p-jpg&qlt=80"
            ],
            "in_stock": True,
            "stock_quantity": 10
        },

        # MID-RANGE PHONES (KES 50,000 - 120,000)
        {
            "name": "iPhone 15",
            "brand": "Apple",
            "category": "Phone",
            "price_category": "Mid-range",
            "performance_tier": "High-end",
            "brand_series": "iPhone",
            "target_audience": "General",
            "price": 11999900,
            "description": "The iPhone 15 with Dynamic Island and advanced dual-camera system.",
            "specs": {
                "screen_size": "6.1 inch Super Retina XDR",
                "ram": "6GB",
                "storage": "128GB",
                "battery": "Up to 20 hours video playback",
                "camera": "48MP Main | Ultra Wide",
                "processor": "A16 Bionic chip",
                "price_category": "Mid-range",
                "performance_tier": "High-end",
                "brand_series": "iPhone",
                "target_audience": "General"
            },
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-naturaltitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-bluetitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-blacktitanium?wid=400&hei=300&fmt=p-jpg&qlt=80"
            ],
            "in_stock": True,
            "stock_quantity": 25
        },
        {
            "name": "Pixel 8 Pro",
            "brand": "Google",
            "category": "Phone",
            "price_category": "Mid-range",
            "performance_tier": "Premium",
            "brand_series": "Pixel Pro",
            "target_audience": "Photography",
            "price": 11999900,
            "description": "The most advanced Pixel with Google AI and the best Pixel Camera.",
            "specs": {
                "screen_size": "6.7 inch Super Actua display",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "5050 mAh",
                "camera": "50MP Main | Ultra Wide | Telephoto",
                "processor": "Google Tensor G3",
                "price_category": "Mid-range",
                "performance_tier": "Premium",
                "brand_series": "Pixel Pro",
                "target_audience": "Photography"
            },
            "images": [
                "https://images.unsplash.com/photo-1598300042247-d088f8ab3a91?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1605236453806-6ff36851218e?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1616348436168-de43ad0db179?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 15
        },
        {
            "name": "Galaxy S24",
            "brand": "Samsung",
            "category": "Phone",
            "price_category": "Mid-range",
            "performance_tier": "High-end",
            "brand_series": "Galaxy S",
            "target_audience": "General",
            "price": 9999900,
            "description": "Galaxy S24 with AI-powered features and premium design.",
            "specs": {
                "screen_size": "6.2 inch Dynamic AMOLED 2X",
                "ram": "8GB",
                "storage": "128GB",
                "battery": "4000 mAh",
                "camera": "50MP Main | Ultra Wide | Telephoto",
                "processor": "Snapdragon 8 Gen 3",
                "price_category": "Mid-range",
                "performance_tier": "High-end",
                "brand_series": "Galaxy S",
                "target_audience": "General"
            },
            "images": [
                "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1556656793-08538906a9f8?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1574944985070-8f3ebc6b79d2?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 20
        },
        {
            "name": "OnePlus 12",
            "brand": "OnePlus",
            "category": "Phone",
            "price_category": "Mid-range",
            "performance_tier": "Premium",
            "brand_series": "OnePlus",
            "target_audience": "Performance",
            "price": 8999900,
            "description": "Never Settle with flagship performance and fast charging.",
            "specs": {
                "screen_size": "6.82 inch LTPO AMOLED",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "5400 mAh",
                "camera": "50MP Hasselblad Triple Camera",
                "processor": "Snapdragon 8 Gen 3",
                "price_category": "Mid-range",
                "performance_tier": "Premium",
                "brand_series": "OnePlus",
                "target_audience": "Performance"
            },
            "images": [
                "https://images.unsplash.com/photo-1598300042247-d088f8ab3a91?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1605236453806-6ff36851218e?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1616348436168-de43ad0db179?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 18
        },
        {
            "name": "iPhone 13",
            "brand": "Apple",
            "category": "Phone",
            "price_category": "Mid-range",
            "performance_tier": "High-end",
            "brand_series": "iPhone",
            "target_audience": "General",
            "price": 8999900,
            "description": "iPhone 13 with A15 Bionic chip and advanced dual-camera system.",
            "specs": {
                "screen_size": "6.1 inch Super Retina XDR",
                "ram": "4GB",
                "storage": "128GB",
                "battery": "Up to 19 hours video playback",
                "camera": "12MP Main | Ultra Wide",
                "processor": "A15 Bionic chip",
                "price_category": "Mid-range",
                "performance_tier": "High-end",
                "brand_series": "iPhone",
                "target_audience": "General"
            },
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-naturaltitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-bluetitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-blacktitanium?wid=400&hei=300&fmt=p-jpg&qlt=80"
            ],
            "in_stock": True,
            "stock_quantity": 22
        },
        {
            "name": "Realme GT 5 Pro",
            "brand": "Realme",
            "category": "Phone",
            "price_category": "Mid-range",
            "performance_tier": "Premium",
            "brand_series": "Realme GT",
            "target_audience": "Gamers",
            "price": 7999900,
            "description": "Gaming flagship with powerful performance and fast charging.",
            "specs": {
                "screen_size": "6.78 inch LTPO AMOLED",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "5400 mAh",
                "camera": "50MP Triple Camera",
                "processor": "Snapdragon 8 Gen 3",
                "price_category": "Mid-range",
                "performance_tier": "Premium",
                "brand_series": "Realme GT",
                "target_audience": "Gamers"
            },
            "images": [
                "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1556656793-08538906a9f8?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1574944985070-8f3ebc6b79d2?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 15
        },
        {
            "name": "Pixel 7a",
            "brand": "Google",
            "category": "Phone",
            "price_category": "Mid-range",
            "performance_tier": "Mid-tier",
            "brand_series": "Pixel A",
            "target_audience": "Photography",
            "price": 5999900,
            "description": "Pixel 7a with flagship camera features at an affordable price.",
            "specs": {
                "screen_size": "6.1 inch OLED",
                "ram": "8GB",
                "storage": "128GB",
                "battery": "4385 mAh",
                "camera": "64MP Main | Ultra Wide",
                "processor": "Google Tensor G2",
                "price_category": "Mid-range",
                "performance_tier": "Mid-tier",
                "brand_series": "Pixel A",
                "target_audience": "Photography"
            },
            "images": [
                "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1580910051074-3eb694886505?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 25
        },

        # BUDGET PHONES (Under KES 50,000)
        {
            "name": "OnePlus Nord 3",
            "brand": "OnePlus",
            "category": "Phone",
            "price_category": "Budget",
            "performance_tier": "Performance",
            "brand_series": "OnePlus Nord",
            "target_audience": "Students",
            "price": 4999900,
            "description": "Premium mid-range experience with flagship features.",
            "specs": {
                "screen_size": "6.74 inch AMOLED",
                "ram": "8GB",
                "storage": "128GB",
                "battery": "5000 mAh",
                "camera": "50MP Triple Camera",
                "processor": "MediaTek Dimensity 9000",
                "price_category": "Budget",
                "performance_tier": "Performance",
                "brand_series": "OnePlus Nord",
                "target_audience": "Students"
            },
            "images": [
                "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1580910051074-3eb694886505?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 30
        },
        {
            "name": "Galaxy A55",
            "brand": "Samsung",
            "category": "Phone",
            "price_category": "Budget",
            "performance_tier": "Mid-tier",
            "brand_series": "Galaxy A",
            "target_audience": "Students",
            "price": 4999900,
            "description": "Mid-range Galaxy with premium features and great value.",
            "specs": {
                "screen_size": "6.6 inch Super AMOLED",
                "ram": "8GB",
                "storage": "128GB",
                "battery": "5000 mAh",
                "camera": "50MP Main | Ultra Wide | Macro",
                "processor": "Exynos 1480",
                "price_category": "Budget",
                "performance_tier": "Mid-tier",
                "brand_series": "Galaxy A",
                "target_audience": "Students"
            },
            "images": [
                "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1601784551446-20c9e07cdbdb?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 35
        },
        {
            "name": "Redmi Note 13 Pro",
            "brand": "Xiaomi",
            "category": "Phone",
            "price_category": "Budget",
            "performance_tier": "Performance",
            "brand_series": "Redmi Note",
            "target_audience": "Students",
            "price": 3999900,
            "description": "Premium mid-range phone with excellent camera and performance.",
            "specs": {
                "screen_size": "6.67 inch AMOLED",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "5100 mAh",
                "camera": "200MP Main | Ultra Wide | Macro",
                "processor": "Snapdragon 7s Gen 2",
                "price_category": "Budget",
                "performance_tier": "Performance",
                "brand_series": "Redmi Note",
                "target_audience": "Students"
            },
            "images": [
                "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1601784551446-20c9e07cdbdb?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 40
        },
        {
            "name": "Tecno Camon 30 Pro",
            "brand": "Tecno",
            "category": "Phone",
            "price_category": "Budget",
            "performance_tier": "Performance",
            "brand_series": "Tecno Camon",
            "target_audience": "Photography",
            "price": 3999900,
            "description": "Camera-focused smartphone with AI photography features.",
            "specs": {
                "screen_size": "6.78 inch AMOLED",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "50MP Triple Camera",
                "processor": "MediaTek Dimensity 8050",
                "price_category": "Budget",
                "performance_tier": "Performance",
                "brand_series": "Tecno Camon",
                "target_audience": "Photography"
            },
            "images": [
                "https://images.unsplash.com/photo-1598300042247-d088f8ab3a91?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1605236453806-6ff36851218e?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1616348436168-de43ad0db179?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 25
        },
        {
            "name": "Infinix Note 40 Pro",
            "brand": "Infinix",
            "category": "Phone",
            "price_category": "Budget",
            "performance_tier": "Performance",
            "brand_series": "Infinix Note",
            "target_audience": "Students",
            "price": 3499900,
            "description": "Performance-focused smartphone with fast charging and good cameras.",
            "specs": {
                "screen_size": "6.78 inch AMOLED",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "108MP Triple Camera",
                "processor": "MediaTek Dimensity 7020",
                "price_category": "Budget",
                "performance_tier": "Performance",
                "brand_series": "Infinix Note",
                "target_audience": "Students"
            },
            "images": [
                "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1556656793-08538906a9f8?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1574944985070-8f3ebc6b79d2?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 30
        },
        {
            "name": "Vivo Y36",
            "brand": "Vivo",
            "category": "Phone",
            "price_category": "Budget",
            "performance_tier": "Entry",
            "brand_series": "Vivo Y",
            "target_audience": "Students",
            "price": 2999900,
            "description": "Budget-friendly smartphone with good camera and battery life.",
            "specs": {
                "screen_size": "6.64 inch IPS LCD",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "50MP Dual Camera",
                "processor": "Snapdragon 680",
                "price_category": "Budget",
                "performance_tier": "Entry",
                "brand_series": "Vivo Y",
                "target_audience": "Students"
            },
            "images": [
                "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1580910051074-3eb694886505?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 35
        },
        {
            "name": "Realme C67",
            "brand": "Realme",
            "category": "Phone",
            "price_category": "Budget",
            "performance_tier": "Entry",
            "brand_series": "Realme C",
            "target_audience": "Students",
            "price": 1999900,
            "description": "Budget smartphone with good performance and long battery life.",
            "specs": {
                "screen_size": "6.72 inch IPS LCD",
                "ram": "6GB",
                "storage": "128GB",
                "battery": "5000 mAh",
                "camera": "108MP Dual Camera",
                "processor": "Snapdragon 685",
                "price_category": "Budget",
                "performance_tier": "Entry",
                "brand_series": "Realme C",
                "target_audience": "Students"
            },
            "images": [
                "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1601784551446-20c9e07cdbdb?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 50
        },
        {
            "name": "Infinix Hot 40i",
            "brand": "Infinix",
            "category": "Phone",
            "price_category": "Budget",
            "performance_tier": "Entry",
            "brand_series": "Infinix Hot",
            "target_audience": "Students",
            "price": 1799900,
            "description": "Budget-friendly smartphone with good battery life and performance.",
            "specs": {
                "screen_size": "6.7 inch IPS LCD",
                "ram": "4GB",
                "storage": "128GB",
                "battery": "5000 mAh",
                "camera": "32MP Dual Camera",
                "processor": "UNISOC Tiger T606",
                "price_category": "Budget",
                "performance_tier": "Entry",
                "brand_series": "Infinix Hot",
                "target_audience": "Students"
            },
            "images": [
                "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1601784551446-20c9e07cdbdb?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 40
        },
        {
            "name": "Tecno Spark 20",
            "brand": "Tecno",
            "category": "Phone",
            "price_category": "Budget",
            "performance_tier": "Entry",
            "brand_series": "Tecno Spark",
            "target_audience": "Students",
            "price": 1499900,
            "description": "Affordable smartphone with decent performance and features.",
            "specs": {
                "screen_size": "6.6 inch IPS LCD",
                "ram": "4GB",
                "storage": "128GB",
                "battery": "5000 mAh",
                "camera": "48MP Dual Camera",
                "processor": "UNISOC Tiger T606",
                "price_category": "Budget",
                "performance_tier": "Entry",
                "brand_series": "Tecno Spark",
                "target_audience": "Students"
            },
            "images": [
                "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400&h=300&fit=crop&crop=center",
                "https://images.unsplash.com/photo-1580910051074-3eb694886505?w=400&h=300&fit=crop&crop=center"
            ],
            "in_stock": True,
            "stock_quantity": 45
        }
    ]
    
    print(f"📱 Creating {len(products)} categorized products\n")
    
    # Create products
    success_count = 0
    categories_stats = {
        "price_category": {},
        "performance_tier": {},
        "brand_series": {},
        "target_audience": {}
    }
    
    for i, product in enumerate(products, 1):
        print(f"[{i:2d}/{len(products)}] Creating {product['name']}...")
        
        if create_product(product):
            success_count += 1
            
            # Update stats
            for key in categories_stats.keys():
                value = product[key]
                if value not in categories_stats[key]:
                    categories_stats[key][value] = 0
                categories_stats[key][value] += 1
        
        # Small delay between requests
        time.sleep(0.5)
    
    print("\n" + "=" * 80)
    print("  CATEGORIZATION SUMMARY")
    print("=" * 80)
    print(f"✅ Successfully created: {success_count}/{len(products)} products\n")
    
    # Display category statistics
    print("📊 PRICE CATEGORIES:")
    for category, count in sorted(categories_stats['price_category'].items()):
        print(f"   {category}: {count} products")
    
    print("\n🚀 PERFORMANCE TIERS:")
    for tier, count in sorted(categories_stats['performance_tier'].items()):
        print(f"   {tier}: {count} products")
    
    print("\n📱 BRAND SERIES:")
    for series, count in sorted(categories_stats['brand_series'].items()):
        print(f"   {series}: {count} products")
    
    print("\n👥 TARGET AUDIENCES:")
    for audience, count in sorted(categories_stats['target_audience'].items()):
        print(f"   {audience}: {count} products")
    
    print("\n🎯 READY FOR FRONTEND INTEGRATION!")
    print("   - All products have proper categories")
    print("   - Ready for filtering and navigation")
    print("   - Categories stored in product specs")

if __name__ == '__main__':
    main()