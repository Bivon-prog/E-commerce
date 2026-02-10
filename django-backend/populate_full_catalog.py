#!/usr/bin/env python
"""
Populate Astra database with comprehensive phone catalog
All major brands with their series and 3 images each
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
            print(f"✅ Created: {product_data['name']}")
            return True
        else:
            print(f"❌ Failed to create {product_data['name']}: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error creating {product_data['name']}: {e}")
        return False

def main():
    print("=" * 80)
    print("  POPULATING ASTRA WITH COMPREHENSIVE PHONE CATALOG")
    print("=" * 80)
    
    # Comprehensive phone catalog with reliable image URLs
    products = [
        # APPLE IPHONES
        {
            "name": "iPhone 15 Pro Max",
            "brand": "Apple",
            "category": "Phone",
            "price": 16999900,
            "description": "The ultimate iPhone with titanium design, A17 Pro chip, and advanced camera system.",
            "specs": {
                "screen_size": "6.7 inch Super Retina XDR",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "Up to 29 hours video playback",
                "camera": "48MP Main | Ultra Wide | Telephoto",
                "processor": "A17 Pro chip"
            },
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-max-finish-select-202309-6-7inch-naturaltitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-max-finish-select-202309-6-7inch-bluetitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-max-finish-select-202309-6-7inch-whitetitanium?wid=400&hei=300&fmt=p-jpg&qlt=80"
            ],
            "in_stock": True,
            "stock_quantity": 20
        },
        {
            "name": "iPhone 15 Pro",
            "brand": "Apple",
            "category": "Phone",
            "price": 14999900,
            "description": "Pro performance with titanium design and A17 Pro chip.",
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
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-bluetitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-blacktitanium?wid=400&hei=300&fmt=p-jpg&qlt=80"
            ],
            "in_stock": True,
            "stock_quantity": 25
        },
        {
            "name": "iPhone 15",
            "brand": "Apple",
            "category": "Phone",
            "price": 11999900,
            "description": "The iPhone 15 with Dynamic Island and advanced dual-camera system.",
            "specs": {
                "screen_size": "6.1 inch Super Retina XDR",
                "ram": "6GB",
                "storage": "128GB",
                "battery": "Up to 20 hours video playback",
                "camera": "48MP Main | Ultra Wide",
                "processor": "A16 Bionic chip"
            },
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-finish-select-202309-6-1inch-pink?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-finish-select-202309-6-1inch-blue?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-finish-select-202309-6-1inch-green?wid=400&hei=300&fmt=p-jpg&qlt=80"
            ],
            "in_stock": True,
            "stock_quantity": 30
        },
        {
            "name": "iPhone 14",
            "brand": "Apple",
            "category": "Phone",
            "price": 9999900,
            "description": "iPhone 14 with advanced camera system and A15 Bionic chip.",
            "specs": {
                "screen_size": "6.1 inch Super Retina XDR",
                "ram": "6GB",
                "storage": "128GB",
                "battery": "Up to 20 hours video playback",
                "camera": "12MP Main | Ultra Wide",
                "processor": "A15 Bionic chip"
            },
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-finish-select-202209-6-1inch-blue?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-finish-select-202209-6-1inch-purple?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-finish-select-202209-6-1inch-midnight?wid=400&hei=300&fmt=p-jpg&qlt=80"
            ],
            "in_stock": True,
            "stock_quantity": 15
        },

        # SAMSUNG GALAXY
        {
            "name": "Galaxy S24 Ultra",
            "brand": "Samsung",
            "category": "Phone",
            "price": 13999900,
            "description": "The ultimate Galaxy with S Pen, AI features, and 200MP camera.",
            "specs": {
                "screen_size": "6.8 inch Dynamic AMOLED 2X",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "200MP Main | Ultra Wide | Telephoto",
                "processor": "Snapdragon 8 Gen 3"
            },
            "images": [
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Galaxy+S24+Ultra+Black",
                "https://via.placeholder.com/400x300/8b5cf6/ffffff?text=Galaxy+S24+Ultra+Violet",
                "https://via.placeholder.com/400x300/f3f4f6/1a1a1a?text=Galaxy+S24+Ultra+Gray"
            ],
            "in_stock": True,
            "stock_quantity": 18
        },
        {
            "name": "Galaxy S24+",
            "brand": "Samsung",
            "category": "Phone",
            "price": 11999900,
            "description": "Premium Galaxy experience with advanced AI and camera features.",
            "specs": {
                "screen_size": "6.7 inch Dynamic AMOLED 2X",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "4900 mAh",
                "camera": "50MP Main | Ultra Wide | Telephoto",
                "processor": "Snapdragon 8 Gen 3"
            },
            "images": [
                "https://via.placeholder.com/400x300/fbbf24/1a1a1a?text=Galaxy+S24%2B+Gold",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Galaxy+S24%2B+Black",
                "https://via.placeholder.com/400x300/8b5cf6/ffffff?text=Galaxy+S24%2B+Violet"
            ],
            "in_stock": True,
            "stock_quantity": 22
        },
        {
            "name": "Galaxy S24",
            "brand": "Samsung",
            "category": "Phone",
            "price": 9999900,
            "description": "Galaxy S24 with AI-powered features and premium design.",
            "specs": {
                "screen_size": "6.2 inch Dynamic AMOLED 2X",
                "ram": "8GB",
                "storage": "128GB",
                "battery": "4000 mAh",
                "camera": "50MP Main | Ultra Wide | Telephoto",
                "processor": "Snapdragon 8 Gen 3"
            },
            "images": [
                "https://via.placeholder.com/400x300/fbbf24/1a1a1a?text=Galaxy+S24+Amber",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Galaxy+S24+Black",
                "https://via.placeholder.com/400x300/f3f4f6/1a1a1a?text=Galaxy+S24+Marble"
            ],
            "in_stock": True,
            "stock_quantity": 25
        },
        {
            "name": "Galaxy A55",
            "brand": "Samsung",
            "category": "Phone",
            "price": 4999900,
            "description": "Mid-range Galaxy with premium features and great value.",
            "specs": {
                "screen_size": "6.6 inch Super AMOLED",
                "ram": "8GB",
                "storage": "128GB",
                "battery": "5000 mAh",
                "camera": "50MP Main | Ultra Wide | Macro",
                "processor": "Exynos 1480"
            },
            "images": [
                "https://via.placeholder.com/400x300/3b82f6/ffffff?text=Galaxy+A55+Blue",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Galaxy+A55+Black",
                "https://via.placeholder.com/400x300/f3f4f6/1a1a1a?text=Galaxy+A55+White"
            ],
            "in_stock": True,
            "stock_quantity": 35
        },

        # GOOGLE PIXEL
        {
            "name": "Pixel 8 Pro",
            "brand": "Google",
            "category": "Phone",
            "price": 11999900,
            "description": "The most advanced Pixel with Google AI and the best Pixel Camera.",
            "specs": {
                "screen_size": "6.7 inch Super Actua display",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "5050 mAh",
                "camera": "50MP Main | Ultra Wide | Telephoto",
                "processor": "Google Tensor G3"
            },
            "images": [
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Pixel+8+Pro+Obsidian",
                "https://via.placeholder.com/400x300/e5e7eb/1a1a1a?text=Pixel+8+Pro+Porcelain",
                "https://via.placeholder.com/400x300/3b82f6/ffffff?text=Pixel+8+Pro+Bay"
            ],
            "in_stock": True,
            "stock_quantity": 12
        },
        {
            "name": "Pixel 8",
            "brand": "Google",
            "category": "Phone",
            "price": 8999900,
            "description": "Google Pixel 8 with advanced AI features and pure Android experience.",
            "specs": {
                "screen_size": "6.2 inch Actua display",
                "ram": "8GB",
                "storage": "128GB",
                "battery": "4575 mAh",
                "camera": "50MP Main | Ultra Wide",
                "processor": "Google Tensor G3"
            },
            "images": [
                "https://via.placeholder.com/400x300/f59e0b/1a1a1a?text=Pixel+8+Hazel",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Pixel+8+Obsidian",
                "https://via.placeholder.com/400x300/ec4899/ffffff?text=Pixel+8+Rose"
            ],
            "in_stock": True,
            "stock_quantity": 18
        },
        {
            "name": "Pixel 7a",
            "brand": "Google",
            "category": "Phone",
            "price": 5999900,
            "description": "Pixel 7a with flagship camera features at an affordable price.",
            "specs": {
                "screen_size": "6.1 inch OLED",
                "ram": "8GB",
                "storage": "128GB",
                "battery": "4385 mAh",
                "camera": "64MP Main | Ultra Wide",
                "processor": "Google Tensor G2"
            },
            "images": [
                "https://via.placeholder.com/400x300/f3f4f6/1a1a1a?text=Pixel+7a+Snow",
                "https://via.placeholder.com/400x300/374151/ffffff?text=Pixel+7a+Charcoal",
                "https://via.placeholder.com/400x300/3b82f6/ffffff?text=Pixel+7a+Sea"
            ],
            "in_stock": True,
            "stock_quantity": 28
        },

        # XIAOMI
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
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Xiaomi+14+Ultra+Black",
                "https://via.placeholder.com/400x300/f3f4f6/1a1a1a?text=Xiaomi+14+Ultra+White",
                "https://via.placeholder.com/400x300/3b82f6/ffffff?text=Xiaomi+14+Ultra+Blue"
            ],
            "in_stock": True,
            "stock_quantity": 8
        },
        {
            "name": "Xiaomi 14",
            "brand": "Xiaomi",
            "category": "Phone",
            "price": 8999900,
            "description": "Flagship performance with Leica cameras and premium build quality.",
            "specs": {
                "screen_size": "6.36 inch LTPO AMOLED",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "4610 mAh",
                "camera": "50MP Leica Triple Camera",
                "processor": "Snapdragon 8 Gen 3"
            },
            "images": [
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Xiaomi+14+Black",
                "https://via.placeholder.com/400x300/f3f4f6/1a1a1a?text=Xiaomi+14+White",
                "https://via.placeholder.com/400x300/10b981/ffffff?text=Xiaomi+14+Green"
            ],
            "in_stock": True,
            "stock_quantity": 15
        },
        {
            "name": "Redmi Note 13 Pro",
            "brand": "Xiaomi",
            "category": "Phone",
            "price": 3999900,
            "description": "Premium mid-range phone with excellent camera and performance.",
            "specs": {
                "screen_size": "6.67 inch AMOLED",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "5100 mAh",
                "camera": "200MP Main | Ultra Wide | Macro",
                "processor": "Snapdragon 7s Gen 2"
            },
            "images": [
                "https://via.placeholder.com/400x300/8b5cf6/ffffff?text=Redmi+Note+13+Pro+Purple",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Redmi+Note+13+Pro+Black",
                "https://via.placeholder.com/400x300/3b82f6/ffffff?text=Redmi+Note+13+Pro+Blue"
            ],
            "in_stock": True,
            "stock_quantity": 40
        },

        # ONEPLUS
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
                "camera": "50MP Hasselblad Triple Camera",
                "processor": "Snapdragon 8 Gen 3"
            },
            "images": [
                "https://via.placeholder.com/400x300/10b981/ffffff?text=OnePlus+12+Green",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=OnePlus+12+Black",
                "https://via.placeholder.com/400x300/f3f4f6/1a1a1a?text=OnePlus+12+White"
            ],
            "in_stock": True,
            "stock_quantity": 15
        },
        {
            "name": "OnePlus 11",
            "brand": "OnePlus",
            "category": "Phone",
            "price": 6999900,
            "description": "Flagship killer with Hasselblad cameras and fast performance.",
            "specs": {
                "screen_size": "6.7 inch LTPO AMOLED",
                "ram": "8GB",
                "storage": "128GB",
                "battery": "5000 mAh",
                "camera": "50MP Hasselblad Triple Camera",
                "processor": "Snapdragon 8 Gen 2"
            },
            "images": [
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=OnePlus+11+Black",
                "https://via.placeholder.com/400x300/10b981/ffffff?text=OnePlus+11+Green",
                "https://via.placeholder.com/400x300/3b82f6/ffffff?text=OnePlus+11+Blue"
            ],
            "in_stock": True,
            "stock_quantity": 20
        },
        {
            "name": "OnePlus Nord 3",
            "brand": "OnePlus",
            "category": "Phone",
            "price": 4999900,
            "description": "Premium mid-range experience with flagship features.",
            "specs": {
                "screen_size": "6.74 inch AMOLED",
                "ram": "8GB",
                "storage": "128GB",
                "battery": "5000 mAh",
                "camera": "50MP Triple Camera",
                "processor": "MediaTek Dimensity 9000"
            },
            "images": [
                "https://via.placeholder.com/400x300/10b981/ffffff?text=OnePlus+Nord+3+Green",
                "https://via.placeholder.com/400x300/6b7280/ffffff?text=OnePlus+Nord+3+Gray",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=OnePlus+Nord+3+Black"
            ],
            "in_stock": True,
            "stock_quantity": 25
        },

        # OPPO
        {
            "name": "OPPO Find X7 Ultra",
            "brand": "Oppo",
            "category": "Phone",
            "price": 12999900,
            "description": "Photography flagship with Hasselblad cameras and premium design.",
            "specs": {
                "screen_size": "6.82 inch LTPO AMOLED",
                "ram": "16GB",
                "storage": "512GB",
                "battery": "5000 mAh",
                "camera": "50MP Hasselblad Quad Camera",
                "processor": "Snapdragon 8 Gen 3"
            },
            "images": [
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=OPPO+Find+X7+Ultra+Black",
                "https://via.placeholder.com/400x300/8b5cf6/ffffff?text=OPPO+Find+X7+Ultra+Purple",
                "https://via.placeholder.com/400x300/f3f4f6/1a1a1a?text=OPPO+Find+X7+Ultra+White"
            ],
            "in_stock": True,
            "stock_quantity": 10
        },
        {
            "name": "OPPO Reno 11",
            "brand": "Oppo",
            "category": "Phone",
            "price": 5999900,
            "description": "Stylish design with excellent camera and fast charging.",
            "specs": {
                "screen_size": "6.7 inch AMOLED",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "50MP Triple Camera",
                "processor": "MediaTek Dimensity 7050"
            },
            "images": [
                "https://via.placeholder.com/400x300/3b82f6/ffffff?text=OPPO+Reno+11+Blue",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=OPPO+Reno+11+Black",
                "https://via.placeholder.com/400x300/f59e0b/1a1a1a?text=OPPO+Reno+11+Gold"
            ],
            "in_stock": True,
            "stock_quantity": 18
        },
        {
            "name": "OPPO A79",
            "brand": "Oppo",
            "category": "Phone",
            "price": 2999900,
            "description": "Affordable smartphone with good performance and battery life.",
            "specs": {
                "screen_size": "6.72 inch IPS LCD",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "50MP Dual Camera",
                "processor": "MediaTek Dimensity 6020"
            },
            "images": [
                "https://via.placeholder.com/400x300/10b981/ffffff?text=OPPO+A79+Green",
                "https://via.placeholder.com/400x300/8b5cf6/ffffff?text=OPPO+A79+Purple",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=OPPO+A79+Black"
            ],
            "in_stock": True,
            "stock_quantity": 30
        },

        # VIVO
        {
            "name": "Vivo X100 Pro",
            "brand": "Vivo",
            "category": "Phone",
            "price": 11999900,
            "description": "Professional photography flagship with Zeiss cameras.",
            "specs": {
                "screen_size": "6.78 inch LTPO AMOLED",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "5400 mAh",
                "camera": "50MP Zeiss Triple Camera",
                "processor": "MediaTek Dimensity 9300"
            },
            "images": [
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Vivo+X100+Pro+Black",
                "https://via.placeholder.com/400x300/3b82f6/ffffff?text=Vivo+X100+Pro+Blue",
                "https://via.placeholder.com/400x300/f3f4f6/1a1a1a?text=Vivo+X100+Pro+White"
            ],
            "in_stock": True,
            "stock_quantity": 12
        },
        {
            "name": "Vivo V30",
            "brand": "Vivo",
            "category": "Phone",
            "price": 6999900,
            "description": "Stylish design with excellent selfie camera and performance.",
            "specs": {
                "screen_size": "6.78 inch AMOLED",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "50MP Triple Camera",
                "processor": "Snapdragon 7 Gen 3"
            },
            "images": [
                "https://via.placeholder.com/400x300/ec4899/ffffff?text=Vivo+V30+Pink",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Vivo+V30+Black",
                "https://via.placeholder.com/400x300/3b82f6/ffffff?text=Vivo+V30+Blue"
            ],
            "in_stock": True,
            "stock_quantity": 20
        },
        {
            "name": "Vivo Y36",
            "brand": "Vivo",
            "category": "Phone",
            "price": 2999900,
            "description": "Budget-friendly smartphone with good camera and battery life.",
            "specs": {
                "screen_size": "6.64 inch IPS LCD",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "50MP Dual Camera",
                "processor": "Snapdragon 680"
            },
            "images": [
                "https://via.placeholder.com/400x300/10b981/ffffff?text=Vivo+Y36+Green",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Vivo+Y36+Black",
                "https://via.placeholder.com/400x300/f59e0b/1a1a1a?text=Vivo+Y36+Gold"
            ],
            "in_stock": True,
            "stock_quantity": 35
        },

        # REALME
        {
            "name": "Realme GT 5 Pro",
            "brand": "Realme",
            "category": "Phone",
            "price": 7999900,
            "description": "Gaming flagship with powerful performance and fast charging.",
            "specs": {
                "screen_size": "6.78 inch LTPO AMOLED",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "5400 mAh",
                "camera": "50MP Triple Camera",
                "processor": "Snapdragon 8 Gen 3"
            },
            "images": [
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Realme+GT+5+Pro+Black",
                "https://via.placeholder.com/400x300/f3f4f6/1a1a1a?text=Realme+GT+5+Pro+White",
                "https://via.placeholder.com/400x300/3b82f6/ffffff?text=Realme+GT+5+Pro+Blue"
            ],
            "in_stock": True,
            "stock_quantity": 15
        },
        {
            "name": "Realme 12 Pro+",
            "brand": "Realme",
            "category": "Phone",
            "price": 4999900,
            "description": "Premium mid-range with excellent camera and design.",
            "specs": {
                "screen_size": "6.7 inch AMOLED",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "50MP Triple Camera",
                "processor": "Snapdragon 7s Gen 2"
            },
            "images": [
                "https://via.placeholder.com/400x300/10b981/ffffff?text=Realme+12+Pro%2B+Green",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Realme+12+Pro%2B+Black",
                "https://via.placeholder.com/400x300/f59e0b/1a1a1a?text=Realme+12+Pro%2B+Gold"
            ],
            "in_stock": True,
            "stock_quantity": 25
        },
        {
            "name": "Realme C67",
            "brand": "Realme",
            "category": "Phone",
            "price": 1999900,
            "description": "Budget smartphone with good performance and long battery life.",
            "specs": {
                "screen_size": "6.72 inch IPS LCD",
                "ram": "6GB",
                "storage": "128GB",
                "battery": "5000 mAh",
                "camera": "108MP Dual Camera",
                "processor": "Snapdragon 685"
            },
            "images": [
                "https://via.placeholder.com/400x300/fbbf24/1a1a1a?text=Realme+C67+Gold",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Realme+C67+Black",
                "https://via.placeholder.com/400x300/3b82f6/ffffff?text=Realme+C67+Blue"
            ],
            "in_stock": True,
            "stock_quantity": 50
        },

        # TECNO
        {
            "name": "Tecno Phantom V Fold",
            "brand": "Tecno",
            "category": "Phone",
            "price": 14999900,
            "description": "Innovative foldable smartphone with premium features.",
            "specs": {
                "screen_size": "7.85 inch LTPO AMOLED (unfolded)",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "50MP Triple Camera",
                "processor": "MediaTek Dimensity 9000+"
            },
            "images": [
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Tecno+Phantom+V+Fold+Black",
                "https://via.placeholder.com/400x300/f3f4f6/1a1a1a?text=Tecno+Phantom+V+Fold+White",
                "https://via.placeholder.com/400x300/fbbf24/1a1a1a?text=Tecno+Phantom+V+Fold+Gold"
            ],
            "in_stock": True,
            "stock_quantity": 5
        },
        {
            "name": "Tecno Camon 30 Pro",
            "brand": "Tecno",
            "category": "Phone",
            "price": 3999900,
            "description": "Camera-focused smartphone with AI photography features.",
            "specs": {
                "screen_size": "6.78 inch AMOLED",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "50MP Triple Camera",
                "processor": "MediaTek Dimensity 8050"
            },
            "images": [
                "https://via.placeholder.com/400x300/10b981/ffffff?text=Tecno+Camon+30+Pro+Green",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Tecno+Camon+30+Pro+Black",
                "https://via.placeholder.com/400x300/3b82f6/ffffff?text=Tecno+Camon+30+Pro+Blue"
            ],
            "in_stock": True,
            "stock_quantity": 20
        },
        {
            "name": "Tecno Spark 20",
            "brand": "Tecno",
            "category": "Phone",
            "price": 1499900,
            "description": "Affordable smartphone with decent performance and features.",
            "specs": {
                "screen_size": "6.6 inch IPS LCD",
                "ram": "4GB",
                "storage": "128GB",
                "battery": "5000 mAh",
                "camera": "48MP Dual Camera",
                "processor": "UNISOC Tiger T606"
            },
            "images": [
                "https://via.placeholder.com/400x300/ec4899/ffffff?text=Tecno+Spark+20+Pink",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Tecno+Spark+20+Black",
                "https://via.placeholder.com/400x300/3b82f6/ffffff?text=Tecno+Spark+20+Blue"
            ],
            "in_stock": True,
            "stock_quantity": 40
        },

        # INFINIX
        {
            "name": "Infinix Note 40 Pro",
            "brand": "Infinix",
            "category": "Phone",
            "price": 3499900,
            "description": "Performance-focused smartphone with fast charging and good cameras.",
            "specs": {
                "screen_size": "6.78 inch AMOLED",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "108MP Triple Camera",
                "processor": "MediaTek Dimensity 7020"
            },
            "images": [
                "https://via.placeholder.com/400x300/fbbf24/1a1a1a?text=Infinix+Note+40+Pro+Gold",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Infinix+Note+40+Pro+Black",
                "https://via.placeholder.com/400x300/8b5cf6/ffffff?text=Infinix+Note+40+Pro+Purple"
            ],
            "in_stock": True,
            "stock_quantity": 25
        },
        {
            "name": "Infinix Hot 40i",
            "brand": "Infinix",
            "category": "Phone",
            "price": 1799900,
            "description": "Budget-friendly smartphone with good battery life and performance.",
            "specs": {
                "screen_size": "6.7 inch IPS LCD",
                "ram": "4GB",
                "storage": "128GB",
                "battery": "5000 mAh",
                "camera": "32MP Dual Camera",
                "processor": "UNISOC Tiger T606"
            },
            "images": [
                "https://via.placeholder.com/400x300/10b981/ffffff?text=Infinix+Hot+40i+Green",
                "https://via.placeholder.com/400x300/1a1a1a/ffffff?text=Infinix+Hot+40i+Black",
                "https://via.placeholder.com/400x300/fbbf24/1a1a1a?text=Infinix+Hot+40i+Gold"
            ],
            "in_stock": True,
            "stock_quantity": 35
        }
    ]
    
    print(f"📱 Total products to create: {len(products)}")
    print(f"📊 Brands: {len(set(p['brand'] for p in products))}")
    print()
    
    # Create products with delay to avoid overwhelming the API
    success_count = 0
    failed_products = []
    
    for i, product in enumerate(products, 1):
        print(f"[{i:2d}/{len(products)}] Creating {product['name']}...")
        
        if create_product(product):
            success_count += 1
        else:
            failed_products.append(product['name'])
        
        # Small delay between requests
        time.sleep(0.5)
    
    print("\n" + "=" * 80)
    print("  SUMMARY")
    print("=" * 80)
    print(f"✅ Successfully created: {success_count}/{len(products)} products")
    
    if failed_products:
        print(f"❌ Failed products: {len(failed_products)}")
        for name in failed_products:
            print(f"   - {name}")
    
    # Test final retrieval
    print("\n📋 Testing final product retrieval...")
    try:
        response = requests.get('http://localhost:8080/api/v1/products')
        if response.status_code == 200:
            products = response.json()
            print(f"✅ Total products in Astra: {len(products)}")
            
            # Group by brand
            brands = {}
            for product in products:
                brand = product['brand']
                if brand not in brands:
                    brands[brand] = 0
                brands[brand] += 1
            
            print("\n📊 Products by brand:")
            for brand, count in sorted(brands.items()):
                print(f"   {brand}: {count} products")
        else:
            print(f"❌ Failed to retrieve products: {response.text}")
    except Exception as e:
        print(f"❌ Error retrieving products: {e}")

if __name__ == '__main__':
    main()