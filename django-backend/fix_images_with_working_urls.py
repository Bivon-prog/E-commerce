import os
from astrapy import DataAPIClient
from dotenv import load_dotenv

load_dotenv()

# Working image URLs from GSMarena's pics directory (not bigpic)
WORKING_IMAGES = {
    # Apple iPhones
    "iPhone 16 Pro Max": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-16-pro-max-1.jpg",
    "iPhone 16 Pro": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-16-pro-1.jpg",
    "iPhone 16 Plus": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-16-plus-1.jpg",
    "iPhone 16": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-16-1.jpg",
    "iPhone 15 Pro Max": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-pro-max-1.jpg",
    "iPhone 15 Pro": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-pro-1.jpg",
    "iPhone 15 Plus": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-plus-1.jpg",
    "iPhone 15": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-1.jpg",
    "iPhone 14 Pro Max": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-pro-max-1.jpg",
    "iPhone 14 Pro": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-pro-1.jpg",
    "iPhone 14 Plus": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-plus-1.jpg",
    "iPhone 14": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-1.jpg",
    "iPhone 13 Pro Max": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-pro-max-1.jpg",
    "iPhone 13 Pro": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-pro-1.jpg",
    "iPhone 13": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-1.jpg",
    "iPhone 13 mini": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-mini-1.jpg",
    "iPhone 12 Pro Max": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-12-pro-max-1.jpg",
    "iPhone 12 Pro": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-12-pro-1.jpg",
    "iPhone 12": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-12-1.jpg",
    "iPhone 12 Mini": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-12-mini-1.jpg",
    "iPhone SE (2022)": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-se-2022-1.jpg",
    "iPhone 11 Pro Max": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-11-pro-max-1.jpg",
    "iPhone 11 Pro": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-11-pro-1.jpg",
    "iPhone 11": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-11-1.jpg",
    "iPhone X": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-x-new-1.jpg",
    
    # Samsung Galaxy S Series
    "Samsung Galaxy S25": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-ultra-5g-1.jpg",
    "Samsung Galaxy S25 Edge": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-ultra-5g-1.jpg",
    "Samsung Galaxy S25 Plus": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-plus-5g-1.jpg",
    "Samsung Galaxy S25 Ultra": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-ultra-5g-1.jpg",
    "Galaxy S25 Ultra": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-ultra-5g-1.jpg",
    "Samsung Galaxy S24 Ultra": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-ultra-5g-1.jpg",
    "Galaxy S24 Ultra": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-ultra-5g-1.jpg",
    "Samsung Galaxy S24+": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-plus-5g-1.jpg",
    "Samsung Galaxy S24": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-5g-1.jpg",
    "Galaxy S24": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-5g-1.jpg",
    "Samsung Galaxy S23 Ultra": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s23-ultra-5g-1.jpg",
    "Samsung Galaxy S23 Plus": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s23-plus-5g-1.jpg",
    "Samsung Galaxy S23+": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s23-plus-5g-1.jpg",
    "Samsung Galaxy S23": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s23-5g-1.jpg",
    "Samsung Galaxy S23 FE": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s23-fe-1.jpg",
    "Samsung Galaxy S22 Ultra": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s22-ultra-5g-1.jpg",
    "Samsung Galaxy S22+": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s22-plus-5g-1.jpg",
    "Samsung Galaxy S22": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s22-5g-1.jpg",
    "Samsung Galaxy S21": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s21-5g-1.jpg",
    "Samsung Galaxy S21+": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s21-plus-5g-1.jpg",
    "Samsung Galaxy S21 Ultra": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s21-ultra-5g-1.jpg",
    "Samsung Galaxy S21 FE": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s21-fe-5g-1.jpg",
    
    # Samsung Galaxy Z Series
    "Samsung Galaxy Z Fold6": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-fold6-1.jpg",
    "Galaxy Z Fold 6": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-fold6-1.jpg",
    "Samsung Galaxy Z Flip6": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-flip6-1.jpg",
    "Galaxy Z Flip 6": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-flip6-1.jpg",
    "Samsung Galaxy Z Fold5": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-fold5-1.jpg",
    "Samsung Galaxy Z Flip5": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-flip5-5g-1.jpg",
    "Samsung Galaxy Z Fold4": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-fold4-5g-1.jpg",
    "Samsung Galaxy Z Flip4": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-flip4-5g-1.jpg",
    "Samsung Galaxy Z Flip3": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-flip3-5g-1.jpg",
    "Samsung Galaxy Z Fold3": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-fold3-5g-1.jpg",
    "Samsung Galaxy Z Fold2": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-fold2-5g-1.jpg",
    "Samsung Galaxy Z Flip": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-flip-1.jpg",
    "Samsung Galaxy Z Flip 5G": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-flip-5g-1.jpg",
    "Samsung Galaxy Z Flip7": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-flip6-1.jpg",
    "Samsung Galaxy Z Fold7": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-fold6-1.jpg",
    "Samsung Galaxy Fold": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-fold-1.jpg",
    "Samsung Tri-Fold": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-fold6-1.jpg",
    
    # Samsung Galaxy A Series
    "Samsung Galaxy A55": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a55-1.jpg",
    "Galaxy A55": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a55-1.jpg",
    "Samsung Galaxy A56": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a55-1.jpg",
    "Samsung Galaxy A54": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a54-1.jpg",
    "Samsung Galaxy A53": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a53-5g-1.jpg",
    "Samsung Galaxy A52": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a52-5g-1.jpg",
    "Samsung Galaxy A51": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a51-1.jpg",
    "Samsung Galaxy A35": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a35-1.jpg",
    "Samsung Galaxy A36": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a35-1.jpg",
    "Samsung Galaxy A34": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a34-1.jpg",
    "Galaxy A34": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a34-1.jpg",
    "Samsung Galaxy A33": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a33-5g-1.jpg",
    "Samsung Galaxy A32": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a32-1.jpg",
    "Samsung Galaxy A31": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a31-1.jpg",
    "Samsung Galaxy A26": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a25-1.jpg",
    "Samsung Galaxy A25": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a25-1.jpg",
    "Samsung Galaxy A24": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a24-4g-1.jpg",
    "Samsung Galaxy A23": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a23-1.jpg",
    "Samsung Galaxy A22": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a22-5g-1.jpg",
    "Samsung Galaxy A21": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a21s-1.jpg",
    "Samsung Galaxy A17": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a15-5g-1.jpg",
    "Samsung Galaxy A16": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a15-5g-1.jpg",
    "Samsung Galaxy A15": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a15-5g-1.jpg",
    "Samsung Galaxy A14": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a14-5g-1.jpg",
    "Samsung Galaxy A13": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a13-5g-1.jpg",
    "Samsung Galaxy A12": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a12-nacho-1.jpg",
    "Samsung Galaxy A11": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a11-1.jpg",
    "Samsung Galaxy A07": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a05-1.jpg",
    "Samsung Galaxy A06": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a05-1.jpg",
    "Samsung Galaxy A05": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a05-1.jpg",
    "Samsung Galaxy A04": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a04-1.jpg",
    "Samsung Galaxy A03": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a03-1.jpg",
    "Samsung Galaxy A02": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a02-1.jpg",
    "Samsung Galaxy A01": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a01-1.jpg",
    "Samsung Galaxy A71": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a71-5g-1.jpg",
    "Samsung Galaxy A72": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a72-1.jpg",
    "Samsung Galaxy A73": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a73-5g-1.jpg",
}

def fix_all_images():
    """Fix all images with working URLs"""
    token = os.getenv('ASTRA_TOKEN')
    api_endpoint = os.getenv('ASTRA_API_ENDPOINT')
    
    client = DataAPIClient(token)
    database = client.get_database(api_endpoint)
    collection = database.get_collection("products")
    
    products = list(collection.find({}))
    
    print(f"\n{'='*80}")
    print(f"FIXING ALL IMAGES WITH WORKING URLs")
    print(f"{'='*80}\n")
    
    updated = 0
    
    for product in products:
        name = product.get('name', '')
        product_id = product.get('_id')
        
        if name in WORKING_IMAGES:
            new_image = WORKING_IMAGES[name]
            collection.update_one(
                {"_id": product_id},
                {"$set": {"images": [new_image]}}
            )
            print(f"✓ {name}")
            updated += 1
    
    print(f"\n{'='*80}")
    print(f"✓ Updated {updated} products with working image URLs")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    fix_all_images()
