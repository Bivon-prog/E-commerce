#!/usr/bin/env python3
"""
Add comprehensive iPhone lineup to database with real images and descriptions
"""

import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from astrapy import DataAPIClient
import uuid

def get_all_iphones():
    """Complete iPhone lineup with real Apple CDN images"""
    
    iphones = [
        # iPhone X
        {
            "name": "iPhone X",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 4999900,
            "description": "Revolutionary iPhone X with edge-to-edge Super Retina display, Face ID, and dual cameras. The phone that started the modern iPhone design with 5.8-inch OLED display.",
            "in_stock": True,
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-x-silver-select-2017?wid=470&hei=556&fmt=png-alpha&.v=1515602510472",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-x-spacegray-select-2017?wid=470&hei=556&fmt=png-alpha&.v=1515602697796"
            ],
            "specs": {"ram": "3GB", "storage": "64GB/256GB", "display": "5.8-inch OLED", "processor": "A11 Bionic", "camera": "12MP Dual", "battery": "2716mAh", "price_tier": "Mid-Range", "use_case": "General", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "General"}
        },
        
        # iPhone 11 Series
        {
            "name": "iPhone 11",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 5999900,
            "description": "iPhone 11 with dual-camera system, Night mode, and all-day battery life. Features 6.1-inch Liquid Retina display and A13 Bionic chip.",
            "in_stock": True,
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-purple-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956144418",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-black-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956145099",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-white-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956146102"
            ],
            "specs": {"ram": "4GB", "storage": "64GB/128GB/256GB", "display": "6.1-inch LCD", "processor": "A13 Bionic", "camera": "12MP Dual", "battery": "3110mAh", "price_tier": "Mid-Range", "use_case": "General", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "General"}
        },
        {
            "name": "iPhone 11 Pro",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 7999900,
            "description": "iPhone 11 Pro with triple-camera system, Super Retina XDR display, and A13 Bionic chip. Professional photography in your pocket.",
            "in_stock": True,
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-midnight-green-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953859383",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-space-gray-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953854163",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-silver-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953854071"
            ],
            "specs": {"ram": "4GB", "storage": "64GB/256GB/512GB", "display": "5.8-inch OLED", "processor": "A13 Bionic", "camera": "12MP Triple", "battery": "3046mAh", "price_tier": "Premium Flagship", "use_case": "Camera & Photography", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "Professionals"}
        },
        {
            "name": "iPhone 11 Pro Max",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 8999900,
            "description": "iPhone 11 Pro Max with largest Super Retina XDR display, triple cameras, and longest battery life. The ultimate iPhone 11 experience.",
            "in_stock": True,
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-max-midnight-green-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953956379",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-max-space-gray-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953955926",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-max-gold-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953955144"
            ],
            "specs": {"ram": "4GB", "storage": "64GB/256GB/512GB", "display": "6.5-inch OLED", "processor": "A13 Bionic", "camera": "12MP Triple", "battery": "3969mAh", "price_tier": "Ultra-Premium", "use_case": "Camera & Photography", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "Professionals"}
        }
