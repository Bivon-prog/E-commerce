#!/usr/bin/env python3
"""
Add comprehensive Transsion Holdings lineup (Tecno, Infinix, itel) to database
"""

import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from astrapy import DataAPIClient
import uuid

def get_tecno_phones():
    """Complete Tecno lineup"""
    phones = []
    
    # Phantom Series (Foldables & Flagship)
    phantom_models = [
        ("Tecno Phantom V Fold 2 5G", 19999900, "Latest foldable with improved hinge and displays. Revolutionary design."),
        ("Tecno Phantom V Flip 2 5G", 14999900, "Compact foldable with clamshell design. Stylish innovation."),
        ("Tecno Phantom V Fold", 17999900, "First Tecno foldable with large inner display. Pioneering device."),
        ("Tecno Phantom V Flip", 12999900, "First flip phone from Tecno. Compact elegance."),
        ("Tecno Phantom X2 Pro 5G", 8999900, "Flagship with curved display and premium cameras. Top-tier Tecno."),
        ("Tecno Phantom X2 5G", 7999900, "Standard flagship with excellent cameras. Premium experience."),
    ]
    
    for name, price, desc in phantom_models:
        form_factor = "Foldable Clamshell" if "Flip" in name else ("Foldable Book" if "Fold" in name else "Candy Bar")
        tier = "Ultra-Premium" if price > 10000000 else "Premium Flagship"
        phones.append({
            "name": name,
            "brand": "Tecno",
            "category": "Smartphones",
            "price": price,
            "description": desc,
            "in_stock": True,
            "images": [
                "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-phantom-x2-pro-1.jpg",
                "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-phantom-x2-pro-2.jpg",
                "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=470&h=556&fit=crop"
            ],
            "specs": {
                "ram": "8GB/12GB",
                "storage": "256GB/512GB",
                "display": "6.7-6.9-inch AMOLED",
                "processor": "MediaTek Dimensity",
                "camera": "50MP-64MP Multi",
                "battery": "4500-5000mAh",
                "price_tier": tier,
                "use_case": "Camera & Photography",
                "form_factor": form_factor,
                "software_experience": "HiOS",
                "chipset_category": "MediaTek Dimensity",
                "market_origin": "Transsion Empire",
                "target_demographic": "Professionals"
            }
        })
    
    # Camon Series (Camera Experts)
    camon_models = [
        # Camon 40 Series
        ("Tecno Camon 40 Premier 5G", 5999900, "Top Camon with premium cameras and 5G. Photography flagship."),
        ("Tecno Camon 40 Pro 5G", 4999900, "Pro camera phone with 5G connectivity. Excellent photography."),
        ("Tecno Camon 40 Pro 4G", 4499900, "Pro cameras without 5G. Great value camera phone."),
        ("Tecno Camon 40", 3999900, "Standard Camon with good cameras. Reliable shooter."),
        # Camon 30 Series
        ("Tecno Camon 30 Premier 5G", 5499900, "Previous flagship camera phone. Still excellent."),
        ("Tecno Camon 30 Pro 5G", 4499900, "Pro camera with 5G. Great photography device."),
        ("Tecno Camon 30 5G", 3999900, "Mid-range camera phone with 5G. Good value."),
        ("Tecno Camon 30", 3499900, "Standard camera phone. Decent photography."),
        # Camon 20 Series
        ("Tecno Camon 20 Premier 5G", 4999900, "Older flagship camera phone. Still capable."),
        ("Tecno Camon 20 Pro 5G", 3999900, "Pro camera from previous gen. Good option."),
        ("Tecno Camon 20 Pro", 3499900, "4G pro camera phone. Budget-friendly."),
        ("Tecno Camon 20", 2999900, "Entry camera phone. Basic photography."),
    ]
    
    for name, price, desc in camon_models:
        tier = "Flagship Killer" if price > 5000000 else ("Mid-Range" if price > 3500000 else "Budget")
        phones.append({
            "name": name,
            "brand": "Tecno",
            "category": "Smartphones",
            "price": price,
            "description": desc,
            "in_stock": True,
            "images": [
                "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-30-pro-1.jpg",
                "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-30-pro-2.jpg",
                "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=470&h=556&fit=crop"
            ],
            "specs": {
                "ram": "6GB/8GB",
                "storage": "128GB/256GB",
                "display": "6.6-6.8-inch AMOLED",
                "processor": "MediaTek Helio/Dimensity",
                "camera": "50MP-64MP Multi",
                "battery": "5000mAh",
                "price_tier": tier,
                "use_case": "Camera & Photography"
            }
        })
    
    return phones


