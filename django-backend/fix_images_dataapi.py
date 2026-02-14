import os
from astrapy import DataAPIClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Comprehensive image database
PHONE_IMAGES = {
    # Apple iPhones
    "iPhone 16 Pro Max": "https://www.apple.com/newsroom/images/2024/09/apple-debuts-iphone-16-pro-and-iphone-16-pro-max/article/Apple-iPhone-16-Pro-lineup-hero-geo-240909_inline.jpg.large.jpg",
    "iPhone 16 Pro": "https://www.apple.com/newsroom/images/2024/09/apple-debuts-iphone-16-pro-and-iphone-16-pro-max/article/Apple-iPhone-16-Pro-lineup-hero-geo-240909_inline.jpg.large.jpg",
    "iPhone 16 Plus": "https://www.apple.com/newsroom/images/2024/09/apple-introduces-iphone-16-and-iphone-16-plus/article/Apple-iPhone-16-hero-geo-240909_inline.jpg.large.jpg",
    "iPhone 16": "https://www.apple.com/newsroom/images/2024/09/apple-introduces-iphone-16-and-iphone-16-plus/article/Apple-iPhone-16-hero-geo-240909_inline.jpg.large.jpg",
    "iPhone 15 Pro Max": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple-iPhone-15-Pro-lineup-hero-230912_Full-Bleed-Image.jpg.large.jpg",
    "iPhone 15 Pro": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple-iPhone-15-Pro-lineup-hero-230912_Full-Bleed-Image.jpg.large.jpg",
    "iPhone 15 Plus": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple-iPhone-15-lineup-color-lineup-230912_Full-Bleed-Image.jpg.large.jpg",
    "iPhone 15": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple-iPhone-15-lineup-color-lineup-230912_Full-Bleed-Image.jpg.large.jpg",
    "iPhone 14 Pro Max": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple_iPhone-14-Pro-iPhone-14-Pro-Max-hero-220907_Full-Bleed-Image.jpg.large.jpg",
    "iPhone 14 Pro": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple_iPhone-14-Pro-iPhone-14-Pro-Max-hero-220907_Full-Bleed-Image.jpg.large.jpg",
    "iPhone 14 Plus": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple_announce-iphone14-iphone14plus_09072022_big.jpg.large.jpg",
    "iPhone 14": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple_announce-iphone14-iphone14plus_09072022_big.jpg.large.jpg",
    "iPhone 13 Pro Max": "https://www.apple.com/newsroom/images/product/iphone/standard/apple_iphone-13-pro_09142021_big.jpg.large.jpg",
    "iPhone 13 Pro": "https://www.apple.com/newsroom/images/product/iphone/standard/apple_iphone-13-pro_09142021_big.jpg.large.jpg",
    "iPhone 13": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple_iphone13_hero_09142021_big.jpg.large.jpg",
    "iPhone 13 Mini": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple_iphone13_hero_09142021_big.jpg.large.jpg",
    "iPhone 12 Pro Max": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple_announce-iphone12pro_10132020_big.jpg.large.jpg",
    "iPhone 12 Pro": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple_announce-iphone12pro_10132020_big.jpg.large.jpg",
    "iPhone 12": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple_announce-iphone12_10132020_big.jpg.large.jpg",
    "iPhone 12 Mini": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple_announce-iphone12_10132020_big.jpg.large.jpg",
    "iPhone SE (2022)": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple_iphone-se_03082022_big.jpg.large.jpg",
    "iPhone 11 Pro Max": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-11-pro.jpg",
    "iPhone 11 Pro": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-11-pro.jpg",
    "iPhone 11": "https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-11.jpg",
    
    # Samsung Galaxy
    "Samsung Galaxy S24 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-ultra-5g.jpg",
    "Samsung Galaxy S24+": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-plus-5g.jpg",
    "Samsung Galaxy S24": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-5g.jpg",
    "Samsung Galaxy S23 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-ultra-5g.jpg",
    "Samsung Galaxy S23+": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-plus-5g.jpg",
    "Samsung Galaxy S23": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-5g.jpg",
    "Samsung Galaxy S23 FE": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-fe.jpg",
    "Samsung Galaxy Z Fold6": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-fold6.jpg",
    "Samsung Galaxy Z Flip6": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-flip6.jpg",
    "Samsung Galaxy A55": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a55.jpg",
    "Samsung Galaxy A54": "https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a54.jpg",
    
    # OPPO
    "OPPO Find X7 Ultra": "https://fdn2.gsmarena.com/vv/bigpic/oppo-find-x7-ultra.jpg",
    "OPPO Reno12 Pro": "https://fdn2.gsmarena.com/vv/bigpic/oppo-reno12-pro-5g-global.jpg",
    "OPPO Reno12": "https://fdn2.gsmarena.com/vv/bigpic/oppo-reno12-5g-global.jpg",
    "OPPO Reno11 Pro": "https://fdn2.gsmarena.com/vv/bigpic/oppo-reno11-pro-5g-global.jpg",
    "OPPO A79": "https://fdn2.gsmarena.com/vv/bigpic/oppo-a79-5g.jpg",
    "OPPO A78": "https://fdn2.gsmarena.com/vv/bigpic/oppo-a78-5g.jpg",
    
    # vivo
    "vivo X100 Pro": "https://fdn2.gsmarena.com/vv/bigpic/vivo-x100-pro.jpg",
    "vivo X100": "https://fdn2.gsmarena.com/vv/bigpic/vivo-x100-r1.jpg",
    "vivo V30 Pro": "https://fdn2.gsmarena.com/vv/bigpic/vivo-v30-pro-5g.jpg",
    "vivo V30": "https://fdn2.gsmarena.com/vv/bigpic/vivo-v30-5g.jpg",
    "vivo Y200": "https://fdn2.gsmarena.com/vv/bigpic/vivo-y200-5g.jpg",
    "vivo Y100": "https://fdn2.gsmarena.com/vv/bigpic/vivo-y100-5g.jpg",
    
    # OnePlus
    "OnePlus 12": "https://fdn2.gsmarena.com/vv/bigpic/oneplus-12.jpg",
    "OnePlus 12R": "https://fdn2.gsmarena.com/vv/bigpic/oneplus-12r.jpg",
    "OnePlus 11": "https://fdn2.gsmarena.com/vv/bigpic/oneplus-11-5g.jpg",
    "OnePlus Nord 4": "https://fdn2.gsmarena.com/vv/bigpic/oneplus-nord-4.jpg",
    "OnePlus Nord 3": "https://fdn2.gsmarena.com/vv/bigpic/oneplus-nord-3-5g.jpg",
    
    # Realme
    "Realme GT 6": "https://fdn2.gsmarena.com/vv/bigpic/realme-gt-6.jpg",
    "Realme 13 Pro+": "https://fdn2.gsmarena.com/vv/bigpic/realme-13-pro-plus-5g.jpg",
    "Realme 12 Pro+": "https://fdn2.gsmarena.com/vv/bigpic/realme-12-pro-plus-5g.jpg",
    "Realme C67": "https://fdn2.gsmarena.com/vv/bigpic/realme-c67-5g.jpg",
    
    # iQOO
    "iQOO 12": "https://fdn2.gsmarena.com/vv/bigpic/iqoo-12.jpg",
    "iQOO Neo9 Pro": "https://fdn2.gsmarena.com/vv/bigpic/iqoo-neo9-pro.jpg",
    "iQOO Z9": "https://fdn2.gsmarena.com/vv/bigpic/iqoo-z9-5g.jpg",
    
    # Transsion
    "Tecno Phantom X2 Pro": "https://fdn2.gsmarena.com/vv/bigpic/tecno-phantom-x2-pro-5g.jpg",
    "Infinix Note 40 Pro": "https://fdn2.gsmarena.com/vv/bigpic/infinix-note-40-pro-5g.jpg",
}

