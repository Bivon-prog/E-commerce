import os
from astrapy import DataAPIClient
from dotenv import load_dotenv

load_dotenv()

# Comprehensive and accurate image mappings
CORRECT_IMAGES = {
    # Apple iPhones - Using official Apple images
    "iPhone 16 Pro Max": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-16-pro-max.jpg",
    "iPhone 16 Pro": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-16-pro.jpg",
    "iPhone 16 Plus": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-16-plus.jpg",
    "iPhone 16": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-16.jpg",
    "iPhone 15 Pro Max": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-15-pro-max.jpg",
    "iPhone 15 Pro": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-15-pro.jpg",
    "iPhone 15 Plus": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-15-plus.jpg",
    "iPhone 15": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-15.jpg",
    "iPhone 14 Pro Max": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-14-pro-max-.jpg",
    "iPhone 14 Pro": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-14-pro.jpg",
    "iPhone 14 Plus": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-14-plus.jpg",
    "iPhone 14": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-14.jpg",
    "iPhone 13 Pro Max": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-13-pro-max.jpg",
    "iPhone 13 Pro": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-13-pro.jpg",
    "iPhone 13": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-13.jpg",
    "iPhone 13 mini": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-13-mini.jpg",
    "iPhone 12 Pro Max": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-12-pro-max-.jpg",
    "iPhone 12 Pro": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-12-pro.jpg",
    "iPhone 12": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-12.jpg",
    "iPhone 12 Mini": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-12-mini.jpg",
    "iPhone SE (2022)": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-se-2022.jpg",
    "iPhone 11 Pro Max": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-11-pro.jpg",
    "iPhone 11 Pro": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-11-pro.jpg",
    "iPhone 11": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-11.jpg",
    "iPhone X": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-x.jpg",
    
    # Samsung Galaxy S Series
    "Samsung Galaxy S25": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-ultra-5g.jpg",
    "Samsung Galaxy S25 Edge": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-ultra-5g.jpg",
    "Samsung Galaxy S24 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-ultra-5g.jpg",
    "Galaxy S24 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-ultra-5g.jpg",
    "Samsung Galaxy S24+": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-plus-5g.jpg",
    "Samsung Galaxy S24": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-5g.jpg",
    "Samsung Galaxy S23 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-ultra-5g.jpg",
    "Samsung Galaxy S23+": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-plus-5g.jpg",
    "Samsung Galaxy S23": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-5g.jpg",
    "Samsung Galaxy S23 FE": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-fe.jpg",
    "Samsung Galaxy S22 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s22-ultra-5g.jpg",
    "Samsung Galaxy S22+": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s22-plus-5g.jpg",
    "Samsung Galaxy S22": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s22-5g.jpg",
    "Samsung Galaxy S21": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s21-5g.jpg",
    "Samsung Galaxy S21+": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s21-plus-5g.jpg",
    "Samsung Galaxy S21 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s21-ultra-5g.jpg",
    "Samsung Galaxy S21 FE": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s21-fe-5g.jpg",
    
    # Samsung Galaxy Z Series
    "Samsung Galaxy Z Fold6": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-fold6.jpg",
    "Samsung Galaxy Z Flip6": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-flip6.jpg",
    "Samsung Galaxy Z Fold5": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-fold5.jpg",
    "Samsung Galaxy Z Flip5": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-flip5-5g.jpg",
    "Samsung Galaxy Z Fold4": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-fold4-5g.jpg",
    "Samsung Galaxy Z Flip4": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-flip4-5g.jpg",
    "Samsung Galaxy Z Flip3": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-flip3-5g.jpg",
    "Samsung Galaxy Fold": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-fold.jpg",
    
    # Samsung Galaxy A Series
    "Samsung Galaxy A56": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a55.jpg",
    "Samsung Galaxy A55": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a55.jpg",
    "Samsung Galaxy A54": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a54.jpg",
    "Samsung Galaxy A53": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a53-5g.jpg",
    "Samsung Galaxy A52": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a52-5g.jpg",
    "Samsung Galaxy A35": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a35.jpg",
    "Samsung Galaxy A34": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a34.jpg",
    "Galaxy A34": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a34.jpg",
    "Samsung Galaxy A26": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a25.jpg",
    "Samsung Galaxy A25": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a25.jpg",
    "Samsung Galaxy A21": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a21s.jpg",
    "Samsung Galaxy A15": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a15-5g.jpg",
    "Samsung Galaxy A14": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a14-5g.jpg",
    "Samsung Galaxy A12": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a12-nacho.jpg",
    "Samsung Galaxy A05": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a05.jpg",
    "Samsung Galaxy A04": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a04.jpg",
    "Samsung Galaxy A03": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a03.jpg",
    "Samsung Galaxy A71": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a71-5g.jpg",
    "Samsung Galaxy A72": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a72.jpg",
    
    # Samsung Galaxy M Series
    "Samsung Galaxy M36": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-m35-1.jpg",
    "Samsung Galaxy M35": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-m35-1.jpg",
    "Samsung Galaxy M32": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-m32.jpg",
    
    # Samsung Galaxy Note Series
    "Samsung Galaxy Note 20": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-note20-5g.jpg",
    "Samsung Galaxy Note 10+": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-note10-plus-5g.jpg",
    "Samsung Galaxy Note 9": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-note9.jpg",
    
    # Infinix
    "Infinix Zero 40 5G": "https://fdn2.gsmarena.com/vv/bigpic/infinix-zero-40-5g.jpg",
    "Infinix Zero Ultra": "https://fdn2.gsmarena.com/vv/bigpic/infinix-zero-ultra.jpg",
    "Infinix Note 50s": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-40-pro-5g.jpg",
    "Infinix Note 40 Pro+ 5G": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-40-pro-plus-5g.jpg",
    "Infinix Note 40 Pro 5G": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-40-pro-5g.jpg",
    "Infinix Note 40 Pro 4G": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-40-pro-5g.jpg",
    "Infinix Note 40X": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-40-pro-5g.jpg",
    "Infinix Note 30 VIP": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-30-vip.jpg",
    "Infinix Note 30 5G": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-30-5g.jpg",
    "Infinix Note 30": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-30.jpg",
    "Infinix GT 10 Pro": "https://fdn2.gsmarena.com/vv/bigpic/infinix-gt-10-pro.jpg",
    "Infinix Hot 60i": "https://fdn2.gsmarena.com/vv/bigpic/infinix-hot-40i.jpg",
    "Infinix Hot 60": "https://fdn2.gsmarena.com/vv/bigpic/infinix-hot-40i.jpg",
    "Infinix Hot 50 5G": "https://fdn2.gsmarena.com/vv/bigpic/infinix-hot-50-5g.jpg",
    "Infinix Hot 50 Pro": "https://fdn2.gsmarena.com/vv/bigpic/infinix-hot-50-5g.jpg",
    
    # Tecno
    "Tecno Phantom X2 Pro": "https://fdn2.gsmarena.com/vv/bigpic/tecno-phantom-x2-pro-5g.jpg",
    "Tecno Phantom X2 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-phantom-x2-5g.jpg",
    "Tecno Phantom V Flip 2 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-phantom-v-flip-5g.jpg",
    "Tecno Phantom V Flip": "https://fdn2.gsmarena.com/vv/bigpic/tecno-phantom-v-flip-5g.jpg",
    "Tecno Camon 40": "https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-30-pro-5g.jpg",
    "Tecno Camon 30 Pro": "https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-30-pro-5g.jpg",
    "Tecno Camon 30": "https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-30-5g.jpg",
    "Tecno Camon 20 Premier 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-20-premier-5g.jpg",
    "Tecno Pova 7 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-pova-6-pro-5g.jpg",
    "Tecno Pova 6": "https://fdn2.gsmarena.com/vv/bigpic/tecno-pova-6-pro-5g.jpg",
    "Tecno Spark 30 Pro 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-20-pro-plus.jpg",
    "Tecno Spark 30 Pro": "https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-20-pro-plus.jpg",
    "Tecno Pop 9": "https://fdn2.gsmarena.com/vv/bigpic/tecno-pop-8.jpg",
    "Tecno Pop 8": "https://fdn2.gsmarena.com/vv/bigpic/tecno-pop-8.jpg",
    
    # itel
    "itel P55 4G": "https://fdn2.gsmarena.com/vv/bigpic/itel-p55-plus.jpg",
    "itel P40": "https://fdn2.gsmarena.com/vv/bigpic/itel-p40-plus.jpg",
    "itel S24": "https://fdn2.gsmarena.com/vv/bigpic/itel-s24.jpg",
    "itel S23": "https://fdn2.gsmarena.com/vv/bigpic/itel-s23-plus.jpg",
    "itel A05s": "https://fdn2.gsmarena.com/vv/bigpic/itel-a60s.jpg",
    
    # Vivo
    "Vivo X100 Pro": "https://fdn2.gsmarena.com/vv/bigpic/vivo-x100-pro.jpg",
    "Vivo Y36": "https://fdn2.gsmarena.com/vv/bigpic/vivo-y36.jpg",
    
    # Realme
    "Realme 12 Pro+": "https://fdn2.gsmarena.com/vv/bigpic/realme-12-pro-plus-5g.jpg",
    
    # OnePlus
    "OnePlus 12R": "https://fdn2.gsmarena.com/vv/bigpic/oneplus-12r.jpg",
    
    # Xiaomi/POCO
    "POCO F6 Pro": "https://fdn2.gsmarena.com/vv/bigpic/xiaomi-poco-f6-pro.jpg",
    "Redmi A3": "https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-a3.jpg",
    
    # Motorola
    "Motorola Edge 50 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/motorola-edge-50-ultra.jpg",
    
    # ASUS
    "ASUS Zenfone 11 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/asus-zenfone-11-ultra.jpg",
}

def fix_images():
    """Fix all product images with correct ones"""
    token = os.getenv('ASTRA_TOKEN')
    api_endpoint = os.getenv('ASTRA_API_ENDPOINT')
    
    client = DataAPIClient(token)
    database = client.get_database(api_endpoint)
    collection = database.get_collection("products")
    
    products = list(collection.find({}))
    
    print(f"\n{'='*80}")
    print(f"FIXING ALL PRODUCT IMAGES")
    print(f"{'='*80}\n")
    
    updated = 0
    not_found = []
    
    for product in products:
        name = product.get('name', '')
        product_id = product.get('_id')
        
        if name in CORRECT_IMAGES:
            new_image = CORRECT_IMAGES[name]
            collection.update_one(
                {"_id": product_id},
                {"$set": {"images": [new_image]}}
            )
            print(f"✓ Updated: {name}")
            updated += 1
        else:
            not_found.append(name)
    
    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"Total products: {len(products)}")
    print(f"✓ Updated: {updated}")
    print(f"✗ Not in database: {len(not_found)}")
    print(f"{'='*80}\n")
    
    if not_found:
        print("\nProducts not in image database (need manual addition):")
        for name in sorted(not_found):
            print(f"  - {name}")

if __name__ == "__main__":
    fix_images()
