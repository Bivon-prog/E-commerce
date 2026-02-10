"""
Mock product models for running without database
"""
import uuid
import json
import logging
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)

# In-memory storage
MOCK_PRODUCTS = []

class MockProduct:
    """Mock Product model for in-memory operations"""
    
    @staticmethod
    def _validate_image_urls(images):
        """Mock validation - always passes"""
        if not images or not isinstance(images, list):
            raise ValueError("Images must be a non-empty list")
        logger.info(f"Mock: Validated {len(images)} images")
    
    @staticmethod
    def _prepare_product_data(data):
        """Prepare product data, ensuring backward compatibility"""
        product_data = data.copy()
        
        # Handle backward compatibility: convert image_url to images array
        if 'image_url' in product_data and 'images' not in product_data:
            product_data['images'] = [product_data.pop('image_url')]
        
        # Ensure images is always a list
        if 'images' in product_data and not isinstance(product_data['images'], list):
            product_data['images'] = [product_data['images']]
        
        return product_data
    
    @classmethod
    def create(cls, data):
        """Create a new product in memory"""
        product_data = cls._prepare_product_data(data)
        
        # Mock validation
        if 'images' in product_data:
            cls._validate_image_urls(product_data['images'])
        
        product_id = str(uuid.uuid4())
        product_data['_id'] = product_id
        
        MOCK_PRODUCTS.append(product_data)
        logger.info(f"Mock: Created product {product_data.get('name')} (ID: {product_id})")
        
        return product_data
    
    @classmethod
    def get_all(cls, filters=None):
        """Get all products with optional filtering"""
        products = MOCK_PRODUCTS.copy()
        
        if filters:
            if 'brand' in filters:
                products = [p for p in products if p.get('brand') == filters['brand']]
            if 'category' in filters:
                products = [p for p in products if p.get('category') == filters['category']]
            if 'in_stock' in filters:
                products = [p for p in products if p.get('in_stock') == filters['in_stock']]
        
        logger.info(f"Mock: Retrieved {len(products)} products")
        return products
    
    @classmethod
    def get_by_id(cls, product_id):
        """Get a single product by ID"""
        for product in MOCK_PRODUCTS:
            if product['_id'] == product_id:
                return product
        return None
    
    @classmethod
    def update(cls, product_id, data):
        """Update a product"""
        product_data = cls._prepare_product_data(data)
        
        # Mock validation
        if 'images' in product_data:
            cls._validate_image_urls(product_data['images'])
        
        for i, product in enumerate(MOCK_PRODUCTS):
            if product['_id'] == product_id:
                MOCK_PRODUCTS[i].update(product_data)
                logger.info(f"Mock: Updated product {product_id}")
                return True
        
        return False
    
    @classmethod
    def delete(cls, product_id):
        """Delete a product"""
        for i, product in enumerate(MOCK_PRODUCTS):
            if product['_id'] == product_id:
                del MOCK_PRODUCTS[i]
                logger.info(f"Mock: Deleted product {product_id}")
                return True
        
        return False

# Initialize with some sample data
def initialize_mock_data():
    """Add some sample products"""
    if MOCK_PRODUCTS:  # Already initialized
        return
    
    sample_products = [
        {
            "name": "iPhone 15 Pro",
            "brand": "Apple",
            "category": "Phone",
            "price": 14999900,  # KES in cents
            "description": "The most advanced iPhone ever with titanium design and A17 Pro chip.",
            "specs": {
                "screen_size": "6.1 inch Super Retina XDR",
                "ram": "8GB",
                "storage": "256GB",
                "battery": "Up to 23 hours video playback",
                "camera": "48MP Main | Ultra Wide | Telephoto",
                "processor": "A17 Pro chip"
            },
            "images": [
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-naturaltitanium?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-naturaltitanium_AV2?wid=400&hei=300&fmt=p-jpg&qlt=80",
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-naturaltitanium_AV3?wid=400&hei=300&fmt=p-jpg&qlt=80"
            ],
            "in_stock": True,
            "stock_quantity": 25
        },
        {
            "name": "Samsung Galaxy S24 Ultra",
            "brand": "Samsung",
            "category": "Phone",
            "price": 13999900,
            "description": "The ultimate Galaxy experience with S Pen and AI features.",
            "specs": {
                "screen_size": "6.8 inch Dynamic AMOLED 2X",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "5000 mAh",
                "camera": "200MP Main | Ultra Wide | Telephoto",
                "processor": "Snapdragon 8 Gen 3"
            },
            "images": [
                "https://images.samsung.com/is/image/samsung/p6pim/in/2401/gallery/in-galaxy-s24-ultra-s928-sm-s928bztqins-thumb-539573828?$344_344_PNG$",
                "https://images.samsung.com/is/image/samsung/p6pim/in/2401/gallery/in-galaxy-s24-ultra-s928-sm-s928bztqins-thumb-539573829?$344_344_PNG$"
            ],
            "in_stock": True,
            "stock_quantity": 18
        },
        {
            "name": "Google Pixel 8 Pro",
            "brand": "Google",
            "category": "Phone",
            "price": 11999900,
            "description": "The most advanced Pixel phone with Google AI and the best Pixel Camera.",
            "specs": {
                "screen_size": "6.7 inch Super Actua display",
                "ram": "12GB",
                "storage": "256GB",
                "battery": "5050 mAh",
                "camera": "50 MP Octa PD wide camera",
                "processor": "Google Tensor G3"
            },
            "images": [
                "https://lh3.googleusercontent.com/Nu3a6F80WfixUqf_ec_vgXy_c0-0r4VLJRXjVFF_X_Yk3ijzE5UHc8S53EQVQ8k0wHSjigZzNA=s0-e365-rw",
                "https://lh3.googleusercontent.com/Nu3a6F80WfixUqf_ec_vgXy_c0-0r4VLJRXjVFF_X_Yk3ijzE5UHc8S53EQVQ8k0wHSjigZzNA=s0-e365-rw"
            ],
            "in_stock": True,
            "stock_quantity": 12
        }
    ]
    
    for product_data in sample_products:
        MockProduct.create(product_data)
    
    logger.info(f"Mock: Initialized with {len(sample_products)} sample products")

# Initialize on import
initialize_mock_data()