def get_tecno_spark_pova_pop():
    """Tecno Spark, Pova, and Pop series"""
    phones = []
    
    # Spark Series (Youth & Budget)
    spark_models = [
        # Spark 40 Series
        ("Tecno Spark 40 Pro+", 3299900, "Top Spark with enhanced features. Best budget option."),
        ("Tecno Spark 40 Pro", 2999900, "Pro features at budget price. Great value."),
        ("Tecno Spark 40", 2699900, "Standard Spark with good specs. Reliable budget phone."),
        ("Tecno Spark 40C", 2399900, "Entry Spark model. Basic smartphone."),
        # Spark 30 Series
        ("Tecno Spark 30 Pro 5G", 2999900, "Budget 5G phone. Affordable connectivity."),
        ("Tecno Spark 30 Pro", 2699900, "Pro budget phone. Good features."),
        ("Tecno Spark 30", 2399900, "Standard budget phone. Basic features."),
        ("Tecno Spark 30C", 2099900, "Entry budget phone. Starter device."),
        # Spark 20 Series
        ("Tecno Spark 20 Pro+", 2799900, "Previous top Spark. Still good."),
        ("Tecno Spark 20 Pro", 2499900, "Older pro model. Budget option."),
        ("Tecno Spark 20", 2199900, "Standard older Spark. Entry level."),
        ("Tecno Spark 20C", 1899900, "Basic Spark model. Very affordable."),
    ]
    
    # Pova Series (Gaming & Battery)
    pova_models = [
        # Pova 7 Series
        ("Tecno Pova 7 5G", 4299900, "Gaming phone with 5G. Performance beast."),
        ("Tecno Pova 7 Pro", 3999900, "Pro gaming features. Excellent performance."),
        ("Tecno Pova Slim 5G", 3699900, "Slim gaming phone with 5G. Portable power."),
        # Pova 6 Series
        ("Tecno Pova 6 Pro 5G", 3899900, "Previous pro gaming phone. Still powerful."),
        ("Tecno Pova 6", 3499900, "Standard gaming phone. Good performance."),
        ("Tecno Pova 6 Neo", 3199900, "Entry gaming phone. Budget gaming."),
        # Pova 5 Series
        ("Tecno Pova 5 Pro", 3599900, "Older pro gaming phone. Capable device."),
        ("Tecno Pova 5", 3299900, "Previous standard gaming. Budget option."),
    ]
    
    # Pop Series (Entry Level)
    pop_models = [
        ("Tecno Pop 10 Pro", 1799900, "Latest entry phone with pro features. Best Pop."),
        ("Tecno Pop 10", 1599900, "Standard entry phone. Basic smartphone."),
        ("Tecno Pop 9", 1499900, "Previous entry model. Very affordable."),
        ("Tecno Pop 8", 1399900, "Older entry phone. Budget starter."),
        ("Tecno Pop 7", 1299900, "Basic entry phone. Ultra-budget."),
    ]
    
    all_models = spark_models + pova_models + pop_models
    
    for name, price, desc in all_models:
        if "Pova" in name:
            use_case = "Gaming"
            tier = "Mid-Range"
        elif "Pop" in name:
            use_case = "General"
            tier = "Entry-Level"
        else:
            use_case = "General"
            tier = "Budget" if price > 2500000 else "Entry-Level"
        
        phones.append({
            "name": name,
            "brand": "Tecno",
            "category": "Smartphones",
            "price": price,
            "description": desc,
            "in_stock": True,
            "images": [
                "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-spark-20-1.jpg",
                "https://fdn2.gsmarena.com/vv/pics/tecno/tecno-spark-20-2.jpg",
                "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=470&h=556&fit=crop"
            ],
            "specs": {
                "ram": "4GB/6GB/8GB",
                "storage": "64GB/128GB/256GB",
                "display": "6.5-6.8-inch HD+/FHD+",
                "processor": "MediaTek Helio",
                "camera": "13MP-50MP Multi",
                "battery": "5000-6000mAh",
                "price_tier": tier,
                "use_case": use_case
            }
        })
    
    return phones


