"""
Product models and Cassandra connection management.
"""
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import SimpleStatement
from django.conf import settings
import requests
import logging
import uuid
import json
import os

logger = logging.getLogger(__name__)


class CassandraDB:
    """Cassandra connection manager (supports local and Astra)"""
    _cluster = None
    _session = None
    
    @classmethod
    def get_cluster(cls):
        """Get or create Cassandra cluster"""
        if cls._cluster is None:
            # Check if using Astra (cloud)
            if hasattr(settings, 'ASTRA_SECURE_BUNDLE_PATH') and settings.ASTRA_SECURE_BUNDLE_PATH:
                # Astra connection with secure bundle
                bundle_path = os.path.join(settings.BASE_DIR, settings.ASTRA_SECURE_BUNDLE_PATH)
                
                cloud_config = {
                    'secure_connect_bundle': bundle_path
                }
                
                auth_provider = PlainTextAuthProvider(
                    username='token',
                    password=settings.ASTRA_TOKEN
                )
                
                cls._cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
                logger.info(f"Connected to Astra Cassandra (cloud)")
            else:
                # Local Cassandra connection
                from cassandra.policies import RoundRobinPolicy
                
                cls._cluster = Cluster(
                    contact_points=settings.CASSANDRA_HOSTS,
                    port=settings.CASSANDRA_PORT,
                    load_balancing_policy=RoundRobinPolicy(),
                    protocol_version=4
                )
                logger.info(f"Connected to Cassandra at {settings.CASSANDRA_HOSTS}:{settings.CASSANDRA_PORT}")
        
        return cls._cluster
    
    @classmethod
    def get_session(cls):
        """Get session instance"""
        if cls._session is None:
            cluster = cls.get_cluster()
            cls._session = cluster.connect()
            
            # Use keyspace
            keyspace = getattr(settings, 'ASTRA_DB_KEYSPACE', settings.CASSANDRA_KEYSPACE)
            cls._session.set_keyspace(keyspace)
            logger.info(f"Using keyspace: {keyspace}")
        return cls._session
    
    @classmethod
    def initialize_keyspace(cls):
        """Create keyspace and tables if they don't exist"""
        try:
            cluster = cls.get_cluster()
            session = cluster.connect()
            
            # Create keyspace
            session.execute(f"""
                CREATE KEYSPACE IF NOT EXISTS {settings.CASSANDRA_KEYSPACE}
                WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': 1}}
            """)
            
            session.set_keyspace(settings.CASSANDRA_KEYSPACE)
            
            # Create products table
            session.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id uuid PRIMARY KEY,
                    name text,
                    brand text,
                    category text,
                    price int,
                    description text,
                    specs text,
                    images list<text>,
                    in_stock boolean,
                    stock_quantity int
                )
            """)
            
            # Create index for brand filtering
            try:
                session.execute("CREATE INDEX IF NOT EXISTS ON products (brand)")
            except Exception as e:
                logger.warning(f"Brand index might already exist: {e}")
            
            # Create index for category filtering
            try:
                session.execute("CREATE INDEX IF NOT EXISTS ON products (category)")
            except Exception as e:
                logger.warning(f"Category index might already exist: {e}")
            
            logger.info("Cassandra keyspace and tables initialized")
            session.shutdown()
            cluster.shutdown()
        except Exception as e:
            logger.error(f"Error initializing Cassandra: {e}")
            raise


class Product:
    """Product model for Cassandra operations"""
    
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
        
        # Convert specs dict to JSON string for Cassandra
        if 'specs' in product_data and isinstance(product_data['specs'], dict):
            product_data['specs'] = json.dumps(product_data['specs'])
        
        return product_data
    
    @staticmethod
    def _format_product(row):
        """Format Cassandra row to product dictionary"""
        if not row:
            return None
        
        product = {
            '_id': str(row.id),
            'name': row.name,
            'brand': row.brand,
            'category': row.category,
            'price': row.price,
            'description': row.description,
            'specs': json.loads(row.specs) if row.specs else {},
            'images': list(row.images) if row.images else [],
            'in_stock': row.in_stock,
            'stock_quantity': row.stock_quantity
        }
        
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
        
        session = CassandraDB.get_session()
        product_id = uuid.uuid4()
        
        query = """
            INSERT INTO products (id, name, brand, category, price, description, specs, images, in_stock, stock_quantity)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        session.execute(query, (
            product_id,
            product_data.get('name'),
            product_data.get('brand'),
            product_data.get('category'),
            product_data.get('price'),
            product_data.get('description'),
            product_data.get('specs', '{}'),
            product_data.get('images', []),
            product_data.get('in_stock', True),
            product_data.get('stock_quantity', 0)
        ))
        
        product_data['_id'] = str(product_id)
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
        session = CassandraDB.get_session()
        
        if filters:
            # Build query with filters
            where_clauses = []
            params = []
            
            if 'brand' in filters:
                where_clauses.append("brand = %s")
                params.append(filters['brand'])
            
            if 'category' in filters:
                where_clauses.append("category = %s")
                params.append(filters['category'])
            
            if where_clauses:
                query = f"SELECT * FROM products WHERE {' AND '.join(where_clauses)} ALLOW FILTERING"
                rows = session.execute(query, params)
            else:
                query = "SELECT * FROM products"
                rows = session.execute(query)
        else:
            query = "SELECT * FROM products"
            rows = session.execute(query)
        
        products = [cls._format_product(row) for row in rows]
        
        # Filter by in_stock if specified (post-query filtering)
        if filters and 'in_stock' in filters:
            products = [p for p in products if p['in_stock'] == filters['in_stock']]
        
        return products
    
    @classmethod
    def get_by_id(cls, product_id):
        """
        Get a single product by ID.
        Args:
            product_id: String representation of UUID
        Returns:
            Product document or None
        """
        session = CassandraDB.get_session()
        try:
            query = "SELECT * FROM products WHERE id = %s"
            row = session.execute(query, (uuid.UUID(product_id),)).one()
            return cls._format_product(row)
        except Exception as e:
            logger.error(f"Error fetching product {product_id}: {str(e)}")
            return None
    
    @classmethod
    def update(cls, product_id, data):
        """
        Update a product with image validation.
        Args:
            product_id: String representation of UUID
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
        
        session = CassandraDB.get_session()
        try:
            # Build update query dynamically
            set_clauses = []
            params = []
            
            for key, value in product_data.items():
                if key not in ['_id', 'id']:
                    set_clauses.append(f"{key} = %s")
                    params.append(value)
            
            if not set_clauses:
                return False
            
            params.append(uuid.UUID(product_id))
            query = f"UPDATE products SET {', '.join(set_clauses)} WHERE id = %s"
            
            session.execute(query, params)
            logger.info(f"Updated product: {product_id}")
            return True
        except Exception as e:
            logger.error(f"Error updating product {product_id}: {str(e)}")
            return False
    
    @classmethod
    def delete(cls, product_id):
        """
        Delete a product.
        Args:
            product_id: String representation of UUID
        Returns:
            Boolean indicating success
        """
        session = CassandraDB.get_session()
        try:
            query = "DELETE FROM products WHERE id = %s"
            session.execute(query, (uuid.UUID(product_id),))
            logger.info(f"Deleted product: {product_id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting product {product_id}: {str(e)}")
            return False
