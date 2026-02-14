import os
from astrapy import DataAPIClient
from dotenv import load_dotenv

load_dotenv()

def list_all_products():
    """List all products with their images"""
    token = os.getenv('ASTRA_TOKEN')
    api_endpoint = os.getenv('ASTRA_API_ENDPOINT')
    
    client = DataAPIClient(token)
    database = client.get_database(api_endpoint)
    collection = database.get_collection("products")
    
    products = list(collection.find({}))
    
    print(f"\n{'='*100}")
    print(f"ALL PRODUCTS AND THEIR IMAGES ({len(products)} total)")
    print(f"{'='*100}\n")
    
    for i, product in enumerate(products, 1):
        name = product.get('name', 'Unknown')
        brand = product.get('brand', 'Unknown')
        images = product.get('images', [])
        
        print(f"{i}. {name} ({brand})")
        if images and len(images) > 0:
            print(f"   Image: {images[0]}")
        else:
            print(f"   Image: ❌ NO IMAGE")
        print()

if __name__ == "__main__":
    list_all_products()