def get_infinix_phones():
    """Complete Infinix lineup"""
    phones = []
    
    # Zero Series (Vlogging & Premium)
    zero_models = [
        ("Infinix Zero Flip", 14999900, "Foldable flip phone. Stylish innovation."),
        ("Infinix Zero 40 5G", 5999900, "Latest premium phone with 5G. Flagship experience."),
        ("Infinix Zero 40 4G", 5499900, "Premium phone without 5G. Great value."),
        ("Infinix Zero 30 5G", 5499900, "Previous 5G flagship. Still excellent."),
        ("Infinix Zero 30 4G", 4999900, "Previous flagship 4G. Good option."),
        ("Infinix Zero Ultra", 6499900, "Ultra premium model. Top-tier Infinix."),
    ]
    
    # GT Series (Dedicated Gaming)
    gt_models = [
        ("Infinix GT 30 Pro", 4999900, "Latest gaming flagship. Performance beast."),
        ("Infinix GT 20 Pro", 4499900, "Previous gaming pro. Still powerful."),
        ("Infinix GT 10 Pro", 3999900, "Older gaming phone. Budget gaming."),
    ]
    
    # Note Series (Performance & Fast Charge)
    note_models = [
        # Note 60 Series
        ("Infinix Note 60 Ultra", 5499900, "Ultra performance with fast charge. Top Note."),
        ("Infinix Note 60", 4999900, "Latest Note with great features. Excellent phone."),
        # Note 50 Series
        ("Infinix Note 50 Pro+", 4799900, "Top Note 50 with premium features. Great value."),
        ("Infinix Note 50 Pro", 4299900, "Pro performance and charging. Reliable device."),
        ("Infinix Note 50s", 3999900, "Slim Note variant. Portable power."),
        # Note 40 Series
        ("Infinix Note 40 Pro+ 5G", 4499900, "Previous top Note with 5G. Still great."),
        ("Infinix Note 40 Pro 5G", 3999900, "Pro Note with 5G. Good connectivity."),
        ("Infinix Note 40 Pro 4G", 3699900, "Pro Note without 5G. Budget option."),
        ("Infinix Note 40", 3399900, "Standard Note 40. Reliable phone."),
        ("Infinix Note 40X", 3199900, "Budget Note variant. Entry performance."),
        # Note 30 Series
        ("Infinix Note 30 VIP", 4299900, "VIP edition with premium features. Special model."),
        ("Infinix Note 30 Pro", 3799900, "Pro Note 30. Good performance."),
        ("Infinix Note 30 5G", 3499900, "5G connectivity. Future-ready."),
        ("Infinix Note 30", 3199900, "Standard Note 30. Basic features."),
    ]
    
    all_infinix = zero_models + gt_models + note_models
    
    for name, price, desc in all_infinix:
        if "Zero" in name:
            tier = "Premium Flagship" if price > 10000000 else "Flagship Killer"
            use_case = "Camera & Photography"
            form_factor = "Foldable Clamshell" if "Flip" in name else "Candy Bar"
        elif "GT" in name:
            tier = "Mid-Range"
            use_case = "Gaming"
            form_factor = "Candy Bar"
        else:
            tier = "Mid-Range" if price > 4000000 else "Budget"
            use_case = "Battery & Endurance"
            form_factor = "Candy Bar"
        
        phones.append({
            "name": name,
            "brand": "Infinix",
            "category": "Smartphones",
            "price": price,
            "description": desc,
            "in_stock": True,
            "images": [
                "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-40-pro-1.jpg",
                "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-note-40-pro-2.jpg",
                "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=470&h=556&fit=crop"
            ],
            "specs": {
                "ram": "6GB/8GB/12GB",
                "storage": "128GB/256GB/512GB",
                "display": "6.6-6.8-inch AMOLED",
                "processor": "MediaTek Helio/Dimensity",
                "camera": "50MP-108MP Multi",
                "battery": "5000-6000mAh",
                "price_tier": tier,
                "use_case": use_case,
                "form_factor": form_factor
            }
        })
    
    return phones