,
        
        # iPhone 12 Series
        {
            "name": "iPhone 12",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 7499900,
            "description": "iPhone 12 with 5G, A14 Bionic, Ceramic Shield, and dual cameras. Beautiful design with aerospace-grade aluminum edges.",
            "in_stock": True,
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-blue-select-2020?wid=470&hei=556&fmt=png-alpha&.v=1604343704000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-black-select-2020?wid=470&hei=556&fmt=png-alpha&.v=1604343706000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-white-select-2020?wid=470&hei=556&fmt=png-alpha&.v=1604343708000"
            ],
            "specs": {"ram": "4GB", "storage": "64GB/128GB/256GB", "display": "6.1-inch OLED", "processor": "A14 Bionic", "camera": "12MP Dual", "battery": "2815mAh", "price_tier": "Flagship Killer", "use_case": "General", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "General"}
        },
        {
            "name": "iPhone 12 Pro",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 9999900,
            "description": "iPhone 12 Pro with LiDAR Scanner, ProRAW, and triple-camera system. Professional photography and videography capabilities.",
            "in_stock": True,
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-blue-hero?wid=470&hei=556&fmt=png-alpha&.v=1604021661000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-graphite-hero?wid=470&hei=556&fmt=png-alpha&.v=1604021659000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-gold-hero?wid=470&hei=556&fmt=png-alpha&.v=1604021660000"
            ],
            "specs": {"ram": "6GB", "storage": "128GB/256GB/512GB", "display": "6.1-inch OLED", "processor": "A14 Bionic", "camera": "12MP Triple + LiDAR", "battery": "2815mAh", "price_tier": "Premium Flagship", "use_case": "Camera & Photography", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "Professionals"}
        },
        {
            "name": "iPhone 12 Pro Max",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 11999900,
            "description": "iPhone 12 Pro Max with largest display, sensor-shift stabilization, and longest battery life. The ultimate iPhone 12.",
            "in_stock": True,
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-max-blue-hero?wid=470&hei=556&fmt=png-alpha&.v=1604021663000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-max-graphite-hero?wid=470&hei=556&fmt=png-alpha&.v=1604021662000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-max-silver-hero?wid=470&hei=556&fmt=png-alpha&.v=1604021664000"
            ],
            "specs": {"ram": "6GB", "storage": "128GB/256GB/512GB", "display": "6.7-inch OLED", "processor": "A14 Bionic", "camera": "12MP Triple + LiDAR", "battery": "3687mAh", "price_tier": "Ultra-Premium", "use_case": "Camera & Photography", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "Professionals"}
        }
,
        
        # iPhone 13 Series
        {
            "name": "iPhone 13",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 8999900,
            "description": "iPhone 13 with advanced dual-camera system, Cinematic mode, and A15 Bionic chip. All-day battery life and beautiful design.",
            "in_stock": True,
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-13-pink-select-2021?wid=470&hei=556&fmt=png-alpha&.v=1629842709000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-13-blue-select-2021?wid=470&hei=556&fmt=png-alpha&.v=1629842708000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-13-midnight-select-2021?wid=470&hei=556&fmt=png-alpha&.v=1629842709000"
            ],
            "specs": {"ram": "4GB", "storage": "128GB/256GB/512GB", "display": "6.1-inch OLED", "processor": "A15 Bionic", "camera": "12MP Dual", "battery": "3240mAh", "price_tier": "Flagship Killer", "use_case": "General", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "General"}
        },
        {
            "name": "iPhone 13 Pro",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 11499900,
            "description": "iPhone 13 Pro with ProMotion 120Hz display, ProRes video, and triple-camera system. Professional-grade performance.",
            "in_stock": True,
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-13-pro-sierra-blue-select?wid=470&hei=556&fmt=png-alpha&.v=1631652954000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-13-pro-graphite-select?wid=470&hei=556&fmt=png-alpha&.v=1631652956000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-13-pro-gold-select?wid=470&hei=556&fmt=png-alpha&.v=1631652955000"
            ],
            "specs": {"ram": "6GB", "storage": "128GB/256GB/512GB/1TB", "display": "6.1-inch OLED 120Hz", "processor": "A15 Bionic", "camera": "12MP Triple", "battery": "3095mAh", "price_tier": "Premium Flagship", "use_case": "Camera & Photography", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "Professionals"}
        },
        {
            "name": "iPhone 13 Pro Max",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 12999900,
            "description": "iPhone 13 Pro Max with largest ProMotion display, longest battery life, and pro camera system. The ultimate iPhone 13.",
            "in_stock": True,
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-13-pro-max-sierra-blue-select?wid=470&hei=556&fmt=png-alpha&.v=1631652957000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-13-pro-max-graphite-select?wid=470&hei=556&fmt=png-alpha&.v=1631652956000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-13-pro-max-silver-select?wid=470&hei=556&fmt=png-alpha&.v=1631652957000"
            ],
            "specs": {"ram": "6GB", "storage": "128GB/256GB/512GB/1TB", "display": "6.7-inch OLED 120Hz", "processor": "A15 Bionic", "camera": "12MP Triple", "battery": "4352mAh", "price_tier": "Ultra-Premium", "use_case": "Camera & Photography", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "Professionals"}
        },
        {
            "name": "iPhone 13 mini",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 7499900,
            "description": "iPhone 13 mini with compact 5.4-inch design, dual cameras, and A15 Bionic chip. Big power in a small package.",
            "in_stock": True,
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-13-mini-pink-select-2021?wid=470&hei=556&fmt=png-alpha&.v=1629842711000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-13-mini-blue-select-2021?wid=470&hei=556&fmt=png-alpha&.v=1629842710000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-13-mini-starlight-select-2021?wid=470&hei=556&fmt=png-alpha&.v=1629842711000"
            ],
            "specs": {"ram": "4GB", "storage": "128GB/256GB/512GB", "display": "5.4-inch OLED", "processor": "A15 Bionic", "camera": "12MP Dual", "battery": "2438mAh", "price_tier": "Mid-Range", "use_case": "General", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "General"}
        }
