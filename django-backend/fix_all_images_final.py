import os
import django
from cassandra.cqlengine import connection
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from products.astra_models import Product

# Connect to Astra DB
def connect_to_astra():
    ASTRA_DB_ID = os.getenv('ASTRA_DB_ID')
    ASTRA_DB_REGION = os.getenv('ASTRA_DB_REGION')
    ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')
    ASTRA_DB_TOKEN = os.getenv('ASTRA_DB_APPLICATION_TOKEN')
    
    SECURE_CONNECT_BUNDLE = f'secure-connect-{ASTRA_DB_ID}.zip'
    
    cloud_config = {'secure_connect_bundle': SECURE_CONNECT_BUNDLE}
    auth_provider = PlainTextAuthProvider('token', ASTRA_DB_TOKEN)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    
    connection.register_connection('default', session=session, default=True)
    connection.set_default_connection('default')
    
    print(f"✓ Connected to Astra DB: {ASTRA_DB_KEYSPACE}")
    return session

# Comprehensive image database with high-quality official images
PHONE_IMAGES = {
    # Apple iPhones
    "iPhone 16 Pro Max": ["https://www.apple.com/newsroom/images/2024/09/apple-debuts-iphone-16-pro-and-iphone-16-pro-max/article/Apple-iPhone-16-Pro-lineup-hero-geo-240909_inline.jpg.large.jpg"],
    "iPhone 16 Pro": ["https://www.apple.com/newsroom/images/2024/09/apple-debuts-iphone-16-pro-and-iphone-16-pro-max/article/Apple-iPhone-16-Pro-lineup-hero-geo-240909_inline.jpg.large.jpg"],
    "iPhone 16 Plus": ["https://www.apple.com/newsroom/images/2024/09/apple-introduces-iphone-16-and-iphone-16-plus/article/Apple-iPhone-16-hero-geo-240909_inline.jpg.large.jpg"],
    "iPhone 16": ["https://www.apple.com/newsroom/images/2024/09/apple-introduces-iphone-16-and-iphone-16-plus/article/Apple-iPhone-16-hero-geo-240909_inline.jpg.large.jpg"],
    "iPhone 15 Pro Max": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple-iPhone-15-Pro-lineup-hero-230912_Full-Bleed-Image.jpg.large.jpg"],
    "iPhone 15 Pro": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple-iPhone-15-Pro-lineup-hero-230912_Full-Bleed-Image.jpg.large.jpg"],
    "iPhone 15 Plus": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple-iPhone-15-lineup-color-lineup-230912_Full-Bleed-Image.jpg.large.jpg"],
    "iPhone 15": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple-iPhone-15-lineup-color-lineup-230912_Full-Bleed-Image.jpg.large.jpg"],
    "iPhone 14 Pro Max": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple_iPhone-14-Pro-iPhone-14-Pro-Max-hero-220907_Full-Bleed-Image.jpg.large.jpg"],
    "iPhone 14 Pro": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple_iPhone-14-Pro-iPhone-14-Pro-Max-hero-220907_Full-Bleed-Image.jpg.large.jpg"],
    "iPhone 14 Plus": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple_announce-iphone14-iphone14plus_09072022_big.jpg.large.jpg"],
    "iPhone 14": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple_announce-iphone14-iphone14plus_09072022_big.jpg.large.jpg"],
    "iPhone 13 Pro Max": ["https://www.apple.com/newsroom/images/product/iphone/standard/apple_iphone-13-pro_09142021_big.jpg.large.jpg"],
    "iPhone 13 Pro": ["https://www.apple.com/newsroom/images/product/iphone/standard/apple_iphone-13-pro_09142021_big.jpg.large.jpg"],
    "iPhone 13": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple_iphone13_hero_09142021_big.jpg.large.jpg"],
    "iPhone 13 Mini": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple_iphone13_hero_09142021_big.jpg.large.jpg"],
    "iPhone 12 Pro Max": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple_announce-iphone12pro_10132020_big.jpg.large.jpg"],
    "iPhone 12 Pro": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple_announce-iphone12pro_10132020_big.jpg.large.jpg"],
    "iPhone 12": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple_announce-iphone12_10132020_big.jpg.large.jpg"],
    "iPhone 12 Mini": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple_announce-iphone12_10132020_big.jpg.large.jpg"],
    "iPhone SE (2022)": ["https://www.apple.com/newsroom/images/product/iphone/standard/Apple_iphone-se_03082022_big.jpg.large.jpg"],
    "iPhone 11 Pro Max": ["https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-11-pro.jpg"],
    "iPhone 11 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-11-pro.jpg"],
    "iPhone 11": ["https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-11.jpg"],
    
    # Samsung Galaxy S Series
    "Samsung Galaxy S24 Ultra": ["https://images.samsung.com/is/image/samsung/p6pim/za/2401/gallery/za-galaxy-s24-s928-sm-s928bzkfafa-thumb-539573205"],
    "Samsung Galaxy S24+": ["https://images.samsung.com/is/image/samsung/p6pim/za/2401/gallery/za-galaxy-s24-s926-sm-s926blbfafa-thumb-539573161"],
    "Samsung Galaxy S24": ["https://images.samsung.com/is/image/samsung/p6pim/za/2401/gallery/za-galaxy-s24-s921-sm-s921blbfafa-thumb-539573117"],
    "Samsung Galaxy S23 Ultra": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-ultra-5g.jpg"],
    "Samsung Galaxy S23+": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-plus-5g.jpg"],
    "Samsung Galaxy S23": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-5g.jpg"],
    "Samsung Galaxy S23 FE": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-fe.jpg"],
    "Samsung Galaxy S22 Ultra": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s22-ultra-5g.jpg"],
    "Samsung Galaxy S22+": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s22-plus-5g.jpg"],
    "Samsung Galaxy S22": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s22-5g.jpg"],
    "Samsung Galaxy S21 Ultra": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s21-ultra-5g.jpg"],
    "Samsung Galaxy S21+": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s21-plus-5g.jpg"],
    "Samsung Galaxy S21": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s21-5g.jpg"],
    "Samsung Galaxy S21 FE": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s21-fe-5g.jpg"],
    
    # Samsung Galaxy Z Series
    "Samsung Galaxy Z Fold6": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-fold6.jpg"],
    "Samsung Galaxy Z Flip6": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-flip6.jpg"],
    "Samsung Galaxy Z Fold5": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-fold5.jpg"],
    "Samsung Galaxy Z Flip5": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-flip5-5g.jpg"],
    "Samsung Galaxy Z Fold4": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-fold4-5g.jpg"],
    "Samsung Galaxy Z Flip4": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-flip4-5g.jpg"],
    
    # Samsung Galaxy A Series
    "Samsung Galaxy A55": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a55.jpg"],
    "Samsung Galaxy A54": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a54.jpg"],
    "Samsung Galaxy A35": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a35.jpg"],
    "Samsung Galaxy A34": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a34.jpg"],
    "Samsung Galaxy A25": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a25.jpg"],
    "Samsung Galaxy A15": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a15-5g.jpg"],
    "Samsung Galaxy A05": ["https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a05.jpg"],
    
    # OPPO Find Series
    "OPPO Find X7 Ultra": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-find-x7-ultra.jpg"],
    "OPPO Find X7": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-find-x7.jpg"],
    "OPPO Find X6 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-find-x6-pro.jpg"],
    "OPPO Find X5 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-find-x5-pro.jpg"],
    "OPPO Find N3": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-find-n3.jpg"],
    "OPPO Find N3 Flip": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-find-n3-flip.jpg"],
    
    # OPPO Reno Series
    "OPPO Reno12 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-reno12-pro-5g-global.jpg"],
    "OPPO Reno12": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-reno12-5g-global.jpg"],
    "OPPO Reno11 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-reno11-pro-5g-global.jpg"],
    "OPPO Reno11": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-reno11-5g-global.jpg"],
    "OPPO Reno10 Pro+": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-reno10-pro-plus-5g.jpg"],
    "OPPO Reno10 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-reno10-pro-5g.jpg"],
    "OPPO Reno10": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-reno10-5g.jpg"],
    "OPPO Reno8 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-reno8-pro-5g.jpg"],
    "OPPO Reno8": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-reno8-5g.jpg"],
    
    # OPPO A Series
    "OPPO A3 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-a3-pro-5g.jpg"],
    "OPPO A79": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-a79-5g.jpg"],
    "OPPO A78": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-a78-5g.jpg"],
    "OPPO A58": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-a58-5g.jpg"],
    "OPPO A38": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-a38.jpg"],
    "OPPO A18": ["https://fdn2.gsmarena.com/vv/bigpic/oppo-a18.jpg"],
    
    # vivo X Series
    "vivo X100 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-x100-pro.jpg"],
    "vivo X100": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-x100-r1.jpg"],
    "vivo X90 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-x90-pro.jpg"],
    "vivo X90": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-x90-5g.jpg"],
    "vivo X Fold3 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-x-fold3-pro.jpg"],
    "vivo X Flip": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-x-flip.jpg"],
    
    # vivo V Series
    "vivo V30 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-v30-pro-5g.jpg"],
    "vivo V30": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-v30-5g.jpg"],
    "vivo V29 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-v29-pro-5g.jpg"],
    "vivo V29": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-v29-5g.jpg"],
    "vivo V27 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-v27-pro.jpg"],
    "vivo V27": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-v27-5g.jpg"],
    
    # vivo Y Series
    "vivo Y200 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-y200-pro.jpg"],
    "vivo Y200": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-y200-5g.jpg"],
    "vivo Y100": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-y100-5g.jpg"],
    "vivo Y78": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-y78-5g.jpg"],
    "vivo Y56": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-y56-5g.jpg"],
    "vivo Y36": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-y36.jpg"],
    "vivo Y28": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-y28-5g.jpg"],
    "vivo Y18": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-y18.jpg"],
    
    # OnePlus Flagship
    "OnePlus 12": ["https://fdn2.gsmarena.com/vv/bigpic/oneplus-12.jpg"],
    "OnePlus 12R": ["https://fdn2.gsmarena.com/vv/bigpic/oneplus-12r.jpg"],
    "OnePlus 11": ["https://fdn2.gsmarena.com/vv/bigpic/oneplus-11-5g.jpg"],
    "OnePlus 11R": ["https://fdn2.gsmarena.com/vv/bigpic/oneplus-11r-5g.jpg"],
    "OnePlus 10 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/oneplus-10-pro-5g.jpg"],
    "OnePlus 10T": ["https://fdn2.gsmarena.com/vv/bigpic/oneplus-10t-5g.jpg"],
    "OnePlus 9 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/oneplus-9-pro-.jpg"],
    "OnePlus 9": ["https://fdn2.gsmarena.com/vv/bigpic/oneplus-9-5g.jpg"],
    "OnePlus Open": ["https://fdn2.gsmarena.com/vv/bigpic/oneplus-open.jpg"],
    
    # OnePlus Nord Series
    "OnePlus Nord 4": ["https://fdn2.gsmarena.com/vv/bigpic/oneplus-nord-4.jpg"],
    "OnePlus Nord 3": ["https://fdn2.gsmarena.com/vv/bigpic/oneplus-nord-3-5g.jpg"],
    "OnePlus Nord CE4": ["https://fdn2.gsmarena.com/vv/bigpic/oneplus-nord-ce4.jpg"],
    "OnePlus Nord CE3": ["https://fdn2.gsmarena.com/vv/bigpic/oneplus-nord-ce-3-5g.jpg"],
    "OnePlus Nord N30": ["https://fdn2.gsmarena.com/vv/bigpic/oneplus-nord-n30-5g.jpg"],
    
    # Realme GT Series
    "Realme GT 6": ["https://fdn2.gsmarena.com/vv/bigpic/realme-gt-6.jpg"],
    "Realme GT 5 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/realme-gt5-pro.jpg"],
    "Realme GT 5": ["https://fdn2.gsmarena.com/vv/bigpic/realme-gt5.jpg"],
    "Realme GT Neo6": ["https://fdn2.gsmarena.com/vv/bigpic/realme-gt-neo6.jpg"],
    "Realme GT Neo5": ["https://fdn2.gsmarena.com/vv/bigpic/realme-gt-neo-5.jpg"],
    "Realme GT 3": ["https://fdn2.gsmarena.com/vv/bigpic/realme-gt3-240w.jpg"],
    "Realme GT 2 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/realme-gt2-pro-5g.jpg"],
    
    # Realme Number Series
    "Realme 13 Pro+": ["https://fdn2.gsmarena.com/vv/bigpic/realme-13-pro-plus-5g.jpg"],
    "Realme 13 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/realme-13-pro-5g.jpg"],
    "Realme 12 Pro+": ["https://fdn2.gsmarena.com/vv/bigpic/realme-12-pro-plus-5g.jpg"],
    "Realme 12 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/realme-12-pro-5g.jpg"],
    "Realme 12": ["https://fdn2.gsmarena.com/vv/bigpic/realme-12-5g.jpg"],
    "Realme 11 Pro+": ["https://fdn2.gsmarena.com/vv/bigpic/realme-11-pro-plus-5g.jpg"],
    "Realme 11 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/realme-11-pro-5g.jpg"],
    
    # Realme C Series
    "Realme C67": ["https://fdn2.gsmarena.com/vv/bigpic/realme-c67-5g.jpg"],
    "Realme C65": ["https://fdn2.gsmarena.com/vv/bigpic/realme-c65.jpg"],
    "Realme C55": ["https://fdn2.gsmarena.com/vv/bigpic/realme-c55.jpg"],
    "Realme C53": ["https://fdn2.gsmarena.com/vv/bigpic/realme-c53.jpg"],
    "Realme C35": ["https://fdn2.gsmarena.com/vv/bigpic/realme-c35.jpg"],
    
    # iQOO Flagship
    "iQOO 12": ["https://fdn2.gsmarena.com/vv/bigpic/iqoo-12.jpg"],
    "iQOO 12 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/iqoo-12-pro.jpg"],
    "iQOO 11": ["https://fdn2.gsmarena.com/vv/bigpic/iqoo-11-5g.jpg"],
    "iQOO 11 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-iqoo-11-pro.jpg"],
    "iQOO 10 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-iqoo-10-pro.jpg"],
    "iQOO 9 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/vivo-iqoo-9-pro.jpg"],
    
    # iQOO Neo Series
    "iQOO Neo9 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/iqoo-neo9-pro.jpg"],
    "iQOO Neo9": ["https://fdn2.gsmarena.com/vv/bigpic/iqoo-neo9.jpg"],
    "iQOO Neo8 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/iqoo-neo8-pro.jpg"],
    "iQOO Neo7 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/iqoo-neo7-pro.jpg"],
    
    # iQOO Z Series
    "iQOO Z9": ["https://fdn2.gsmarena.com/vv/bigpic/iqoo-z9-5g.jpg"],
    "iQOO Z9x": ["https://fdn2.gsmarena.com/vv/bigpic/iqoo-z9x.jpg"],
    "iQOO Z8": ["https://fdn2.gsmarena.com/vv/bigpic/iqoo-z8-5g.jpg"],
    "iQOO Z7 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/iqoo-z7-pro-5g.jpg"],
    
    # Transsion (Tecno, Infinix, itel)
    "Tecno Phantom X2 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/tecno-phantom-x2-pro-5g.jpg"],
    "Tecno Camon 30 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-30-pro-5g.jpg"],
    "Tecno Spark 20 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-20-pro-5g.jpg"],
    "Infinix Note 40 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/infinix-note-40-pro-5g.jpg"],
    "Infinix Zero 30": ["https://fdn2.gsmarena.com/vv/bigpic/infinix-zero-30-5g.jpg"],
    "Infinix Hot 40 Pro": ["https://fdn2.gsmarena.com/vv/bigpic/infinix-hot-40-pro.jpg"],
    "itel S24": ["https://fdn2.gsmarena.com/vv/bigpic/itel-s24.jpg"],
}

