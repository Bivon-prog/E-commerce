"""
Product models using AstraPy (Data API) for Astra
"""
from astrapy import DataAPIClient
from django.conf import settings
import requests
import logging
import uuid
import json

logger = logging.getLogger(__name__)


class AstraDB:
    """Astra Data API connection manager"""
    _client = None
    _database = None
    _collection = None
    
    @classmethod
    def get_client(cls):
        """Get or create Astra client"""
        if cls._client is None:
            cls._client = DataAPIClient(settings.ASTRA_TOKEN)
            logger.info("Connected to Astra Data API")
        return cls._client
    
    @classmethod
    def get_database(cls):
        """Get database instance"""
        if cls._database is None:
            client = cls.get_client()
            cls._database = client.get_database_by_api_endpoint(settings.ASTRA_API_ENDPOINT)
            logger.info(f"Using Astra database: {settings.ASTRA_DB_ID}")
        return cls._database
    
    @classmethod
    def get_collection(cls):
        """Get products collection"""
        if cls._collection is None:
            database = cls.get_database()
            
            # Create collection if it doesn't exist
            try:
                cls._collection = database.get_collection("products")
                # Test if collection exists by trying to find one document
                cls._collection.find_one({})
            except Exception:
                # Collection doesn't exist, create it
                cls._collection = database.create_collection("products")
                logger.info("Created products collection")
            
            logger.info("Using products collection")
        return cls._collection


class AstraProduct:
    """Product model for Astra Data API operations"""
    
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
    
    @staticmethod
    def _format_product(doc):
        """Format Astra document to product dictionary"""
        if not doc:
            return None
        
        product = doc.copy()
        
        # Convert _id to string if it's not already
        if '_id' in product:
            product['_id'] = str(product['_id'])
        
        return product
    
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
        
        collection = AstraDB.get_collection()
        product_id = str(uuid.uuid4())
        product_data['_id'] = product_id
        
        result = collection.insert_one(product_data)
        
        logger.info(f"Created product: {product_data.get('name')} (ID: {product_id})")
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
        collection = AstraDB.get_collection()
        
        # Build query
        query = {}
        if filters:
            if 'brand' in filters:
                query['brand'] = filters['brand']
            if 'category' in filters:
                query['category'] = filters['category']
            if 'in_stock' in filters:
                query['in_stock'] = filters['in_stock']
        
        # Find documents
        cursor = collection.find(query)
        products = [cls._format_product(doc) for doc in cursor]
        
        logger.info(f"Retrieved {len(products)} products")
        return products
    
    @classmethod
    def get_by_id(cls, product_id):
        """
        Get a single product by ID.
        Args:
            product_id: String representation of product ID
        Returns:
            Product document or None
        """
        collection = AstraDB.get_collection()
        try:
            doc = collection.find_one({"_id": product_id})
            return cls._format_product(doc)
        except Exception as e:
            logger.error(f"Error fetching product {product_id}: {str(e)}")
            return None
    
    @classmethod
    def update(cls, product_id, data):
        """
        Update a product with image validation.
        Args:
            product_id: String representation of product ID
            data: Dictionary containing updated product data
        Returns:
            Boolean indicating success
        Raises:
            ValueError: If image URLs are invalid
        """
        product_data = cls._prepare_product_data(data)
        
        # Remove _id field from update data (cannot be updated)
        if '_id' in product_data:
            del product_data['_id']
        
        # Validate image URLs if provided
        if 'images' in product_data:
            cls._validate_image_urls(product_data['images'])
        
        collection = AstraDB.get_collection()
        try:
            result = collection.update_one(
                {"_id": product_id},
                {"$set": product_data}
            )
            # For Astra Data API, check if the operation was successful
            success = result is not None
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
            product_id: String representation of product ID
        Returns:
            Boolean indicating success
        """
        collection = AstraDB.get_collection()
        try:
            result = collection.delete_one({"_id": product_id})
            success = result.deleted_count > 0
            if success:
                logger.info(f"Deleted product: {product_id}")
            return success
        except Exception as e:
            logger.error(f"Error deleting product {product_id}: {str(e)}")
            return False