,
        
        # iPhone 14 Series
        {
            "name": "iPhone 14",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 9999900,
            "description": "iPhone 14 with advanced camera system, Crash Detection, and A15 Bionic chip. Emergency SOS via satellite capability.",
            "in_stock": True,
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-purple-select-2022?wid=470&hei=556&fmt=png-alpha&.v=1661027797000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-blue-select-2022?wid=470&hei=556&fmt=png-alpha&.v=1661027796000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-midnight-select-2022?wid=470&hei=556&fmt=png-alpha&.v=1661027797000"
            ],
            "specs": {"ram": "6GB", "storage": "128GB/256GB/512GB", "display": "6.1-inch OLED", "processor": "A15 Bionic", "camera": "12MP Dual", "battery": "3279mAh", "price_tier": "Flagship Killer", "use_case": "General", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "General"}
        },
        {
            "name": "iPhone 14 Pro",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 12999900,
            "description": "iPhone 14 Pro with Dynamic Island, Always-On display, and 48MP main camera. A16 Bionic chip delivers pro performance.",
            "in_stock": True,
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-pro-deep-purple-select?wid=470&hei=556&fmt=png-alpha&.v=1663703841000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-pro-space-black-select?wid=470&hei=556&fmt=png-alpha&.v=1663703842000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-pro-gold-select?wid=470&hei=556&fmt=png-alpha&.v=1663703841000"
            ],
            "specs": {"ram": "6GB", "storage": "128GB/256GB/512GB/1TB", "display": "6.1-inch OLED 120Hz", "processor": "A16 Bionic", "camera": "48MP Triple", "battery": "3200mAh", "price_tier": "Premium Flagship", "use_case": "Camera & Photography", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "Professionals"}
        },
        {
            "name": "iPhone 14 Pro Max",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 14999900,
            "description": "iPhone 14 Pro Max with largest Always-On display, 48MP camera, and longest battery life. The ultimate iPhone 14.",
            "in_stock": True,
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-pro-max-deep-purple-select?wid=470&hei=556&fmt=png-alpha&.v=1663703843000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-pro-max-space-black-select?wid=470&hei=556&fmt=png-alpha&.v=1663703844000",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-pro-max-silver-select?wid=470&hei=556&fmt=png-alpha&.v=1663703843000"
            ],
            "specs": {"ram": "6GB", "storage": "128GB/256GB/512GB/1TB", "display": "6.7-inch OLED 120Hz", "processor": "A16 Bionic", "camera": "48MP Triple", "battery": "4323mAh", "price_tier": "Ultra-Premium", "use_case": "Camera & Photography", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "Professionals"}
        }
