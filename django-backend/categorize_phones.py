#!/usr/bin/env python
"""
Categorize phones by price range, brand series, and performance tier
"""
import os
import sys
import requests
import json

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
import django
django.setup()

def update_product(product_id, update_data):
    """Update a product via API"""
    try:
        response = requests.put(
            f'http://localhost:8080/api/v1/products/{product_id}',
            json=update_data,
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        
        if response.status_code == 200:
            print(f"✅ Updated: {update_data.get('name', 'Product')}")
            return True
        else:
            print(f"❌ Failed to update {update_data.get('name', 'Product')}: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error updating {update_data.get('name', 'Product')}: {e}")
        return False

def get_all_products():
    """Get all products from API"""
    try:
        response = requests.get('http://localhost:8080/api/v1/products')
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Failed to get products: {response.text}")
            return []
    except Exception as e:
        print(f"❌ Error getting products: {e}")
        return []

def categorize_phone(product):
    """Categorize a phone based on various criteria"""
    name = product['name'].lower()
    brand = product['brand'].lower()
    price = product['price']  # Price in cents
    
    # Price ranges in KES (cents)
    BUDGET_MAX = 5000000      # Up to KES 50,000
    MIDRANGE_MAX = 12000000   # Up to KES 120,000
    # Above 120,000 is flagship
    
    # Determine price category
    if price <= BUDGET_MAX:
        price_category = "Budget"
    elif price <= MIDRANGE_MAX:
        price_category = "Mid-range"
    else:
        price_category = "Flagship"
    
    # Determine performance tier
    performance_tier = "Entry"
    if any(keyword in name for keyword in ['pro', 'ultra', 'max', 'plus', '+']):
        performance_tier = "Premium"
    elif any(keyword in name for keyword in ['gt', 'gaming', 'note', 'find']):
        performance_tier = "Performance"
    elif price > 8000000:  # Above 80k
        performance_tier = "High-end"
    elif price > 4000000:  # Above 40k
        performance_tier = "Mid-tier"
    
    # Determine brand series
    series = "Standard"
    if brand == "apple":
        if "pro max" in name:
            series = "iPhone Pro Max"
        elif "pro" in name:
            series = "iPhone Pro"
        elif "plus" in name:
            series = "iPhone Plus"
        else:
            series = "iPhone"
    elif brand == "samsung":
        if "ultra" in name:
            series = "Galaxy S Ultra"
        elif "s24" in name or "s23" in name:
            series = "Galaxy S"
        elif "note" in name:
            series = "Galaxy Note"
        elif "a" in name:
            series = "Galaxy A"
        elif "fold" in name:
            series = "Galaxy Fold"
    elif brand == "google":
        if "pro" in name:
            series = "Pixel Pro"
        elif "a" in name:
            series = "Pixel A"
        else:
            series = "Pixel"
    elif brand == "xiaomi":
        if "ultra" in name:
            series = "Xiaomi Ultra"
        elif "redmi" in name:
            if "note" in name:
                series = "Redmi Note"
            else:
                series = "Redmi"
        else:
            series = "Xiaomi"
    elif brand == "oneplus":
        if "nord" in name:
            series = "OnePlus Nord"
        elif "pro" in name:
            series = "OnePlus Pro"
        else:
            series = "OnePlus"
    elif brand == "oppo":
        if "find" in name:
            series = "OPPO Find"
        elif "reno" in name:
            series = "OPPO Reno"
        elif "a" in name:
            series = "OPPO A"
        else:
            series = "OPPO"
    elif brand == "vivo":
        if "x" in name:
            series = "Vivo X"
        elif "v" in name:
            series = "Vivo V"
        elif "y" in name:
            series = "Vivo Y"
        else:
            series = "Vivo"
    elif brand == "realme":
        if "gt" in name:
            series = "Realme GT"
        elif "pro" in name:
            series = "Realme Pro"
        elif "c" in name:
            series = "Realme C"
        else:
            series = "Realme"
    elif brand == "tecno":
        if "phantom" in name:
            series = "Tecno Phantom"
        elif "camon" in name:
            series = "Tecno Camon"
        elif "spark" in name:
            series = "Tecno Spark"
        else:
            series = "Tecno"
    elif brand == "infinix":
        if "note" in name:
            series = "Infinix Note"
        elif "hot" in name:
            series = "Infinix Hot"
        elif "zero" in name:
            series = "Infinix Zero"
        else:
            series = "Infinix"
    
    # Determine target audience
    target_audience = "General"
    if price <= 3000000:  # Under 30k
        target_audience = "Students"
    elif "gaming" in name or "gt" in name:
        target_audience = "Gamers"
    elif "pro" in name or "ultra" in name:
        target_audience = "Professionals"
    elif "camera" in name or "camon" in name:
        target_audience = "Photography"
    elif price >= 15000000:  # Above 150k
        target_audience = "Premium"
    
    return {
        "price_category": price_category,
        "performance_tier": performance_tier,
        "brand_series": series,
        "target_audience": target_audience
    }

def main():
    print("=" * 80)
    print("  CATEGORIZING PHONES BY MULTIPLE CRITERIA")
    print("=" * 80)
    
    # Get all products
    products = get_all_products()
    if not products:
        print("❌ No products found!")
        return
    
    print(f"📱 Found {len(products)} products to categorize\n")
    
    # Categorize and update each product
    success_count = 0
    categories_stats = {
        "price_category": {},
        "performance_tier": {},
        "brand_series": {},
        "target_audience": {}
    }
    
    for i, product in enumerate(products, 1):
        print(f"[{i:2d}/{len(products)}] Categorizing {product['name']}...")
        
        # Get categories
        categories = categorize_phone(product)
        
        # Update product data with categories
        updated_product = product.copy()
        updated_product.update(categories)
        
        # Add to existing specs
        if 'specs' not in updated_product:
            updated_product['specs'] = {}
        
        updated_product['specs'].update({
            'price_category': categories['price_category'],
            'performance_tier': categories['performance_tier'],
            'brand_series': categories['brand_series'],
            'target_audience': categories['target_audience']
        })
        
        # Update via API
        if update_product(product['_id'], updated_product):
            success_count += 1
            
            # Update stats
            for key, value in categories.items():
                if value not in categories_stats[key]:
                    categories_stats[key][value] = 0
                categories_stats[key][value] += 1
        
        print(f"   💰 Price: {categories['price_category']}")
        print(f"   🚀 Performance: {categories['performance_tier']}")
        print(f"   📱 Series: {categories['brand_series']}")
        print(f"   👥 Audience: {categories['target_audience']}")
        print()
    
    print("=" * 80)
    print("  CATEGORIZATION SUMMARY")
    print("=" * 80)
    print(f"✅ Successfully categorized: {success_count}/{len(products)} products\n")
    
    # Display category statistics
    print("📊 PRICE CATEGORIES:")
    for category, count in sorted(categories_stats['price_category'].items()):
        print(f"   {category}: {count} products")
    
    print("\n🚀 PERFORMANCE TIERS:")
    for tier, count in sorted(categories_stats['performance_tier'].items()):
        print(f"   {tier}: {count} products")
    
    print("\n📱 BRAND SERIES:")
    for series, count in sorted(categories_stats['brand_series'].items()):
        print(f"   {series}: {count} products")
    
    print("\n👥 TARGET AUDIENCES:")
    for audience, count in sorted(categories_stats['target_audience'].items()):
        print(f"   {audience}: {count} products")
    
    # Test filtering by categories
    print("\n" + "=" * 80)
    print("  TESTING CATEGORY FILTERING")
    print("=" * 80)
    
    test_filters = [
        ("Flagship phones", "?price_category=Flagship"),
        ("Budget phones", "?price_category=Budget"),
        ("Apple iPhones", "?brand=Apple"),
        ("Samsung Galaxy", "?brand=Samsung"),
        ("Premium tier", "?performance_tier=Premium")
    ]
    
    for description, filter_param in test_filters:
        try:
            # Note: Our current API doesn't support these filters yet
            # This is just to show what we could implement
            print(f"🔍 {description}: (Filter ready: {filter_param})")
        except Exception as e:
            print(f"❌ Error testing {description}: {e}")
    
    print("\n🎯 NEXT STEPS:")
    print("   1. Update frontend to show categories")
    print("   2. Add category filtering to API")
    print("   3. Create category-based navigation")
    print("   4. Add price range filters")
    print("   5. Implement brand series grouping")

if __name__ == '__main__':
    main()