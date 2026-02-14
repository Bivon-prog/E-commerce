import os
from astrapy import DataAPIClient
from dotenv import load_dotenv

load_dotenv()

# Images for remaining products
REMAINING_IMAGES = {
    # Samsung Galaxy (remaining)
    "Galaxy A55": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a55.jpg",
    "Galaxy M55": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-m55.jpg",
    "Galaxy S24": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-5g.jpg",
    "Galaxy S25 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-ultra-5g.jpg",
    "Galaxy Z Flip 6": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-flip6.jpg",
    "Galaxy Z Fold 6": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-fold6.jpg",
    "Samsung Galaxy S25 Plus": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-plus-5g.jpg",
    "Samsung Galaxy S25 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-ultra-5g.jpg",
    "Samsung Galaxy S23 Plus": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-plus-5g.jpg",
    "Samsung Galaxy A73": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a73-5g.jpg",
    "Samsung Galaxy A51": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a51.jpg",
    "Samsung Galaxy A36": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a35.jpg",
    "Samsung Galaxy A33": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a33-5g.jpg",
    "Samsung Galaxy A32": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a32.jpg",
    "Samsung Galaxy A31": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a31.jpg",
    "Samsung Galaxy A24": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a24-4g.jpg",
    "Samsung Galaxy A23": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a23.jpg",
    "Samsung Galaxy A22": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a22-5g.jpg",
    "Samsung Galaxy A17": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a15-5g.jpg",
    "Samsung Galaxy A16": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a15-5g.jpg",
    "Samsung Galaxy A13": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a13-5g.jpg",
    "Samsung Galaxy A11": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a11.jpg",
    "Samsung Galaxy A07": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a05.jpg",
    "Samsung Galaxy A06": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a05.jpg",
    "Samsung Galaxy A02": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a02.jpg",
    "Samsung Galaxy A01": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a01.jpg",
    "Samsung Galaxy M34": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-m34-5g.jpg",
    "Samsung Galaxy M33": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-m33-5g.jpg",
    "Samsung Galaxy M31": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-m31.jpg",
    "Samsung Galaxy Note 10": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-note10-5g.jpg",
    "Samsung Galaxy Note 8": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-note8-.jpg",
    "Samsung Galaxy Z Flip": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-flip.jpg",
    "Samsung Galaxy Z Flip 5G": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-flip-5g.jpg",
    "Samsung Galaxy Z Flip7": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-flip6.jpg",
    "Samsung Galaxy Z Fold2": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-fold2-5g.jpg",
    "Samsung Galaxy Z Fold3": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-fold3-5g.jpg",
    "Samsung Galaxy Z Fold7": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-fold6.jpg",
    "Samsung Tri-Fold": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-fold6.jpg",
    
    # Infinix (remaining)
    "Infinix Note 60 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-40-pro-5g.jpg",
    "Infinix Note 60": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-40-pro-5g.jpg",
    "Infinix Note 50 Pro+": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-40-pro-5g.jpg",
    "Infinix Note 50 Pro": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-40-pro-5g.jpg",
    "Infinix Note 40 Pro": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-40-pro-5g.jpg",
    "Infinix Note 40": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-40-pro-5g.jpg",
    "Infinix Note 30 Pro": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-30-pro.jpg",
    "Infinix Zero Flip": "https://fdn2.gsmarena.com/vv/bigpic/infinix-zero-flip.jpg",
    "Infinix Zero 40 4G": "https://fdn2.gsmarena.com/vv/bigpic/infinix-zero-40-5g.jpg",
    "Infinix Zero 30 5G": "https://fdn2.gsmarena.com/vv/bigpic/infinix-zero-30-5g.jpg",
    "Infinix Zero 30 4G": "https://fdn2.gsmarena.com/vv/bigpic/infinix-zero-30-4g.jpg",
    "Infinix GT 30 Pro": "https://fdn2.gsmarena.com/vv/bigpic/infinix-gt-20-pro.jpg",
    "Infinix GT 20 Pro": "https://fdn2.gsmarena.com/vv/bigpic/infinix-gt-20-pro.jpg",
    "Infinix Hot 60 Pro+": "https://fdn2.gsmarena.com/vv/bigpic/infinix-hot-40-pro.jpg",
    "Infinix Hot 60 Pro": "https://fdn2.gsmarena.com/vv/bigpic/infinix-hot-40-pro.jpg",
    "Infinix Hot 50 Pro+": "https://fdn2.gsmarena.com/vv/bigpic/infinix-hot-50-5g.jpg",
    "Infinix Hot 50i": "https://fdn2.gsmarena.com/vv/bigpic/infinix-hot-50-5g.jpg",
    "Infinix Hot 40 Pro": "https://fdn2.gsmarena.com/vv/bigpic/infinix-hot-40-pro.jpg",
    "Infinix Hot 40": "https://fdn2.gsmarena.com/vv/bigpic/infinix-hot-40.jpg",
    "Infinix Hot 40i": "https://fdn2.gsmarena.com/vv/bigpic/infinix-hot-40i.jpg",
    "Infinix Smart 10 HD": "https://fdn2.gsmarena.com/vv/bigpic/infinix-smart-8.jpg",
    "Infinix Smart 10": "https://fdn2.gsmarena.com/vv/bigpic/infinix-smart-8.jpg",
    "Infinix Smart 9": "https://fdn2.gsmarena.com/vv/bigpic/infinix-smart-8.jpg",
    "Infinix Smart 8 Plus": "https://fdn2.gsmarena.com/vv/bigpic/infinix-smart-8-plus.jpg",
    "Infinix Smart 8": "https://fdn2.gsmarena.com/vv/bigpic/infinix-smart-8.jpg",
    
    # Tecno (remaining)
    "Tecno Phantom V Fold 2 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-phantom-v-fold-5g.jpg",
    "Tecno Phantom V Fold": "https://fdn2.gsmarena.com/vv/bigpic/tecno-phantom-v-fold-5g.jpg",
    "Tecno Phantom X2 Pro 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-phantom-x2-pro-5g.jpg",
    "Tecno Camon 40 Pro 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-30-pro-5g.jpg",
    "Tecno Camon 40 Pro 4G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-30-pro-5g.jpg",
    "Tecno Camon 40 Premier 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-30-pro-5g.jpg",
    "Tecno Camon 30 Premier 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-30-premier-5g.jpg",
    "Tecno Camon 30 Pro 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-30-pro-5g.jpg",
    "Tecno Camon 30 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-30-5g.jpg",
    "Tecno Camon 20 Pro 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-20-pro-5g.jpg",
    "Tecno Camon 20 Pro": "https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-20-pro.jpg",
    "Tecno Camon 20": "https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-20.jpg",
    "Tecno Pova 7 Pro": "https://fdn2.gsmarena.com/vv/bigpic/tecno-pova-6-pro-5g.jpg",
    "Tecno Pova 6 Pro 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-pova-6-pro-5g.jpg",
    "Tecno Pova 6 Pro": "https://fdn2.gsmarena.com/vv/bigpic/tecno-pova-6-pro-5g.jpg",
    "Tecno Pova 6 Neo": "https://fdn2.gsmarena.com/vv/bigpic/tecno-pova-6-neo.jpg",
    "Tecno Pova 5 Pro": "https://fdn2.gsmarena.com/vv/bigpic/tecno-pova-5-pro-5g.jpg",
    "Tecno Pova 5": "https://fdn2.gsmarena.com/vv/bigpic/tecno-pova-5-5g.jpg",
    "Tecno Pova Slim 5G": "https://fdn2.gsmarena.com/vv/bigpic/tecno-pova-6-pro-5g.jpg",
    "Tecno Spark 40 Pro+": "https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-20-pro-plus.jpg",
    "Tecno Spark 40 Pro": "https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-20-pro-plus.jpg",
    "Tecno Spark 40": "https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-20-pro-plus.jpg",
    "Tecno Spark 40C": "https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-20c.jpg",
    "Tecno Spark 30": "https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-20-pro-plus.jpg",
    "Tecno Spark 30C": "https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-20c.jpg",
    "Tecno Spark 20 Pro+": "https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-20-pro-plus.jpg",
    "Tecno Spark 20 Pro": "https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-20-pro.jpg",
    "Tecno Spark 20": "https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-20.jpg",
    "Tecno Spark 20C": "https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-20c.jpg",
    "Tecno Pop 10 Pro": "https://fdn2.gsmarena.com/vv/bigpic/tecno-pop-8.jpg",
    "Tecno Pop 10": "https://fdn2.gsmarena.com/vv/bigpic/tecno-pop-8.jpg",
    "Tecno Pop 7": "https://fdn2.gsmarena.com/vv/bigpic/tecno-pop-7-pro.jpg",
    
    # itel (remaining)
    "itel S25 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/itel-s24.jpg",
    "itel S25": "https://fdn2.gsmarena.com/vv/bigpic/itel-s24.jpg",
    "itel S23+": "https://fdn2.gsmarena.com/vv/bigpic/itel-s23-plus.jpg",
    "itel P65": "https://fdn2.gsmarena.com/vv/bigpic/itel-p55-plus.jpg",
    "itel P55+": "https://fdn2.gsmarena.com/vv/bigpic/itel-p55-plus.jpg",
    "itel P55 5G": "https://fdn2.gsmarena.com/vv/bigpic/itel-p55-plus.jpg",
    "itel P40+": "https://fdn2.gsmarena.com/vv/bigpic/itel-p40-plus.jpg",
    "itel A80": "https://fdn2.gsmarena.com/vv/bigpic/itel-a60s.jpg",
    "itel A70": "https://fdn2.gsmarena.com/vv/bigpic/itel-a60s.jpg",
    "itel A60s": "https://fdn2.gsmarena.com/vv/bigpic/itel-a60s.jpg",
    "itel A60": "https://fdn2.gsmarena.com/vv/bigpic/itel-a60.jpg",
    
    # Other brands
    "OnePlus 12": "https://fdn2.gsmarena.com/vv/bigpic/oneplus-12.jpg",
    "OnePlus Nord 3": "https://fdn2.gsmarena.com/vv/bigpic/oneplus-nord-3-5g.jpg",
    "Oppo Find X7 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/oppo-find-x7-ultra.jpg",
    "Oppo Reno 12 Pro": "https://fdn2.gsmarena.com/vv/bigpic/oppo-reno12-pro-5g-global.jpg",
    "Oppo A78": "https://fdn2.gsmarena.com/vv/bigpic/oppo-a78-5g.jpg",
    "Vivo V30 Pro": "https://fdn2.gsmarena.com/vv/bigpic/vivo-v30-pro-5g.jpg",
    "Realme GT 5 Pro": "https://fdn2.gsmarena.com/vv/bigpic/realme-gt5-pro.jpg",
    "Realme C67": "https://fdn2.gsmarena.com/vv/bigpic/realme-c67-5g.jpg",
    "Redmi Note 13 Pro": "https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-13-pro-5g.jpg",
    "Xiaomi 14 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/xiaomi-14-ultra.jpg",
    "Pixel 8 Pro": "https://fdn2.gsmarena.com/vv/bigpic/google-pixel-8-pro.jpg",
    "Pixel 7a": "https://fdn2.gsmarena.com/vv/bigpic/google-pixel-7a.jpg",
    "Honor 200 Pro": "https://fdn2.gsmarena.com/vv/bigpic/honor-200-pro.jpg",
    "Honor Magic 6 Pro": "https://fdn2.gsmarena.com/vv/bigpic/honor-magic6-pro.jpg",
    "Sony Xperia 1 VI": "https://fdn2.gsmarena.com/vv/bigpic/sony-xperia-1-vi.jpg",
    "ASUS ROG Phone 8 Pro": "https://fdn2.gsmarena.com/vv/bigpic/asus-rog-phone-8-pro.jpg",
    "Moto G84": "https://fdn2.gsmarena.com/vv/bigpic/motorola-moto-g84-5g.jpg",
    "Nokia G60 5G": "https://fdn2.gsmarena.com/vv/bigpic/nokia-g60-5g.jpg",
}

def add_remaining():
    """Add images for remaining products"""
    token = os.getenv('ASTRA_TOKEN')
    api_endpoint = os.getenv('ASTRA_API_ENDPOINT')
    
    client = DataAPIClient(token)
    database = client.get_database(api_endpoint)
    collection = database.get_collection("products")
    
    products = list(collection.find({}))
    
    print(f"\n{'='*80}")
    print(f"ADDING REMAINING PRODUCT IMAGES")
    print(f"{'='*80}\n")
    
    updated = 0
    
    for product in products:
        name = product.get('name', '')
        product_id = product.get('_id')
        
        if name in REMAINING_IMAGES:
            new_image = REMAINING_IMAGES[name]
            collection.update_one(
                {"_id": product_id},
                {"$set": {"images": [new_image]}}
            )
            print(f"✓ Updated: {name}")
            updated += 1
    
    print(f"\n{'='*80}")
    print(f"✓ Updated {updated} more products")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    add_remaining()
