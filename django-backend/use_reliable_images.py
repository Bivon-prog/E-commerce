import os
from astrapy import DataAPIClient
from dotenv import load_dotenv

load_dotenv()

def generate_placeholder_image(phone_name, brand):
    """Generate a placeholder image URL with phone name"""
    # Use a reliable placeholder service with phone name
    encoded_name = phone_name.replace(' ', '+')
    return f"https://placehold.co/400x500/2563eb/white?text={encoded_name}&font=roboto"

def fix_all_with_placeholders():
    """Fix all images with reliable placeholder images"""
    token = os.getenv('ASTRA_TOKEN')
    api_endpoint = os.getenv('ASTRA_API_ENDPOINT')
    
    client = DataAPIClient(token)
    database = client.get_database(api_endpoint)
    collection = database.get_collection("products")
    
    products = list(collection.find({}))
    
    print(f"\n{'='*80}")
    print(f"UPDATING ALL IMAGES WITH RELIABLE PLACEHOLDERS")
    print(f"{'='*80}\n")
    
    updated = 0
    
    for product in products:
        name = product.get('name', 'Phone')
        brand = product.get('brand', 'Brand')
        product_id = product.get('_id')
        
        # Generate placeholder image
        image_url = generate_placeholder_image(name, brand)
        
        collection.update_one(
            {"_id": product_id},
            {"$set": {"images": [image_url]}}
        )
        print(f"✓ {name}")
        updated += 1
    
    print(f"\n{'='*80}")
    print(f"✓ Updated all {updated} products with placeholder images")
    print(f"{'='*80}\n")
    print("Note: These are temporary placeholders. You can replace them with actual")
    print("product images later by uploading images or using a different image source.")

if __name__ == "__main__":
    fix_all_with_placeholders()
