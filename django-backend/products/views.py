"""
API views for product management.
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, MongoDB
from .serializers import ProductSerializer, CreateProductSerializer
import logging

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
            serializer = ProductSerializer(products, many=True)
            logger.info(f"Retrieved {len(products)} products")
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
def health_check(request):
    """Health check endpoint"""
    try:
        # Test MongoDB connection
        db = MongoDB.get_database()
        db.command('ping')
        
        return Response({
            'status': 'healthy',
            'database': 'connected',
            'message': 'Django backend is running'
        })
    except Exception as e:
        return Response({
            'status': 'unhealthy',
            'database': 'disconnected',
            'error': str(e)
        }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
