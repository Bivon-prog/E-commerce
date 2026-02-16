"""
Order models using AstraPy (Data API) for Astra
"""
from astrapy import DataAPIClient
from django.conf import settings
import logging
import uuid
from datetime import datetime

logger = logging.getLogger(__name__)


class AstraOrderDB:
    """Astra Data API connection manager for orders"""
    _client = None
    _database = None
    _collection = None
    
    @classmethod
    def get_client(cls):
        """Get or create Astra client"""
        if cls._client is None:
            cls._client = DataAPIClient(settings.ASTRA_TOKEN)
            logger.info("Connected to Astra Data API for orders")
        return cls._client
    
    @classmethod
    def get_database(cls):
        """Get database instance"""
        if cls._database is None:
            client = cls.get_client()
            cls._database = client.get_database_by_api_endpoint(settings.ASTRA_API_ENDPOINT)
            logger.info(f"Using Astra database for orders: {settings.ASTRA_DB_ID}")
        return cls._database
    
    @classmethod
    def get_collection(cls):
        """Get orders collection"""
        if cls._collection is None:
            database = cls.get_database()
            
            # Create collection if it doesn't exist
            try:
                cls._collection = database.get_collection("orders")
                # Test if collection exists by trying to find one document
                cls._collection.find_one({})
            except Exception:
                # Collection doesn't exist, create it
                cls._collection = database.create_collection("orders")
                logger.info("Created orders collection")
            
            logger.info("Using orders collection")
        return cls._collection


class AstraOrder:
    """Order model for Astra Data API operations"""
    
    @staticmethod
    def _format_order(doc):
        """Format Astra document to order dictionary"""
        if not doc:
            return None
        
        order = doc.copy()
        
        # Convert _id to string if it's not already
        if '_id' in order:
            order['_id'] = str(order['_id'])
        
        return order
    
    @classmethod
    def create(cls, data):
        """
        Create a new order.
        Args:
            data: Dictionary containing order data
        Returns:
            Created order document
        """
        collection = AstraOrderDB.get_collection()
        order_id = str(uuid.uuid4())
        
        order_data = {
            '_id': order_id,
            'user_email': data.get('user_email'),
            'items': data.get('items', []),
            'shipping_details': data.get('shipping_details', {}),
            'total': data.get('total', 0),
            'status': 'pending',
            'created_at': datetime.utcnow().isoformat(),
        }
        
        result = collection.insert_one(order_data)
        
        logger.info(f"Created order: {order_id} for {data.get('user_email')}")
        return order_data
    
    @classmethod
    def get_all(cls, filters=None):
        """
        Get all orders with optional filtering.
        Args:
            filters: Dictionary of filter criteria
        Returns:
            List of order documents
        """
        collection = AstraOrderDB.get_collection()
        
        # Build query
        query = {}
        if filters:
            if 'user_email' in filters:
                query['user_email'] = filters['user_email']
            if 'status' in filters:
                query['status'] = filters['status']
        
        # Find documents
        cursor = collection.find(query)
        orders = [cls._format_order(doc) for doc in cursor]
        
        logger.info(f"Retrieved {len(orders)} orders")
        return orders
    
    @classmethod
    def get_by_id(cls, order_id):
        """
        Get a single order by ID.
        Args:
            order_id: String representation of order ID
        Returns:
            Order document or None
        """
        collection = AstraOrderDB.get_collection()
        try:
            doc = collection.find_one({"_id": order_id})
            return cls._format_order(doc)
        except Exception as e:
            logger.error(f"Error fetching order {order_id}: {str(e)}")
            return None
    
    @classmethod
    def get_by_user_email(cls, user_email):
        """
        Get all orders for a specific user.
        Args:
            user_email: User's email address
        Returns:
            List of order documents
        """
        return cls.get_all({'user_email': user_email})