def connect_to_astra():
    """Connect to Astra DB using Data API"""
    token = os.getenv('ASTRA_TOKEN')
    api_endpoint = os.getenv('ASTRA_API_ENDPOINT')
    
    client = DataAPIClient(token)
    database = client.get_database(api_endpoint)
    collection = database.get_collection("products")
    
    print(f"✓ Connected to Astra DB")
    return collection

def fix_all_images():
    """Fix all phone images"""
    collection = connect_to_astra()
    
    print("\n" + "="*60)
    print("FIXING ALL PHONE IMAGES - FINAL UPDATE")
    print("="*60 + "\n")
    
    # Get all products
    products = list(collection.find({}))
    print(f"Found {len(products)} products in database\n")
    
    updated_count = 0
    missing_count = 0
    skipped_count = 0
    
    for product in products:
        product_name = product.get('name', '')
        product_id = product.get('_id')
        images = product.get('images', [])
        
        # Check if needs update
        needs_update = False
        reason = ""
        
        if not images or len(images) == 0:
            needs_update = True
            reason = "No images"
        elif 'placeholder' in str(images[0]).lower():
            needs_update = True
            reason = "Placeholder image"
        elif 'via.placeholder.com' in str(images[0]):
            needs_update = True
            reason = "Placeholder URL"
        
        if needs_update:
            # Find matching image
            found_image = None
            
            # Exact match
            if product_name in PHONE_IMAGES:
                found_image = PHONE_IMAGES[product_name]
            else:
                # Partial match
                for key, value in PHONE_IMAGES.items():
                    if key.lower() in product_name.lower() or product_name.lower() in key.lower():
                        found_image = value
                        break
            
            if found_image:
                # Update product
                collection.update_one(
                    {"_id": product_id},
                    {"$set": {"images": [found_image]}}
                )
                print(f"✓ Updated: {product_name} ({reason})")
                updated_count += 1
            else:
                print(f"✗ Missing: {product_name} - No image found")
                missing_count += 1
        else:
            skipped_count += 1
    
    print("\n" + "="*60)
    print("IMAGE UPDATE SUMMARY")
    print("="*60)
    print(f"Total products: {len(products)}")
    print(f"✓ Updated: {updated_count}")
    print(f"✗ Missing images: {missing_count}")
    print(f"→ Skipped (already have images): {skipped_count}")
    print("="*60 + "\n")

if __name__ == "__main__":
    fix_all_images()
