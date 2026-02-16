"""
URL routing for products API.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('health', views.health_check, name='health-check'),
    path('products', views.product_list, name='product-list'),
    path('products/<str:product_id>', views.product_detail, name='product-detail'),
    path('filter-options', views.filter_options, name='filter-options'),
    path('orders', views.create_order, name='create-order'),
    path('orders/user', views.get_user_orders, name='get-user-orders'),
]
