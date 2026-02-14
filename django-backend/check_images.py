import os
from astrapy import DataAPIClient
from dotenv import load_dotenv

load_dotenv()

def check_images():
    """Check all product images"""
    token = os.getenv('ASTRA_TOKEN')
    api_endpoint = os.getenv('ASTRA_API_ENDPOINT')
    
    client = DataAPIClient(token)
    database = client.get_database(api_endpoint)
    collection = database.get_collection("products")
    
    products = list(collection.find({}))
    
    print(f"\nChecking {len(products)} products...\n")
    
    no_images = []
    placeholder_images = []
    has_images = []
    
    for product in products:
        name = product.get('name', 'Unknown')
        images = product.get('images', [])
        
        if not images or len(images) == 0:
            no_images.append(name)
        elif 'placeholder' in str(images[0]).lower() or 'via.placeholder' in str(images[0]):
            placeholder_images.append((name, images[0]))
        else:
            has_images.append((name, images[0]))
    
    print("="*80)
    print(f"PRODUCTS WITHOUT IMAGES ({len(no_images)}):")
    print("="*80)
    for name in no_images:
        print(f"  - {name}")
    
    print("\n" + "="*80)
    print(f"PRODUCTS WITH PLACEHOLDER IMAGES ({len(placeholder_images)}):")
    print("="*80)
    for name, img in placeholder_images:
        print(f"  - {name}")
        print(f"    {img}")
    
    print("\n" + "="*80)
    print(f"PRODUCTS WITH VALID IMAGES ({len(has_images)}):")
    print("="*80)
    for name, img in has_images[:10]:  # Show first 10
        print(f"  - {name}")
        print(f"    {img[:80]}...")
    if len(has_images) > 10:
        print(f"  ... and {len(has_images) - 10} more")
    
    print("\n" + "="*80)
    print("SUMMARY:")
    print("="*80)
    print(f"Total products: {len(products)}")
    print(f"✓ With valid images: {len(has_images)}")
    print(f"✗ Without images: {len(no_images)}")
    print(f"⚠ With placeholders: {len(placeholder_images)}")
    print("="*80 + "\n")

if __name__ == "__main__":
    check_images()