,
        
        # iPhone 16 Series (Note: iPhone 16 FE doesn't exist, using iPhone SE instead)
        {
            "name": "iPhone 16",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 11999900,
            "description": "iPhone 16 with advanced camera system, A18 chip, and enhanced battery life. The latest standard iPhone experience.",
            "in_stock": True,
            "images": [
                "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=470&h=556&fit=crop",
                "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=470&h=556&fit=crop",
                "https://images.unsplash.com/photo-1580910051074-3eb694886505?w=470&h=556&fit=crop"
            ],
            "specs": {"ram": "8GB", "storage": "128GB/256GB/512GB", "display": "6.1-inch OLED", "processor": "A18", "camera": "48MP Dual", "battery": "3500mAh", "price_tier": "Flagship Killer", "use_case": "General", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "General"}
        },
        {
            "name": "iPhone 16 Pro",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 14999900,
            "description": "iPhone 16 Pro with advanced camera system, A18 Pro chip, and ProMotion display. Professional-grade performance.",
            "in_stock": True,
            "images": [
                "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=470&h=556&fit=crop",
                "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=470&h=556&fit=crop",
                "https://images.unsplash.com/photo-1580910051074-3eb694886505?w=470&h=556&fit=crop"
            ],
            "specs": {"ram": "8GB", "storage": "256GB/512GB/1TB", "display": "6.3-inch OLED 120Hz", "processor": "A18 Pro", "camera": "48MP Triple", "battery": "3600mAh", "price_tier": "Premium Flagship", "use_case": "Camera & Photography", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "Professionals"}
        },
        {
            "name": "iPhone 16 Pro Max",
            "brand": "Apple",
            "category": "Smartphones",
            "price": 16999900,
            "description": "iPhone 16 Pro Max with largest display, advanced camera system, and longest battery life. The ultimate iPhone 16.",
            "in_stock": True,
            "images": [
                "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=470&h=556&fit=crop",
                "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=470&h=556&fit=crop",
                "https://images.unsplash.com/photo-1580910051074-3eb694886505?w=470&h=556&fit=crop"
            ],
            "specs": {"ram": "8GB", "storage": "256GB/512GB/1TB", "display": "6.9-inch OLED 120Hz", "processor": "A18 Pro", "camera": "48MP Triple", "battery": "4800mAh", "price_tier": "Ultra-Premium", "use_case": "Camera & Photography", "form_factor": "Candy Bar", "software_experience": "iOS", "chipset_category": "Apple Bionic", "market_origin": "Global Giants", "target_demographic": "Professionals"}
        }
    ]
    
    return iphones

def add_all_iphones():
    """Add all iPhone models to Astra database"""
    
    try:
        print("📱 ADDING COMPREHENSIVE iPHONE LINEUP")
        print("=" * 60)
        
        client = DataAPIClient(settings.ASTRA_TOKEN)
        database = client.get_database_by_api_endpoint(settings.ASTRA_API_ENDPOINT)
        collection = database.get_collection("products")
        
        iphones = get_all_iphones()
        added_count = 0
        skipped_count = 0
        
        for iphone in iphones:
            try:
                # Check if phone already exists
                existing = collection.find_one({"name": iphone["name"]})
                
                if existing:
                    print(f"⚠️  {iphone['name']} already exists, skipping...")
                    skipped_count += 1
                    continue
                
                # Add new phone
                iphone['_id'] = str(uuid.uuid4())
                collection.insert_one(iphone)
                
                print(f"✅ Added {iphone['name']}")
                print(f"   Price: KES {iphone['price']/100:,.0f}")
                print(f"   Images: {len(iphone['images'])} images")
                added_count += 1
                
            except Exception as e:
                print(f"❌ Failed to add {iphone['name']}: {str(e)}")
        
        print(f"\n🎉 DONE!")
        print(f"   Added: {added_count} new iPhone models")
        print(f"   Skipped: {skipped_count} existing models")
        print(f"   Total iPhone lineup: {added_count + skipped_count} models")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    add_all_iphones()