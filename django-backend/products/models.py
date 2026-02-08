"""
Product models and MongoDB connection management.
"""
from pymongo import MongoClient
from bson import ObjectId
from django.conf import settings
import requests
import logging

logger = logging.getLogger(__name__)


class MongoDB:
    """MongoDB connection manager"""
    _client = None
    _db = None
    
    @classmethod
    def get_client(cls):
        """Get or create MongoDB client"""
        if cls._client is None:
            cls._client = MongoClient(settings.MONGODB_URI)
            logger.info(f"Connected to MongoDB at {settings.MONGODB_URI}")
        return cls._client
    
    @classmethod
    def get_database(cls):
        """Get database instance"""
        if cls._db is None:
            client = cls.get_client()
            cls._db = client[settings.DATABASE_NAME]
            logger.info(f"Using database: {settings.DATABASE_NAME}")
        return cls._db


class Product:
    """Product model for MongoDB operations"""
    
    COLLECTION_NAME = 'products'
    
    @staticmethod
    def _validate_image_urls(images):
        """
        Validate that image URLs are accessible.
        Args:
            images: List of image URL strings
        Raises:
            ValueError: If any image URL is not accessible
        """
        if not images or not isinstance(images, list):
            raise ValueError("Images must be a non-empty list")
        
        for idx, url in enumerate(images):
            try:
                response = requests.head(url, timeout=5, allow_redirects=True)
                if response.status_code != 200:
                    raise ValueError(
                        f"Image {idx + 1} URL is not accessible (status: {response.status_code}): {url}"
                    )
                logger.info(f"Image {idx + 1} validated: {url}")
            except requests.RequestException as e:
                raise ValueError(f"Failed to validate image {idx + 1} URL: {url}. Error: {str(e)}")
    
    @staticmethod
    def _prepare_product_data(data):
        """
        Prepare product data for storage, ensuring backward compatibility.
        Converts old 'image_url' to 'images' array if needed.
        """
        product_data = data.copy()
        
        # Handle backward compatibility: convert image_url to images array
        if 'image_url' in product_data and 'images' not in product_data:
            product_data['images'] = [product_data.pop('image_url')]
        
        # Ensure images is always a list
        if 'images' in product_data and not isinstance(product_data['images'], list):
            product_data['images'] = [product_data['images']]
        
        return product_data
    
    @classmethod
    def get_collection(cls):
        """Get products collection"""
        db = MongoDB.get_database()
        return db[cls.COLLECTION_NAME]
    
    @classmethod
    def create(cls, data):
        """
        Create a new product with image validation.
        Args:
            data: Dictionary containing product data
        Returns:
            Created product document
        Raises:
            ValueError: If image URLs are invalid
        """
        product_data = cls._prepare_product_data(data)
        
        # Validate image URLs before saving
        if 'images' in product_data:
            cls._validate_image_urls(product_data['images'])
        
        collection = cls.get_collection()
        result = collection.insert_one(product_data)
        product_data['_id'] = result.inserted_id
        
        logger.info(f"Created product: {product_data.get('name')} (ID: {result.inserted_id})")
        return product_data
    
    @classmethod
    def get_all(cls, filters=None):
        """
        Get all products with optional filtering.
        Args:
            filters: Dictionary of filter criteria
        Returns:
            List of product documents
        """
        collection = cls.get_collection()
        query = filters or {}
        products = list(collection.find(query))
        
        # Convert ObjectId to string for JSON serialization
        for product in products:
            product['_id'] = str(product['_id'])
            # Ensure backward compatibility: add images if only image_url exists
            if 'image_url' in product and 'images' not in product:
                product['images'] = [product['image_url']]
        
        return products
    
    @classmethod
    def get_by_id(cls, product_id):
        """
        Get a single product by ID.
        Args:
            product_id: String representation of ObjectId
        Returns:
            Product document or None
        """
        collection = cls.get_collection()
        try:
            product = collection.find_one({'_id': ObjectId(product_id)})
            if product:
                product['_id'] = str(product['_id'])
                # Ensure backward compatibility
                if 'image_url' in product and 'images' not in product:
                    product['images'] = [product['image_url']]
            return product
        except Exception as e:
            logger.error(f"Error fetching product {product_id}: {str(e)}")
            return None
    
    @classmethod
    def update(cls, product_id, data):
        """
        Update a product with image validation.
        Args:
            product_id: String representation of ObjectId
            data: Dictionary containing updated product data
        Returns:
            Boolean indicating success
        Raises:
            ValueError: If image URLs are invalid
        """
        product_data = cls._prepare_product_data(data)
        
        # Validate image URLs if provided
        if 'images' in product_data:
            cls._validate_image_urls(product_data['images'])
        
        collection = cls.get_collection()
        try:
            result = collection.update_one(
                {'_id': ObjectId(product_id)},
                {'$set': product_data}
            )
            success = result.modified_count > 0
            if success:
                logger.info(f"Updated product: {product_id}")
            return success
        except Exception as e:
            logger.error(f"Error updating product {product_id}: {str(e)}")
            return False
    
    @classmethod
    def delete(cls, product_id):
        """
        Delete a product.
        Args:
            product_id: String representation of ObjectId
        Returns:
            Boolean indicating success
        """
        collection = cls.get_collection()
        try:
            result = collection.delete_one({'_id': ObjectId(product_id)})
            success = result.deleted_count > 0
            if success:
                logger.info(f"Deleted product: {product_id}")
            return success
        except Exception as e:
            logger.error(f"Error deleting product {product_id}: {str(e)}")
            return False
