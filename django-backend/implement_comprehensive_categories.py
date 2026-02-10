#!/usr/bin/env python
"""
Implement comprehensive 7-category system for all products
Based on the detailed categorization framework provided
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

def get_comprehensive_categories(product):
    """
    Determine comprehensive categories for a product based on its specs and brand
    """
    name = product['name'].lower()
    brand = product['brand'].lower()
    price = product['price']
    specs = product.get('specs', {})
    
    categories = {}
    
    # 1. PRICE TIER CATEGORIZATION
    if price < 2000000:  # Under KES 20,000
        categories['price_tier'] = 'Entry-Level'
        categories['price_tier_description'] = 'The "Survival" Tier - Basic calls, WhatsApp, light browsing'
    elif price < 5000000:  # KES 20,000 - 50,000
        categories['price_tier'] = 'Budget'
        categories['price_tier_description'] = 'The "Value" Tier - Daily use, social media, casual photos'
    elif price < 10000000:  # KES 50,000 - 100,000
        categories['price_tier'] = 'Mid-Range'
        categories['price_tier_description'] = 'The "Sweet Spot" - Great screens and cameras without flagship price'
    elif price < 13000000:  # KES 100,000 - 130,000
        categories['price_tier'] = 'Flagship Killer'
        categories['price_tier_description'] = 'The "Performance" Tier - Top-tier speed, cheaper build/cameras'
    elif price < 18000000:  # KES 130,000 - 180,000
        categories['price_tier'] = 'Premium Flagship'
        categories['price_tier_description'] = 'The "Status" Tier - Best technology available'
    else:  # Above KES 180,000
        categories['price_tier'] = 'Ultra-Premium'
        categories['price_tier_description'] = 'Luxury - Folding screens, experimental tech'
    
    # 2. USE CASE CATEGORIZATION
    if any(keyword in name for keyword in ['pro max', 'ultra', 'pro', 'find x', 'x100', 'phantom']):
        if 'camera' in specs.get('camera', '').lower() or any(brand_name in brand for brand_name in ['vivo', 'oppo', 'xiaomi', 'google']):
            categories['use_case'] = 'Camera & Photography'
            categories['use_case_description'] = 'Massive sensors, optical zoom, camera brand partnerships'
        else:
            categories['use_case'] = 'Camera & Photography'
            categories['use_case_description'] = 'Professional photography features'
    elif any(keyword in name for keyword in ['rog', 'gaming', 'gt', 'poco f', 'pova']):
        categories['use_case'] = 'Gaming'
        categories['use_case_description'] = 'Shoulder triggers, cooling, RGB lights, high performance'
    elif any(keyword in name for keyword in ['m55', 'm', 'pova', 'hot']) and 'mah' in specs.get('battery', ''):
        categories['use_case'] = 'Battery & Endurance'
        categories['use_case_description'] = 'Focused on lasting 2+ days'
    elif 'ultra' in name and 'samsung' in brand:
        categories['use_case'] = 'Productivity & Business'
        categories['use_case_description'] = 'S-Pen stylus, multitasking, business features'
    elif any(keyword in name for keyword in ['v30', 'v', 'reno', 'civi', 'camon']):
        categories['use_case'] = 'Fashion & Vlogging'
        categories['use_case_description'] = 'Selfie quality, beautiful design, slim and light'
    else:
        categories['use_case'] = 'General Purpose'
        categories['use_case_description'] = 'Balanced performance for everyday use'
    
    # 3. FORM FACTOR CATEGORIZATION
    if any(keyword in name for keyword in ['fold', 'flip']):
        if 'fold' in name:
            categories['form_factor'] = 'Foldable (Book Style)'
            categories['form_factor_description'] = 'Opens horizontally like a book to become tablet'
        else:
            categories['form_factor'] = 'Foldable (Clamshell)'
            categories['form_factor_description'] = 'Folds vertically like makeup compact'
    elif any(keyword in name for keyword in ['xcover', 'rugged']):
        categories['form_factor'] = 'Rugged'
        categories['form_factor_description'] = 'Thick, armored phones for construction sites'
    else:
        categories['form_factor'] = 'Candy Bar (Standard)'
        categories['form_factor_description'] = 'Traditional rectangular slab design'
    
    # 4. SOFTWARE EXPERIENCE CATEGORIZATION
    if 'apple' in brand:
        categories['software_experience'] = 'iOS (Walled Garden)'
        categories['software_description'] = 'Smooth, secure, but restrictive'
    elif any(brand_name in brand for brand_name in ['google', 'motorola', 'sony']):
        categories['software_experience'] = 'Stock Android (Clean)'
        categories['software_description'] = 'As Google intended, no bloatware, simple'
    elif 'samsung' in brand:
        categories['software_experience'] = 'OneUI (Feature Rich)'
        categories['software_description'] = 'Heavy skin with tons of extra features'
    elif any(brand_name in brand for brand_name in ['xiaomi', 'redmi', 'poco']):
        categories['software_experience'] = 'HyperOS (Feature Rich)'
        categories['software_description'] = 'Xiaomi\'s feature-packed Android skin'
    elif any(brand_name in brand for brand_name in ['tecno', 'infinix']):
        categories['software_experience'] = 'HiOS/XOS (Feature Rich)'
        categories['software_description'] = 'Transsion\'s customized Android experience'
    elif any(brand_name in brand for brand_name in ['oppo', 'realme']):
        categories['software_experience'] = 'ColorOS (Feature Rich)'
        categories['software_description'] = 'Oppo\'s customized Android skin'
    elif 'vivo' in brand:
        categories['software_experience'] = 'FuntouchOS (Feature Rich)'
        categories['software_description'] = 'Vivo\'s customized Android experience'
    else:
        categories['software_experience'] = 'Custom Android'
        categories['software_description'] = 'Manufacturer-customized Android'
    
    # 5. CHIPSET CATEGORIZATION
    processor = specs.get('processor', '').lower()
    if 'snapdragon' in processor:
        categories['chipset_category'] = 'Snapdragon (Qualcomm)'
        categories['chipset_description'] = 'Standard for Android flagships, best for gaming'
    elif any(chip in processor for chip in ['dimensity', 'helio', 'mediatek']):
        categories['chipset_category'] = 'Dimensity/Helio (MediaTek)'
        categories['chipset_description'] = 'Dominates mid-range and budget market'
    elif any(chip in processor for chip in ['bionic', 'a17', 'a16', 'a15']):
        categories['chipset_category'] = 'Bionic (Apple)'
        categories['chipset_description'] = 'Most powerful chips, exclusive to iPhones'
    elif 'tensor' in processor:
        categories['chipset_category'] = 'Tensor (Google)'
        categories['chipset_description'] = 'Focused on AI tasks rather than raw speed'
    elif 'exynos' in processor:
        categories['chipset_category'] = 'Exynos (Samsung)'
        categories['chipset_description'] = 'Samsung\'s homemade chips'
    elif any(chip in processor for chip in ['unisoc', 'tiger']):
        categories['chipset_category'] = 'UNISOC'
        categories['chipset_description'] = 'Budget-focused processors'
    else:
        categories['chipset_category'] = 'Other'
        categories['chipset_description'] = 'Various other processors'
    
    # 6. MARKET ORIGIN CATEGORIZATION
    if 'apple' in brand:
        categories['market_origin'] = 'American Tech'
        categories['origin_description'] = 'Software-first companies from USA'
    elif 'samsung' in brand:
        categories['market_origin'] = 'Global Giants'
        categories['origin_description'] = 'Available in almost every country on Earth'
    elif any(brand_name in brand for brand_name in ['tecno', 'infinix', 'itel']):
        categories['market_origin'] = 'Transsion Empire'
        categories['origin_description'] = 'Dominant in Africa, Pakistan, parts of India'
    elif any(brand_name in brand for brand_name in ['xiaomi', 'oppo', 'vivo', 'honor', 'realme', 'oneplus']):
        categories['market_origin'] = 'Chinese Powerhouses'
        categories['origin_description'] = 'Massive in Asia and Europe'
    elif 'google' in brand:
        categories['market_origin'] = 'American Tech'
        categories['origin_description'] = 'Software-first companies from USA'
    else:
        categories['market_origin'] = 'Other'
        categories['origin_description'] = 'Various other origins'
    
    # 7. ADDITIONAL SMART CATEGORIES
    # Target demographic based on price and features
    if categories['price_tier'] in ['Entry-Level', 'Budget']:
        categories['target_demographic'] = 'Students & First-time Users'
    elif categories['use_case'] == 'Gaming':
        categories['target_demographic'] = 'Gamers & Performance Users'
    elif categories['use_case'] == 'Camera & Photography':
        categories['target_demographic'] = 'Content Creators & Photography Enthusiasts'
    elif categories['price_tier'] == 'Premium Flagship':
        categories['target_demographic'] = 'Professionals & Status-conscious Users'
    else:
        categories['target_demographic'] = 'General Consumers'
    
    return categories

def update_product_categories(product_id, categories):
    """Update a product with comprehensive categories"""
    try:
        # Get current product
        response = requests.get(f'http://localhost:8080/api/v1/products/{product_id}')
        if response.status_code != 200:
            print(f"❌ Failed to get product {product_id}")
            return False
        
        product = response.json()
        
        # Update specs with new categories
        if 'specs' not in product:
            product['specs'] = {}
        
        product['specs'].update(categories)
        
        # Update product
        update_response = requests.put(
            f'http://localhost:8080/api/v1/products/{product_id}',
            json=product,
            headers={'Content-Type': 'application/json'}
        )
        
        if update_response.status_code == 200:
            return True
        else:
            print(f"❌ Failed to update product {product_id}: {update_response.text}")
            return False
    
    except Exception as e:
        print(f"❌ Error updating product {product_id}: {e}")
        return False

def main():
    print("=" * 80)
    print("  IMPLEMENTING COMPREHENSIVE 7-CATEGORY SYSTEM")
    print("=" * 80)
    
    try:
        # Get all products
        response = requests.get('http://localhost:8080/api/v1/products')
        if response.status_code != 200:
            print(f"❌ Failed to get products: {response.status_code}")
            return
        
        products = response.json()
        print(f"📱 Processing {len(products)} products\n")
        
        success_count = 0
        category_stats = {
            'price_tier': {},
            'use_case': {},
            'form_factor': {},
            'software_experience': {},
            'chipset_category': {},
            'market_origin': {},
            'target_demographic': {}
        }
        
        for i, product in enumerate(products, 1):
            print(f"[{i:2d}/{len(products)}] Processing {product['name']}...")
            
            # Get comprehensive categories
            categories = get_comprehensive_categories(product)
            
            # Update product
            if update_product_categories(product['_id'], categories):
                success_count += 1
                print(f"   ✅ Updated with {len(categories)} categories")
                
                # Update stats
                for key in category_stats.keys():
                    if key in categories:
                        value = categories[key]
                        if value not in category_stats[key]:
                            category_stats[key][value] = 0
                        category_stats[key][value] += 1
            else:
                print(f"   ❌ Failed to update")
            
            # Small delay
            time.sleep(0.3)
        
        print("\n" + "=" * 80)
        print("  COMPREHENSIVE CATEGORIZATION COMPLETE")
        print("=" * 80)
        print(f"✅ Successfully updated: {success_count}/{len(products)} products\n")
        
        # Display category statistics
        print("1️⃣  PRICE TIER CATEGORIES:")
        for tier, count in sorted(category_stats['price_tier'].items()):
            print(f"   {tier}: {count} products")
        
        print("\n2️⃣  USE CASE CATEGORIES:")
        for use_case, count in sorted(category_stats['use_case'].items()):
            print(f"   {use_case}: {count} products")
        
        print("\n3️⃣  FORM FACTOR CATEGORIES:")
        for form, count in sorted(category_stats['form_factor'].items()):
            print(f"   {form}: {count} products")
        
        print("\n4️⃣  SOFTWARE EXPERIENCE:")
        for software, count in sorted(category_stats['software_experience'].items()):
            print(f"   {software}: {count} products")
        
        print("\n5️⃣  CHIPSET CATEGORIES:")
        for chipset, count in sorted(category_stats['chipset_category'].items()):
            print(f"   {chipset}: {count} products")
        
        print("\n6️⃣  MARKET ORIGIN:")
        for origin, count in sorted(category_stats['market_origin'].items()):
            print(f"   {origin}: {count} products")
        
        print("\n7️⃣  TARGET DEMOGRAPHICS:")
        for demo, count in sorted(category_stats['target_demographic'].items()):
            print(f"   {demo}: {count} products")
        
        print("\n🎯 COMPREHENSIVE CATEGORIZATION READY!")
        print("   - 7 different categorization methods implemented")
        print("   - All products updated with smart categories")
        print("   - Ready for advanced filtering and navigation")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()