def fix_all_images():
    """Fix all phone images in the database"""
    session = connect_to_astra()
    
    print("\n" + "="*60)
    print("FIXING ALL PHONE IMAGES - FINAL UPDATE")
    print("="*60 + "\n")
    
    # Get all products
    products = list(Product.objects.all())
    print(f"Found {len(products)} products in database\n")
    
    updated_count = 0
    missing_count = 0
    skipped_count = 0
    
    for product in products:
        product_name = product.name
        
        # Check if product needs image update
        needs_update = False
        
        if not product.images or len(product.images) == 0:
            needs_update = True
            reason = "No images"
        elif 'placeholder' in str(product.images[0]).lower():
            needs_update = True
            reason = "Placeholder image"
        elif 'via.placeholder.com' in str(product.images[0]):
            needs_update = True
            reason = "Placeholder URL"
        
        if needs_update:
            # Try to find matching image
            found_image = None
            
            # Exact match
            if product_name in PHONE_IMAGES:
                found_image = PHONE_IMAGES[product_name]
            else:
                # Partial match
                for key in PHONE_IMAGES.keys():
                    if key.lower() in product_name.lower() or product_name.lower() in key.lower():
                        found_image = PHONE_IMAGES[key]
                        break
            
            if found_image:
                product.images = found_image
                product.save()
                print(f"✓ Updated: {product_name} ({reason})")
                updated_count += 1
            else:
                print(f"✗ Missing: {product_name} - No image found in database")
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
    
    if missing_count > 0:
        print("\nProducts still missing images:")
        for product in products:
            if not product.images or len(product.images) == 0 or 'placeholder' in str(product.images[0]).lower():
                if product.name not in PHONE_IMAGES:
                    found = False
                    for key in PHONE_IMAGES.keys():
                        if key.lower() in product.name.lower() or product.name.lower() in key.lower():
                            found = True
                            break
                    if not found:
                        print(f"  - {product.name}")

if __name__ == "__main__":
    fix_all_images()