def get_infinix_hot_smart():
    """Infinix Hot and Smart series"""
    phones = []
    
    # Hot Series (Entertainment)
    hot_models = [
        # Hot 60 Series
        ("Infinix Hot 60 Pro+", 3499900, "Top Hot with premium features. Best entertainment."),
        ("Infinix Hot 60 Pro", 3199900, "Pro entertainment phone. Great multimedia."),
        ("Infinix Hot 60", 2899900, "Standard Hot 60. Good entertainment."),
        ("Infinix Hot 60i", 2599900, "Entry Hot 60. Budget entertainment."),
        # Hot 50 Series
        ("Infinix Hot 50 Pro+", 3299900, "Previous top Hot. Still great."),
        ("Infinix Hot 50 Pro", 2999900, "Pro Hot 50. Good features."),
        ("Infinix Hot 50 5G", 2799900, "5G entertainment. Future-ready."),
        ("Infinix Hot 50i", 2499900, "Entry Hot 50. Budget option."),
        # Hot 40 Series
        ("Infinix Hot 40 Pro", 2899900, "Older pro Hot. Capable device."),
        ("Infinix Hot 40", 2599900, "Standard Hot 40. Basic entertainment."),
        ("Infinix Hot 40i", 2299900, "Entry Hot 40. Very affordable."),
    ]
    
    # Smart Series (Entry Level)
    smart_models = [
        ("Infinix Smart 10 HD", 1799900, "Latest entry with HD display. Best Smart."),
        ("Infinix Smart 10", 1699900, "Standard entry phone. Basic smartphone."),
        ("Infinix Smart 9", 1599900, "Previous entry model. Affordable."),
        ("Infinix Smart 8 Plus", 1499900, "Enhanced entry phone. Budget option."),
        ("Infinix Smart 8", 1399900, "Basic entry phone. Ultra-budget."),
    ]
    
    all_models = hot_models + smart_models
    
    for name, price, desc in all_models:
        if "Smart" in name:
            tier = "Entry-Level"
            use_case = "General"
        else:
            tier = "Budget" if price > 2800000 else "Entry-Level"
            use_case = "General"
        
        phones.append({
            "name": name,
            "brand": "Infinix",
            "category": "Smartphones",
            "price": price,
            "description": desc,
            "in_stock": True,
            "images": [
                "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-hot-40i-1.jpg",
                "https://fdn2.gsmarena.com/vv/pics/infinix/infinix-hot-40i-2.jpg",
                "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=470&h=556&fit=crop"
            ],
            "specs": {
                "ram": "3GB/4GB/6GB",
                "storage": "64GB/128GB",
                "display": "6.5-6.7-inch HD+/FHD+",
                "processor": "MediaTek Helio/Unisoc",
                "camera": "13MP-50MP Multi",
                "battery": "5000-6000mAh",
                "price_tier": tier,
                "use_case": use_case
            }
        })
    
    return phones

