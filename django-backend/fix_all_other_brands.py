import os
from astrapy import DataAPIClient
from dotenv import load_dotenv

load_dotenv()

# Working image URLs for all other brands using /vv/pics/ directory
OTHER_BRANDS_IMAGES = {
    # Tecno
    "Tecno Phantom X2 Pro": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-phantom-x2-pro-1.jpg",
    "Tecno Phantom X2 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-phantom-x2-1.jpg",
    "Tecno Phantom X2 Pro 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-phantom-x2-pro-1.jpg",
    "Tecno Phantom V Flip": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-phantom-v-flip-1.jpg",
    "Tecno Phantom V Flip 2 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-phantom-v-flip-1.jpg",
    "Tecno Phantom V Fold": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-phantom-v-fold-1.jpg",
    "Tecno Phantom V Fold 2 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-phantom-v-fold-1.jpg",
    "Tecno Camon 40": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-30-pro-1.jpg",
    "Tecno Camon 40 Pro 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-30-pro-1.jpg",
    "Tecno Camon 40 Pro 4G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-30-pro-1.jpg",
    "Tecno Camon 40 Premier 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-30-pro-1.jpg",
    "Tecno Camon 30": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-30-1.jpg",
    "Tecno Camon 30 Pro": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-30-pro-1.jpg",
    "Tecno Camon 30 Pro 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-30-pro-1.jpg",
    "Tecno Camon 30 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-30-1.jpg",
    "Tecno Camon 30 Premier 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-30-premier-1.jpg",
    "Tecno Camon 20": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-20-1.jpg",
    "Tecno Camon 20 Pro": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-20-pro-1.jpg",
    "Tecno Camon 20 Pro 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-20-pro-5g-1.jpg",
    "Tecno Camon 20 Premier 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-20-premier-1.jpg",
    "Tecno Pova 7 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-pova-6-pro-1.jpg",
    "Tecno Pova 7 Pro": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-pova-6-pro-1.jpg",
    "Tecno Pova 6": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-pova-6-pro-1.jpg",
    "Tecno Pova 6 Pro": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-pova-6-pro-1.jpg",
    "Tecno Pova 6 Pro 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-pova-6-pro-1.jpg",
    "Tecno Pova 6 Neo": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-pova-6-neo-1.jpg",
    "Tecno Pova 5": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-pova-5-1.jpg",
    "Tecno Pova 5 Pro": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-pova-5-pro-1.jpg",
    "Tecno Pova Slim 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-pova-6-pro-1.jpg",
    "Tecno Spark 40": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-spark-20-1.jpg",
    "Tecno Spark 40 Pro": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-spark-20-pro-1.jpg",
    "Tecno Spark 40 Pro+": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-spark-20-pro-plus-1.jpg",
    "Tecno Spark 40C": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-spark-20c-1.jpg",
    "Tecno Spark 30": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-spark-20-1.jpg",
    "Tecno Spark 30 Pro": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-spark-20-pro-1.jpg",
    "Tecno Spark 30 Pro 5G": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-spark-20-pro-plus-1.jpg",
    "Tecno Spark 30C": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-spark-20c-1.jpg",
    "Tecno Spark 20": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-spark-20-1.jpg",
    "Tecno Spark 20 Pro": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-spark-20-pro-1.jpg",
    "Tecno Spark 20 Pro+": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-spark-20-pro-plus-1.jpg",
    "Tecno Spark 20C": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-spark-20c-1.jpg",
    "Tecno Pop 10": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-pop-8-1.jpg",
    "Tecno Pop 10 Pro": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-pop-8-1.jpg",
    "Tecno Pop 9": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-pop-8-1.jpg",
    "Tecno Pop 8": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-pop-8-1.jpg",
    "Tecno Pop 7": "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-pop-7-pro-1.jpg",
    
    # Infinix
    "Infinix Zero Flip": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-zero-flip-1.jpg",
    "Infinix Zero 40 5G": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-zero-40-5g-1.jpg",
    "Infinix Zero 40 4G": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-zero-40-5g-1.jpg",
    "Infinix Zero 30 5G": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-zero-30-5g-1.jpg",
    "Infinix Zero 30 4G": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-zero-30-4g-1.jpg",
    "Infinix Zero Ultra": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-zero-ultra-1.jpg",
    "Infinix Note 60 Ultra": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-40-pro-1.jpg",
    "Infinix Note 60": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-40-pro-1.jpg",
    "Infinix Note 50s": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-40-pro-1.jpg",
    "Infinix Note 50 Pro+": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-40-pro-1.jpg",
    "Infinix Note 50 Pro": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-40-pro-1.jpg",
    "Infinix Note 40 Pro+ 5G": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-40-pro-1.jpg",
    "Infinix Note 40 Pro 5G": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-40-pro-1.jpg",
    "Infinix Note 40 Pro 4G": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-40-pro-1.jpg",
    "Infinix Note 40 Pro": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-40-pro-1.jpg",
    "Infinix Note 40X": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-40-pro-1.jpg",
    "Infinix Note 40": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-40-pro-1.jpg",
    "Infinix Note 30 VIP": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-30-vip-1.jpg",
    "Infinix Note 30 Pro": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-30-pro-1.jpg",
    "Infinix Note 30 5G": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-30-5g-1.jpg",
    "Infinix Note 30": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-30-1.jpg",
    "Infinix GT 30 Pro": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-gt-20-pro-1.jpg",
    "Infinix GT 20 Pro": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-gt-20-pro-1.jpg",
    "Infinix GT 10 Pro": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-gt-10-pro-1.jpg",
    "Infinix Hot 60 Pro+": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-hot-40-pro-1.jpg",
    "Infinix Hot 60 Pro": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-hot-40-pro-1.jpg",
    "Infinix Hot 60i": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-hot-40i-1.jpg",
    "Infinix Hot 60": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-hot-40i-1.jpg",
    "Infinix Hot 50 Pro+": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-hot-50-5g-1.jpg",
    "Infinix Hot 50 Pro": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-hot-50-5g-1.jpg",
    "Infinix Hot 50 5G": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-hot-50-5g-1.jpg",
    "Infinix Hot 50i": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-hot-50-5g-1.jpg",
    "Infinix Hot 40 Pro": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-hot-40-pro-1.jpg",
    "Infinix Hot 40": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-hot-40-1.jpg",
    "Infinix Hot 40i": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-hot-40i-1.jpg",
    "Infinix Smart 10 HD": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-smart-8-1.jpg",
    "Infinix Smart 10": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-smart-8-1.jpg",
    "Infinix Smart 9": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-smart-8-1.jpg",
    "Infinix Smart 8 Plus": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-smart-8-plus-1.jpg",
    "Infinix Smart 8": "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-smart-8-1.jpg",
    
    # itel
    "itel S25 Ultra": "https://fdn2.gsmarena.com/vv/pics/itel/itel-s24-1.jpg",
    "itel S25": "https://fdn2.gsmarena.com/vv/pics/itel/itel-s24-1.jpg",
    "itel S24": "https://fdn2.gsmarena.com/vv/pics/itel/itel-s24-1.jpg",
    "itel S23+": "https://fdn2.gsmarena.com/vv/pics/itel/itel-s23-plus-1.jpg",
    "itel S23": "https://fdn2.gsmarena.com/vv/pics/itel/itel-s23-plus-1.jpg",
    "itel P65": "https://fdn2.gsmarena.com/vv/pics/itel/itel-p55-plus-1.jpg",
    "itel P55+": "https://fdn2.gsmarena.com/vv/pics/itel/itel-p55-plus-1.jpg",
    "itel P55 5G": "https://fdn2.gsmarena.com/vv/pics/itel/itel-p55-plus-1.jpg",
    "itel P55 4G": "https://fdn2.gsmarena.com/vv/pics/itel/itel-p55-plus-1.jpg",
    "itel P40+": "https://fdn2.gsmarena.com/vv/pics/itel/itel-p40-plus-1.jpg",
    "itel P40": "https://fdn2.gsmarena.com/vv/pics/itel/itel-p40-plus-1.jpg",
    "itel A80": "https://fdn2.gsmarena.com/vv/pics/itel/itel-a60s-1.jpg",
    "itel A70": "https://fdn2.gsmarena.com/vv/pics/itel/itel-a60s-1.jpg",
    "itel A60s": "https://fdn2.gsmarena.com/vv/pics/itel/itel-a60s-1.jpg",
    "itel A60": "https://fdn2.gsmarena.com/vv/pics/itel/itel-a60-1.jpg",
    "itel A05s": "https://fdn2.gsmarena.com/vv/pics/itel/itel-a60s-1.jpg",
    
    # Other brands
    "OnePlus 12": "https://fdn2.gsmarena.com/vv/pics/oneplus/oneplus-12-1.jpg",
    "OnePlus 12R": "https://fdn2.gsmarena.com/vv/pics/oneplus/oneplus-12r-1.jpg",
    "OnePlus Nord 3": "https://fdn2.gsmarena.com/vv/pics/oneplus/oneplus-nord-3-5g-1.jpg",
    "Oppo Find X7 Ultra": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-find-x7-ultra-1.jpg",
    "Oppo Reno 12 Pro": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno12-pro-1.jpg",
    "Oppo A78": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-a78-5g-1.jpg",
    "Vivo X100 Pro": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-x100-pro-1.jpg",
    "Vivo V30 Pro": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v30-pro-1.jpg",
    "Vivo Y36": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-y36-1.jpg",
    "Realme GT 5 Pro": "https://fdn2.gsmarena.com/vv/pics/realme/realme-gt5-pro-1.jpg",
    "Realme 12 Pro+": "https://fdn2.gsmarena.com/vv/pics/realme/realme-12-pro-plus-1.jpg",
    "Realme C67": "https://fdn2.gsmarena.com/vv/pics/realme/realme-c67-1.jpg",
    "Redmi Note 13 Pro": "https://fdn2.gsmarena.com/vv/pics/xiaomi/redmi-note-13-pro-5g-1.jpg",
    "Redmi A3": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-a3-1.jpg",
    "Xiaomi 14 Ultra": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-14-ultra-1.jpg",
    "POCO F6 Pro": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-poco-f6-pro-1.jpg",
    "Pixel 8 Pro": "https://fdn2.gsmarena.com/vv/pics/google/google-pixel-8-pro-1.jpg",
    "Pixel 7a": "https://fdn2.gsmarena.com/vv/pics/google/google-pixel-7a-1.jpg",
    "Honor 200 Pro": "https://fdn2.gsmarena.com/vv/pics/honor/honor-200-pro-1.jpg",
    "Honor Magic 6 Pro": "https://fdn2.gsmarena.com/vv/pics/honor/honor-magic6-pro-1.jpg",
    "Sony Xperia 1 VI": "https://fdn2.gsmarena.com/vv/pics/sony/sony-xperia-1-vi-1.jpg",
    "ASUS ROG Phone 8 Pro": "https://fdn2.gsmarena.com/vv/pics/asus/asus-rog-phone-8-pro-1.jpg",
    "ASUS Zenfone 11 Ultra": "https://fdn2.gsmarena.com/vv/pics/asus/asus-zenfone-11-ultra-1.jpg",
    "Moto G84": "https://fdn2.gsmarena.com/vv/pics/motorola/motorola-moto-g84-5g-1.jpg",
    "Motorola Edge 50 Ultra": "https://fdn2.gsmarena.com/vv/pics/motorola/motorola-edge-50-ultra-2.jpg",
    "Nokia G60 5G": "https://fdn2.gsmarena.com/vv/pics/nokia/nokia-g60-5g-1.jpg",
    "Samsung Galaxy M36": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-m35-1.jpg",
    "Samsung Galaxy M35": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-m35-1.jpg",
    "Samsung Galaxy M34": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-m34-5g-1.jpg",
    "Samsung Galaxy M33": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-m33-5g-1.jpg",
    "Samsung Galaxy M32": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-m32-1.jpg",
    "Samsung Galaxy M31": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-m31-1.jpg",
    "Galaxy M55": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-m55-1.jpg",
    "Samsung Galaxy Note 20": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-note20-1.jpg",
    "Samsung Galaxy Note 10+": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-note10-plus-1.jpg",
    "Samsung Galaxy Note 10": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-note10-1.jpg",
    "Samsung Galaxy Note 9": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-note9-1.jpg",
    "Samsung Galaxy Note 8": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-note8-1.jpg",
}

def fix_other_brands():
    """Fix all other brand images"""
    token = os.getenv('ASTRA_TOKEN')
    api_endpoint = os.getenv('ASTRA_API_ENDPOINT')
    
    client = DataAPIClient(token)
    database = client.get_database(api_endpoint)
    collection = database.get_collection("products")
    
    products = list(collection.find({}))
    
    print(f"\n{'='*80}")
    print(f"FIXING ALL OTHER BRAND IMAGES")
    print(f"{'='*80}\n")
    
    updated = 0
    
    for product in products:
        name = product.get('name', '')
        product_id = product.get('_id')
        
        if name in OTHER_BRANDS_IMAGES:
            new_image = OTHER_BRANDS_IMAGES[name]
            collection.update_one(
                {"_id": product_id},
                {"$set": {"images": [new_image]}}
            )
            print(f"✓ {name}")
            updated += 1
    
    print(f"\n{'='*80}")
    print(f"✓ Updated {updated} products")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    fix_other_brands()
