import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from products.astra_models import AstraProduct

def update_phone_image(phone_name, image_url):
    """Update a single phone's image"""
    try:
        # Get all products and search for matching name
        all_products = AstraProduct.get_all()
        
        # Find products matching the name (case-insensitive)
        matching_products = [
            p for p in all_products 
            if phone_name.lower() in p.get('name', '').lower()
        ]
        
        if not matching_products:
            print(f"❌ No phone found matching: {phone_name}")
            return False
        
        if len(matching_products) > 1:
            print(f"⚠️  Multiple phones found matching '{phone_name}':")
            for p in matching_products:
                print(f"   - {p.get('name')}")
            print("Please be more specific.")
            return False
        
        product = matching_products[0]
        old_image = product.get('images', ['No image'])[0]
        
        # Update the product with new image (without validation)
        success = AstraProduct.update(product['_id'], {'images': [image_url]}, validate_images=False)
        
        if success:
            print(f"✅ Updated: {product.get('name')}")
            print(f"   Old: {old_image}")
            print(f"   New: {image_url}")
            return True
        else:
            print(f"❌ Failed to update {product.get('name')}")
            return False
        
    except Exception as e:
        print(f"❌ Error updating {phone_name}: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # Update Infinix Note 40 Pro+
    update_phone_image(
        "Infinix Note 40 Pro+",
        "https://i.gadgets360cdn.com/large/infinix_note_40_pro_plus_1712236091790.jpg"
    )
