"""
API views for product management.
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, CreateProductSerializer
import logging
import os

# Choose the right model based on configuration
if os.getenv('USE_MOCK_DB', 'false').lower() == 'true':
    from .mock_models import MockProduct as Product
    DB_TYPE = "mock"
elif os.getenv('ASTRA_TOKEN') and os.getenv('ASTRA_API_ENDPOINT'):
    try:
        from .astra_models import AstraProduct as Product
        DB_TYPE = "astra"
    except ImportError:
        from .mock_models import MockProduct as Product
        DB_TYPE = "mock (astra unavailable)"
else:
    try:
        from .models import Product
        DB_TYPE = "cassandra"
    except Exception:
        from .mock_models import MockProduct as Product
        DB_TYPE = "mock (fallback)"

logger = logging.getLogger(__name__)

logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def product_list(request):
    """
    GET: List all products with optional filtering
    POST: Create a new product
    """
    if request.method == 'GET':
        # Get query parameters for filtering
        filters = {}
        if request.GET.get('brand'):
            filters['brand'] = request.GET.get('brand')
        if request.GET.get('category'):
            filters['category'] = request.GET.get('category')
        if request.GET.get('in_stock'):
            filters['in_stock'] = request.GET.get('in_stock').lower() == 'true'
        
        logger.info(f"Fetching products with filters: {filters}")
        
        try:
            products = Product.get_all(filters)
            
            # Apply additional filtering based on specs (comprehensive categories)
            filtered_products = products
            
            # Filter by price tier
            if request.GET.get('price_tier'):
                price_tier = request.GET.get('price_tier')
                filtered_products = [p for p in filtered_products 
                                   if p.get('specs', {}).get('price_tier') == price_tier]
            
            # Filter by use case
            if request.GET.get('use_case'):
                use_case = request.GET.get('use_case')
                filtered_products = [p for p in filtered_products 
                                   if p.get('specs', {}).get('use_case') == use_case]
            
            # Filter by form factor
            if request.GET.get('form_factor'):
                form_factor = request.GET.get('form_factor')
                filtered_products = [p for p in filtered_products 
                                   if p.get('specs', {}).get('form_factor') == form_factor]
            
            # Filter by software experience
            if request.GET.get('software_experience'):
                software_experience = request.GET.get('software_experience')
                filtered_products = [p for p in filtered_products 
                                   if p.get('specs', {}).get('software_experience') == software_experience]
            
            # Filter by chipset category
            if request.GET.get('chipset_category'):
                chipset_category = request.GET.get('chipset_category')
                filtered_products = [p for p in filtered_products 
                                   if p.get('specs', {}).get('chipset_category') == chipset_category]
            
            # Filter by market origin
            if request.GET.get('market_origin'):
                market_origin = request.GET.get('market_origin')
                filtered_products = [p for p in filtered_products 
                                   if p.get('specs', {}).get('market_origin') == market_origin]
            
            # Filter by target demographic
            if request.GET.get('target_demographic'):
                target_demographic = request.GET.get('target_demographic')
                filtered_products = [p for p in filtered_products 
                                   if p.get('specs', {}).get('target_demographic') == target_demographic]
            
            # Filter by price range
            if request.GET.get('min_price'):
                min_price = int(request.GET.get('min_price'))
                filtered_products = [p for p in filtered_products if p.get('price', 0) >= min_price]
            
            if request.GET.get('max_price'):
                max_price = int(request.GET.get('max_price'))
                filtered_products = [p for p in filtered_products if p.get('price', 0) <= max_price]
            
            serializer = ProductSerializer(filtered_products, many=True)
            logger.info(f"Retrieved {len(filtered_products)} products after filtering")
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error fetching products: {str(e)}")
            return Response(
                {'error': 'Failed to fetch products', 'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    elif request.method == 'POST':
        serializer = CreateProductSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                logger.info(f"Creating product: {serializer.validated_data.get('name')}")
                product = Product.create(serializer.validated_data)
                response_serializer = ProductSerializer(product)
                logger.info(f"Product created successfully: {product['_id']}")
                return Response(
                    {
                        'message': 'Product created successfully',
                        'product': response_serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
            except ValueError as e:
                logger.warning(f"Image validation failed: {str(e)}")
                return Response(
                    {'error': 'Invalid image URL', 'message': str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            except Exception as e:
                logger.error(f"Error creating product: {str(e)}")
                return Response(
                    {'error': 'Failed to create product', 'message': str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, product_id):
    """
    GET: Retrieve a single product
    PUT: Update a product
    DELETE: Delete a product
    """
    if request.method == 'GET':
        try:
            product = Product.get_by_id(product_id)
            if product:
                serializer = ProductSerializer(product)
                return Response(serializer.data)
            else:
                return Response(
                    {'error': 'Product not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            logger.error(f"Error fetching product {product_id}: {str(e)}")
            return Response(
                {'error': 'Failed to fetch product', 'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    elif request.method == 'PUT':
        serializer = CreateProductSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                # Disable image validation for updates (allow any URL)
                if DB_TYPE == "astra":
                    success = Product.update(product_id, serializer.validated_data, validate_images=False)
                else:
                    success = Product.update(product_id, serializer.validated_data)
                
                if success:
                    product = Product.get_by_id(product_id)
                    response_serializer = ProductSerializer(product)
                    return Response(
                        {
                            'message': 'Product updated successfully',
                            'product': response_serializer.data
                        }
                    )
                else:
                    return Response(
                        {'error': 'Product not found'},
                        status=status.HTTP_404_NOT_FOUND
                    )
            except ValueError as e:
                return Response(
                    {'error': 'Invalid image URL', 'message': str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            except Exception as e:
                logger.error(f"Error updating product {product_id}: {str(e)}")
                return Response(
                    {'error': 'Failed to update product', 'message': str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            success = Product.delete(product_id)
            if success:
                return Response(
                    {'message': 'Product deleted successfully'},
                    status=status.HTTP_204_NO_CONTENT
                )
            else:
                return Response(
                    {'error': 'Product not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            logger.error(f"Error deleting product {product_id}: {str(e)}")
            return Response(
                {'error': 'Failed to delete product', 'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(['GET'])
def filter_options(request):
    """Get all available filter options for the comprehensive categorization system"""
    try:
        products = Product.get_all()
        
        filter_options = {
            'brands': set(),
            'price_tiers': set(),
            'use_cases': set(),
            'form_factors': set(),
            'software_experiences': set(),
            'chipset_categories': set(),
            'market_origins': set(),
            'target_demographics': set(),
            'price_range': {'min': float('inf'), 'max': 0}
        }
        
        for product in products:
            # Basic filters
            filter_options['brands'].add(product.get('brand'))
            
            # Price range
            price = product.get('price', 0)
            if price > 0:
                filter_options['price_range']['min'] = min(filter_options['price_range']['min'], price)
                filter_options['price_range']['max'] = max(filter_options['price_range']['max'], price)
            
            # Comprehensive category filters from specs
            specs = product.get('specs', {})
            if specs.get('price_tier'):
                filter_options['price_tiers'].add(specs['price_tier'])
            if specs.get('use_case'):
                filter_options['use_cases'].add(specs['use_case'])
            if specs.get('form_factor'):
                filter_options['form_factors'].add(specs['form_factor'])
            if specs.get('software_experience'):
                filter_options['software_experiences'].add(specs['software_experience'])
            if specs.get('chipset_category'):
                filter_options['chipset_categories'].add(specs['chipset_category'])
            if specs.get('market_origin'):
                filter_options['market_origins'].add(specs['market_origin'])
            if specs.get('target_demographic'):
                filter_options['target_demographics'].add(specs['target_demographic'])
        
        # Convert sets to sorted lists
        response_data = {
            'brands': sorted(list(filter_options['brands'])),
            'price_tiers': sorted(list(filter_options['price_tiers'])),
            'use_cases': sorted(list(filter_options['use_cases'])),
            'form_factors': sorted(list(filter_options['form_factors'])),
            'software_experiences': sorted(list(filter_options['software_experiences'])),
            'chipset_categories': sorted(list(filter_options['chipset_categories'])),
            'market_origins': sorted(list(filter_options['market_origins'])),
            'target_demographics': sorted(list(filter_options['target_demographics'])),
            'price_range': {
                'min': int(filter_options['price_range']['min']) if filter_options['price_range']['min'] != float('inf') else 0,
                'max': int(filter_options['price_range']['max'])
            }
        }
        
        return Response(response_data)
    
    except Exception as e:
        logger.error(f"Error getting filter options: {str(e)}")
        return Response(
            {'error': 'Failed to get filter options', 'message': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def health_check(request):
    """Health check endpoint"""
    try:
        # Check database type and connection
        if DB_TYPE == "mock":
            return Response({
                'status': 'healthy',
                'database': 'mock (in-memory)',
                'message': 'Django backend is running with mock database'
            })
        elif DB_TYPE == "astra":
            # Test Astra connection
            from .astra_models import AstraDB
            database = AstraDB.get_database()
            collections = database.list_collection_names()
            
            return Response({
                'status': 'healthy',
                'database': 'astra (connected)',
                'message': 'Django backend is running with Astra database',
                'collections': collections
            })
        elif DB_TYPE == "cassandra":
            # Test Cassandra connection
            from .models import CassandraDB
            session = CassandraDB.get_session()
            session.execute("SELECT now() FROM system.local")
            
            return Response({
                'status': 'healthy',
                'database': 'cassandra (connected)',
                'message': 'Django backend is running with Cassandra'
            })
        else:
            return Response({
                'status': 'healthy',
                'database': f'{DB_TYPE}',
                'message': f'Django backend is running with {DB_TYPE} database'
            })
    except Exception as e:
        # Fallback response
        return Response({
            'status': 'healthy',
            'database': f'{DB_TYPE} (error)',
            'message': f'Django backend is running but database has issues: {str(e)}',
            'warning': 'Some features may not work properly'
        })


@api_view(['POST'])
def create_order(request):
    """
    Create a new order and save it to the database
    """
    try:
        from .order_models import AstraOrder
        
        items = request.data.get('items', [])
        shipping_details = request.data.get('shippingDetails', {})
        user_email = request.data.get('userEmail', shipping_details.get('email', ''))
        
        if not items:
            return Response(
                {'error': 'No items in order'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Calculate total
        total = sum(item.get('price', 0) * item.get('quantity', 0) for item in items)
        
        # Create order in database
        order_data = {
            'user_email': user_email,
            'items': items,
            'shipping_details': shipping_details,
            'total': total
        }
        
        order = AstraOrder.create(order_data)
        
        logger.info(f"Order created: {order['_id']}, Total: KES {total/100:.2f}")
        
        # Return success response
        return Response(
            {
                'message': 'Order placed successfully',
                'order_id': order['_id'],
                'total': total,
                'items_count': len(items)
            },
            status=status.HTTP_201_CREATED
        )
    except Exception as e:
        logger.error(f"Error creating order: {str(e)}")
        return Response(
            {'error': 'Failed to create order', 'message': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def get_user_orders(request):
    """
    Get all orders for the authenticated user
    """
    try:
        from .order_models import AstraOrder
        
        # Get user email from query parameter
        user_email = request.GET.get('email')
        
        if not user_email:
            return Response(
                {'error': 'Email parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Get orders for this user
        orders = AstraOrder.get_by_user_email(user_email)
        
        # Sort by created_at descending (newest first)
        orders.sort(key=lambda x: x.get('created_at', ''), reverse=True)
        
        logger.info(f"Retrieved {len(orders)} orders for {user_email}")
        
        return Response(orders)
    except Exception as e:
        logger.error(f"Error fetching orders: {str(e)}")
        return Response(
            {'error': 'Failed to fetch orders', 'message': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