def get_itel_phones():
    """Complete itel lineup"""
    phones = []
    
    # S-Series (Premium Budget)
    s_models = [
        ("itel S25 Ultra", 2499900, "Top itel with ultra features. Best budget premium."),
        ("itel S25", 2199900, "Latest S-series. Premium budget."),
        ("itel S24", 1999900, "Previous S-series. Good value."),
        ("itel S23+", 1899900, "Enhanced S23. Budget option."),
        ("itel S23", 1799900, "Standard S23. Affordable premium."),
    ]
    
    # P-Series (Power / Big Battery)
    p_models = [
        ("itel P65", 1999900, "Latest with charging case. Ultimate battery."),
        ("itel P55+", 1799900, "Enhanced P55. Great battery."),
        ("itel P55 5G", 1899900, "5G with big battery. Connected power."),
        ("itel P55 4G", 1699900, "4G power phone. Long-lasting."),
        ("itel P40+", 1599900, "Previous enhanced P. Good battery."),
        ("itel P40", 1499900, "Standard P40. Reliable battery."),
    ]
    
    # A-Series (Basic Entry)
    a_models = [
        ("itel A80", 1399900, "Latest entry phone. Best basic."),
        ("itel A70", 1299900, "Mid entry phone. Good starter."),
        ("itel A60s", 1199900, "Slim entry phone. Portable basic."),
        ("itel A60", 1099900, "Standard entry. Very affordable."),
        ("itel A05s", 999900, "Basic entry phone. Ultra-budget."),
    ]
    
    all_itel = s_models + p_models + a_models
    
    for name, price, desc in all_itel:
        if "S" in name and "S" == name.split()[1][0]:
            tier = "Budget"
            use_case = "General"
        elif "P" in name and "P" == name.split()[1][0]:
            tier = "Entry-Level"
            use_case = "Battery & Endurance"
        else:
            tier = "Entry-Level"
            use_case = "General"
        
        phones.append({
            "name": name,
            "brand": "itel",
            "category": "Smartphones",
            "price": price,
            "description": desc,
            "in_stock": True,
            "images": [
                "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=470&h=556&fit=crop",
                "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=470&h=556&fit=crop",
                "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=470&h=556&fit=crop"
            ],
            "specs": {
                "ram": "2GB/3GB/4GB",
                "storage": "32GB/64GB/128GB",
                "display": "6.5-6.6-inch HD+",
                "processor": "Unisoc/MediaTek",
                "camera": "8MP-13MP Dual",
                "battery": "4000-5000mAh",
                "price_tier": tier,
                "use_case": use_case
            }
        })
    
    return phones


def add_all_transsion_phones():
    """Add all Transsion Holdings phones to Astra database"""
    
    try:
        print("📱 ADDING COMPREHENSIVE TRANSSION HOLDINGS LINEUP")
        print("=" * 60)
        
        client = DataAPIClient(settings.ASTRA_TOKEN)
        database = client.get_database_by_api_endpoint(settings.ASTRA_API_ENDPOINT)
        collection = database.get_collection("products")
        
        # Collect all phones
        all_phones = []
        
        print("\n🔵 Collecting Tecno phones...")
        all_phones.extend(get_tecno_phones())
        all_phones.extend(get_tecno_spark_pova_pop())
        
        print("🟢 Collecting Infinix phones...")
        all_phones.extend(get_infinix_phones())
        all_phones.extend(get_infinix_hot_smart())
        
        print("🟡 Collecting itel phones...")
        all_phones.extend(get_itel_phones())
        
        print(f"\n📊 Total phones to add: {len(all_phones)}")
        print("=" * 60)
        
        added_count = 0
        skipped_count = 0
        
        for phone in all_phones:
            try:
                # Check if phone already exists
                existing = collection.find_one({"name": phone["name"]})
                
                if existing:
                    print(f"⚠️  {phone['name']} already exists, skipping...")
                    skipped_count += 1
                    continue
                
                # Add new phone
                phone['_id'] = str(uuid.uuid4())
                collection.insert_one(phone)
                
                print(f"✅ Added {phone['name']} - KES {phone['price']/100:,.0f}")
                added_count += 1
                
            except Exception as e:
                print(f"❌ Failed to add {phone['name']}: {str(e)}")
        
        print(f"\n🎉 DONE!")
        print(f"   Added: {added_count} new Transsion phones")
        print(f"   Skipped: {skipped_count} existing models")
        print(f"   Total Transsion lineup: {added_count + skipped_count} models")
        print(f"\n📱 Breakdown:")
        print(f"   Tecno: ~43 models")
        print(f"   Infinix: ~39 models")
        print(f"   itel: ~16 models")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    add_all_transsion_phones()