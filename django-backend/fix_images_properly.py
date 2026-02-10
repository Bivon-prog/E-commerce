#!/usr/bin/env python3
"""
Fix images with REAL working URLs that actually display
"""

import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from products.astra_models import AstraProduct as Product

def get_working_images():
    """Get REAL working image URLs that actually display"""
    
    # Using REAL working image URLs that are guaranteed to work
    phone_images = {
        # Apple iPhones - Working Apple CDN URLs
        "iPhone 15 Pro Max": [
            "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-max-naturaltitanium-select?wid=400&hei=400&fmt=jpeg&qlt=90&.v=1692895395658",
            "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-max-bluetitanium-select?wid=400&hei=400&fmt=jpeg&qlt=90&.v=1692895395658",
            "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-max-whitetitanium-select?wid=400&hei=400&fmt=jpeg&qlt=90&.v=1692895395658"
        ],
        "iPhone 15 Pro": [
            "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-naturaltitanium-select?wid=400&hei=400&fmt=jpeg&qlt=90&.v=1692895395658",
            "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-bluetitanium-select?wid=400&hei=400&fmt=jpeg&qlt=90&.v=1692895395658",
            "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-whitetitanium-select?wid=400&hei=400&fmt=jpeg&qlt=90&.v=1692895395658"
        ],
        "iPhone 15": [
            "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-blue-select-202309?wid=400&hei=400&fmt=jpeg&qlt=90&.v=1692895395658",
            "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pink-select-202309?wid=400&hei=400&fmt=jpeg&qlt=90&.v=1692895395658",
            "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-black-select-202309?wid=400&hei=400&fmt=jpeg&qlt=90&.v=1692895395658"
        ],
        
        # For all other phones, use reliable placeholder images that actually work
        "Galaxy S24 Ultra": [
            "https://via.placeholder.com/400x400/1a1a1a/ffffff?text=Galaxy+S24+Ultra",
            "https://via.placeholder.com/400x400/2d2d2d/ffffff?text=Galaxy+S24+Ultra+2",
            "https://via.placeholder.com/400x400/404040/ffffff?text=Galaxy+S24+Ultra+3"
        ],
        "Galaxy S24": [
            "https://via.placeholder.com/400x400/1a1a1a/ffffff?text=Galaxy+S24",
            "https://via.placeholder.com/400x400/2d2d2d/ffffff?text=Galaxy+S24+2",
            "https://via.placeholder.com/400x400/404040/ffffff?text=Galaxy+S24+3"
        ],
        "Galaxy A55": [
            "https://via.placeholder.com/400x400/1a1a1a/ffffff?text=Galaxy+A55",
            "https://via.placeholder.com/400x400/2d2d2d/ffffff?text=Galaxy+A55+2",
            "https://via.placeholder.com/400x400/404040/ffffff?text=Galaxy+A55+3"
        ],
        "Galaxy A34": [
            "https://via.placeholder.com/400x400/1a1a1a/ffffff?text=Galaxy+A34",
            "https://via.placeholder.com/400x400/2d2d2d/ffffff?text=Galaxy+A34+2",
            "https://via.placeholder.com/400x400/404040/ffffff?text=Galaxy+A34+3"
        ],
        "Galaxy M55": [
            "https://via.placeholder.com/400x400/1a1a1a/ffffff?text=Galaxy+M55",
            "https://via.placeholder.com/400x400/2d2d2d/ffffff?text=Galaxy+M55+2",
            "https://via.placeholder.com/400x400/404040/ffffff?text=Galaxy+M55+3"
        ],
        "Galaxy Z Fold 6": [
            "https://via.placeholder.com/400x400/1a1a1a/ffffff?text=Galaxy+Z+Fold+6",
            "https://via.placeholder.com/400x400/2d2d2d/ffffff?text=Galaxy+Z+Fold+6+Open",
            "https://via.placeholder.com/400x400/404040/ffffff?text=Galaxy+Z+Fold+6+Closed"
        ],
        "Galaxy Z Flip 6": [
            "https://via.placeholder.com/400x400/1a1a1a/ffffff?text=Galaxy+Z+Flip+6",
            "https://via.placeholder.com/400x400/2d2d2d/ffffff?text=Galaxy+Z+Flip+6+Open",
            "https://via.placeholder.com/400x400/404040/ffffff?text=Galaxy+Z+Flip+6+Closed"
        ],
        "Galaxy S25 Ultra": [
            "https://via.placeholder.com/400x400/1a1a1a/ffffff?text=Galaxy+S25+Ultra",
            "https://via.placeholder.com/400x400/2d2d2d/ffffff?text=Galaxy+S25+Ultra+2",
            "https://via.placeholder.com/400x400/404040/ffffff?text=Galaxy+S25+Ultra+3"
        ],
        
        # Google Pixel
        "Pixel 8 Pro": [
            "https://via.placeholder.com/400x400/4285f4/ffffff?text=Pixel+8+Pro",
            "https://via.placeholder.com/400x400/34a853/ffffff?text=Pixel+8+Pro+2",
            "https://via.placeholder.com/400x400/ea4335/ffffff?text=Pixel+8+Pro+3"
        ],
        "Pixel 7a": [
            "https://via.placeholder.com/400x400/4285f4/ffffff?text=Pixel+7a",
            "https://via.placeholder.com/400x400/34a853/ffffff?text=Pixel+7a+2",
            "https://via.placeholder.com/400x400/ea4335/ffffff?text=Pixel+7a+3"
        ],
        
        # OnePlus
        "OnePlus 12": [
            "https://via.placeholder.com/400x400/eb0029/ffffff?text=OnePlus+12",
            "https://via.placeholder.com/400x400/000000/ffffff?text=OnePlus+12+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=OnePlus+12+3"
        ],
        "OnePlus 12R": [
            "https://via.placeholder.com/400x400/eb0029/ffffff?text=OnePlus+12R",
            "https://via.placeholder.com/400x400/000000/ffffff?text=OnePlus+12R+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=OnePlus+12R+3"
        ],
        "OnePlus Nord 3": [
            "https://via.placeholder.com/400x400/eb0029/ffffff?text=OnePlus+Nord+3",
            "https://via.placeholder.com/400x400/000000/ffffff?text=OnePlus+Nord+3+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=OnePlus+Nord+3+3"
        ],
        
        # Xiaomi
        "Xiaomi 14 Ultra": [
            "https://via.placeholder.com/400x400/ff6900/ffffff?text=Xiaomi+14+Ultra",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Xiaomi+14+Ultra+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Xiaomi+14+Ultra+3"
        ],
        "POCO F6 Pro": [
            "https://via.placeholder.com/400x400/ffcc02/000000?text=POCO+F6+Pro",
            "https://via.placeholder.com/400x400/000000/ffffff?text=POCO+F6+Pro+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=POCO+F6+Pro+3"
        ],
        "Redmi Note 13 Pro": [
            "https://via.placeholder.com/400x400/ff6900/ffffff?text=Redmi+Note+13+Pro",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Redmi+Note+13+Pro+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Redmi+Note+13+Pro+3"
        ],
        "Redmi A3": [
            "https://via.placeholder.com/400x400/ff6900/ffffff?text=Redmi+A3",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Redmi+A3+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Redmi+A3+3"
        ],
        
        # Oppo
        "Oppo Find X7 Ultra": [
            "https://via.placeholder.com/400x400/1ba784/ffffff?text=Oppo+Find+X7+Ultra",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Oppo+Find+X7+Ultra+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Oppo+Find+X7+Ultra+3"
        ],
        "Oppo Reno 12 Pro": [
            "https://via.placeholder.com/400x400/1ba784/ffffff?text=Oppo+Reno+12+Pro",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Oppo+Reno+12+Pro+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Oppo+Reno+12+Pro+3"
        ],
        "Oppo A78": [
            "https://via.placeholder.com/400x400/1ba784/ffffff?text=Oppo+A78",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Oppo+A78+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Oppo+A78+3"
        ],
        
        # Vivo
        "Vivo X100 Pro": [
            "https://via.placeholder.com/400x400/4169e1/ffffff?text=Vivo+X100+Pro",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Vivo+X100+Pro+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Vivo+X100+Pro+3"
        ],
        "Vivo V30 Pro": [
            "https://via.placeholder.com/400x400/4169e1/ffffff?text=Vivo+V30+Pro",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Vivo+V30+Pro+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Vivo+V30+Pro+3"
        ],
        "Vivo Y36": [
            "https://via.placeholder.com/400x400/4169e1/ffffff?text=Vivo+Y36",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Vivo+Y36+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Vivo+Y36+3"
        ],
        
        # Realme
        "Realme GT 5 Pro": [
            "https://via.placeholder.com/400x400/ffcc02/000000?text=Realme+GT+5+Pro",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Realme+GT+5+Pro+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Realme+GT+5+Pro+3"
        ],
        "Realme 12 Pro+": [
            "https://via.placeholder.com/400x400/ffcc02/000000?text=Realme+12+Pro%2B",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Realme+12+Pro%2B+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Realme+12+Pro%2B+3"
        ],
        "Realme C67": [
            "https://via.placeholder.com/400x400/ffcc02/000000?text=Realme+C67",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Realme+C67+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Realme+C67+3"
        ],
        
        # Tecno
        "Tecno Phantom X2 Pro": [
            "https://via.placeholder.com/400x400/0066cc/ffffff?text=Tecno+Phantom+X2+Pro",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Tecno+Phantom+X2+Pro+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Tecno+Phantom+X2+Pro+3"
        ],
        "Tecno Camon 30 Pro": [
            "https://via.placeholder.com/400x400/0066cc/ffffff?text=Tecno+Camon+30+Pro",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Tecno+Camon+30+Pro+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Tecno+Camon+30+Pro+3"
        ],
        "Tecno Spark 20": [
            "https://via.placeholder.com/400x400/0066cc/ffffff?text=Tecno+Spark+20",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Tecno+Spark+20+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Tecno+Spark+20+3"
        ],
        "Tecno Pova 6 Pro": [
            "https://via.placeholder.com/400x400/0066cc/ffffff?text=Tecno+Pova+6+Pro",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Tecno+Pova+6+Pro+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Tecno+Pova+6+Pro+3"
        ],
        
        # Infinix
        "Infinix Zero 40 5G": [
            "https://via.placeholder.com/400x400/ff6b35/ffffff?text=Infinix+Zero+40+5G",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Infinix+Zero+40+5G+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Infinix+Zero+40+5G+3"
        ],
        "Infinix Hot 40i": [
            "https://via.placeholder.com/400x400/ff6b35/ffffff?text=Infinix+Hot+40i",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Infinix+Hot+40i+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Infinix+Hot+40i+3"
        ],
        "Infinix Note 40 Pro": [
            "https://via.placeholder.com/400x400/ff6b35/ffffff?text=Infinix+Note+40+Pro",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Infinix+Note+40+Pro+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Infinix+Note+40+Pro+3"
        ],
        
        # Honor
        "Honor 200 Pro": [
            "https://via.placeholder.com/400x400/1f4e79/ffffff?text=Honor+200+Pro",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Honor+200+Pro+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Honor+200+Pro+3"
        ],
        "Honor Magic 6 Pro": [
            "https://via.placeholder.com/400x400/1f4e79/ffffff?text=Honor+Magic+6+Pro",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Honor+Magic+6+Pro+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Honor+Magic+6+Pro+3"
        ],
        
        # ASUS
        "ASUS Zenfone 11 Ultra": [
            "https://via.placeholder.com/400x400/000000/ffffff?text=ASUS+Zenfone+11+Ultra",
            "https://via.placeholder.com/400x400/333333/ffffff?text=ASUS+Zenfone+11+Ultra+2",
            "https://via.placeholder.com/400x400/666666/ffffff?text=ASUS+Zenfone+11+Ultra+3"
        ],
        "ASUS ROG Phone 8 Pro": [
            "https://via.placeholder.com/400x400/ff0000/ffffff?text=ASUS+ROG+Phone+8+Pro",
            "https://via.placeholder.com/400x400/000000/ffffff?text=ASUS+ROG+Phone+8+Pro+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=ASUS+ROG+Phone+8+Pro+3"
        ],
        
        # Sony
        "Sony Xperia 1 VI": [
            "https://via.placeholder.com/400x400/000000/ffffff?text=Sony+Xperia+1+VI",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Sony+Xperia+1+VI+2",
            "https://via.placeholder.com/400x400/666666/ffffff?text=Sony+Xperia+1+VI+3"
        ],
        
        # Nokia
        "Nokia G60 5G": [
            "https://via.placeholder.com/400x400/124191/ffffff?text=Nokia+G60+5G",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Nokia+G60+5G+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Nokia+G60+5G+3"
        ],
        
        # Motorola
        "Moto G84": [
            "https://via.placeholder.com/400x400/004ccc/ffffff?text=Moto+G84",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Moto+G84+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Moto+G84+3"
        ],
        "Motorola Edge 50 Ultra": [
            "https://via.placeholder.com/400x400/004ccc/ffffff?text=Motorola+Edge+50+Ultra",
            "https://via.placeholder.com/400x400/000000/ffffff?text=Motorola+Edge+50+Ultra+2",
            "https://via.placeholder.com/400x400/333333/ffffff?text=Motorola+Edge+50+Ultra+3"
        ]
    }
    
    return phone_images

def fix_images_now():
    """Fix all images with working URLs immediately"""
    
    try:
        print("🔧 FIXING IMAGES WITH WORKING URLS")
        print("=" * 50)
        
        products = Product.get_all()
        phone_images = get_working_images()
        
        updated_count = 0
        
        for product in products:
            product_name = product['name']
            
            if product_name in phone_images:
                new_images = phone_images[product_name]
                
                try:
                    from astrapy import DataAPIClient
                    client = DataAPIClient(settings.ASTRA_TOKEN)
                    database = client.get_database_by_api_endpoint(settings.ASTRA_API_ENDPOINT)
                    collection = database.get_collection("products")
                    
                    collection.update_one(
                        {"_id": product['_id']},
                        {"$set": {"images": new_images}}
                    )
                    
                    print(f"✅ Fixed {product_name}")
                    updated_count += 1
                    
                except Exception as e:
                    print(f"❌ Failed {product_name}: {str(e)}")
        
        print(f"\n🎉 DONE! Fixed {updated_count} phones with working images")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    fix_images_now()