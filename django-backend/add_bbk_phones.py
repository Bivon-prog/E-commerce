#!/usr/bin/env python3
"""
Add BBK Electronics phones (OPPO, vivo, OnePlus, Realme, iQOO) to Astra database
Total: ~150 phones across 5 brands
"""

import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from products.astra_models import AstraProduct

def get_generic_images(count=3):
    """Get generic smartphone images"""
    images = [
        "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=470&h=556&fit=crop",
        "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=470&h=556&fit=crop",
        "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=470&h=556&fit=crop"
    ]
    return images[:count]

def add_phones():
    """Add all BBK Electronics phones"""
    
    phones_data = []
    
    # ==================== OPPO (50 models) ====================
    print("Adding OPPO phones...")
    
    # OPPO Find N Series - Foldables (6 models)
    oppo_find_n = [
        ("OPPO Find N5", 179999, "Latest book-style foldable", "12GB/16GB", "256GB/512GB", "7.82\" Foldable", "Snapdragon 8 Gen 3", "50MP Triple", "4805mAh", "Ultra-Premium", "Foldable Book"),
        ("OPPO Find N3", 149999, "Premium book-style foldable with Hasselblad", "12GB/16GB", "256GB/512GB", "7.82\" Foldable", "Snapdragon 8 Gen 2", "48MP Hasselblad", "4805mAh", "Premium Flagship", "Foldable Book"),
        ("OPPO Find N2", 119999, "Compact book-style foldable", "12GB/16GB", "256GB/512GB", "7.1\" Foldable", "Snapdragon 8+ Gen 1", "50MP Triple", "4520mAh", "Premium Flagship", "Foldable Book"),
        ("OPPO Find N5 Flip", 89999, "Latest clamshell foldable", "12GB", "256GB/512GB", "6.8\" Foldable", "Dimensity 9300", "50MP Dual", "4300mAh", "Premium Flagship", "Foldable Clamshell"),
        ("OPPO Find N3 Flip", 79999, "Stylish clamshell with vertical camera", "12GB", "256GB", "6.8\" Foldable", "Dimensity 9200", "50MP Triple", "4300mAh", "Premium Flagship", "Foldable Clamshell"),
        ("OPPO Find N2 Flip", 69999, "Compact flip phone", "8GB/12GB", "256GB", "6.8\" Foldable", "Dimensity 9000+", "50MP Dual", "4300mAh", "Flagship Killer", "Foldable Clamshell"),
    ]
    
    # OPPO Find X Series - Premium Flagship (9 models)
    oppo_find_x = [
        ("OPPO Find X9 Ultra", 139999, "Ultimate flagship with Hasselblad quad camera", "12GB/16GB", "256GB/512GB/1TB", "6.82\" AMOLED 120Hz", "Snapdragon 8 Gen 4", "50MP Hasselblad Quad", "5000mAh", "Ultra-Premium", "Candy Bar"),
        ("OPPO Find X9 Pro", 109999, "Premium flagship with advanced camera", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 120Hz", "Snapdragon 8 Gen 4", "50MP Hasselblad Triple", "5000mAh", "Premium Flagship", "Candy Bar"),
        ("OPPO Find X9", 89999, "Flagship with balanced features", "12GB", "256GB/512GB", "6.7\" AMOLED 120Hz", "Snapdragon 8 Gen 4", "50MP Triple", "4800mAh", "Premium Flagship", "Candy Bar"),
        ("OPPO Find X8 Ultra", 129999, "Photography powerhouse with dual periscope", "12GB/16GB", "256GB/512GB", "6.82\" AMOLED 120Hz", "Snapdragon 8 Gen 3", "50MP Hasselblad Quad", "5000mAh", "Ultra-Premium", "Candy Bar"),
        ("OPPO Find X8 Pro", 99999, "Premium flagship with curved display", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 120Hz", "Snapdragon 8 Gen 3", "50MP Hasselblad Triple", "5000mAh", "Premium Flagship", "Candy Bar"),
        ("OPPO Find X8", 79999, "Flagship with excellent camera", "12GB", "256GB/512GB", "6.7\" AMOLED 120Hz", "Snapdragon 8 Gen 3", "50MP Triple", "4800mAh", "Flagship Killer", "Candy Bar"),
        ("OPPO Find X7 Ultra", 119999, "Camera-centric flagship", "12GB/16GB", "256GB/512GB", "6.82\" AMOLED 120Hz", "Snapdragon 8 Gen 3", "50MP Hasselblad Quad", "5000mAh", "Ultra-Premium", "Candy Bar"),
        ("OPPO Find X7", 84999, "Flagship with great performance", "12GB", "256GB/512GB", "6.7\" AMOLED 120Hz", "Dimensity 9300", "50MP Triple", "4800mAh", "Flagship Killer", "Candy Bar"),
        ("OPPO Find X6 Pro", 94999, "Previous gen flagship", "12GB/16GB", "256GB/512GB", "6.82\" AMOLED 120Hz", "Snapdragon 8 Gen 2", "50MP Triple", "5000mAh", "Premium Flagship", "Candy Bar"),
    ]
    
    # OPPO Reno Series - Mid-Range (20 models)
    oppo_reno = [
        # Reno 15 Series
        ("OPPO Reno 15 Pro+", 54999, "Premium mid-range with portrait focus", "12GB", "256GB/512GB", "6.7\" AMOLED 120Hz", "Dimensity 9200+", "50MP Triple", "4700mAh", "Mid-Range", "Candy Bar"),
        ("OPPO Reno 15 Pro", 47999, "Portrait expert mid-ranger", "8GB/12GB", "256GB", "6.7\" AMOLED 120Hz", "Dimensity 8300", "50MP Triple", "4600mAh", "Mid-Range", "Candy Bar"),
        ("OPPO Reno 15", 39999, "Stylish mid-range phone", "8GB", "256GB", "6.7\" AMOLED 90Hz", "Dimensity 7300", "50MP Dual", "5000mAh", "Mid-Range", "Candy Bar"),
        ("OPPO Reno 15 F", 34999, "Fashion-focused mid-ranger", "8GB", "256GB", "6.67\" AMOLED 90Hz", "Snapdragon 7 Gen 1", "64MP Triple", "5000mAh", "Mid-Range", "Candy Bar"),
        # Reno 14 Series
        ("OPPO Reno 14 Pro+", 52999, "Premium portrait phone", "12GB", "256GB/512GB", "6.7\" AMOLED 120Hz", "Dimensity 9200", "50MP Triple", "4700mAh", "Mid-Range", "Candy Bar"),
        ("OPPO Reno 14 Pro", 45999, "Portrait photography specialist", "8GB/12GB", "256GB", "6.7\" AMOLED 120Hz", "Dimensity 8200", "50MP Triple", "4600mAh", "Mid-Range", "Candy Bar"),
        ("OPPO Reno 14", 37999, "Balanced mid-range option", "8GB", "256GB", "6.7\" AMOLED 90Hz", "Dimensity 7200", "50MP Dual", "5000mAh", "Mid-Range", "Candy Bar"),
        ("OPPO Reno 14 F", 32999, "Stylish and affordable", "8GB", "256GB", "6.67\" AMOLED 90Hz", "Snapdragon 7 Gen 1", "64MP Triple", "5000mAh", "Budget", "Candy Bar"),
        # Reno 13 Series
        ("OPPO Reno 13 Pro+", 49999, "Premium mid-range camera phone", "12GB", "256GB", "6.7\" AMOLED 120Hz", "Dimensity 9000+", "50MP Triple", "4500mAh", "Mid-Range", "Candy Bar"),
        ("OPPO Reno 13 Pro", 43999, "Portrait mode specialist", "8GB/12GB", "256GB", "6.7\" AMOLED 120Hz", "Dimensity 8100", "50MP Triple", "4500mAh", "Mid-Range", "Candy Bar"),
        ("OPPO Reno 13 5G", 35999, "5G mid-ranger", "8GB", "256GB", "6.7\" AMOLED 90Hz", "Dimensity 7050", "64MP Dual", "5000mAh", "Mid-Range", "Candy Bar"),
        # Reno 12 Series
        ("OPPO Reno 12 Pro", 41999, "Mid-range with great cameras", "8GB/12GB", "256GB", "6.7\" AMOLED 120Hz", "Dimensity 7300", "50MP Triple", "5000mAh", "Mid-Range", "Candy Bar"),
        ("OPPO Reno 12", 33999, "Affordable mid-range option", "8GB", "256GB", "6.7\" AMOLED 90Hz", "Dimensity 7050", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("OPPO Reno 12 F", 29999, "Budget-friendly Reno", "8GB", "256GB", "6.67\" AMOLED 90Hz", "Snapdragon 6 Gen 1", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        # Reno 11 Series
        ("OPPO Reno 11 Pro", 39999, "Previous gen mid-range pro", "12GB", "256GB", "6.7\" AMOLED 120Hz", "Dimensity 8200", "50MP Triple", "4600mAh", "Mid-Range", "Candy Bar"),
        ("OPPO Reno 11", 31999, "Reliable mid-ranger", "8GB", "256GB", "6.7\" AMOLED 90Hz", "Dimensity 7050", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("OPPO Reno 11 F", 27999, "Entry mid-range", "8GB", "256GB", "6.67\" AMOLED 90Hz", "Snapdragon 6 Gen 1", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        # Reno 10 Series
        ("OPPO Reno 10 Pro+", 44999, "Premium Reno 10", "12GB", "256GB", "6.74\" AMOLED 120Hz", "Snapdragon 8+ Gen 1", "50MP Triple", "4700mAh", "Mid-Range", "Candy Bar"),
        ("OPPO Reno 10 Pro", 37999, "Mid-range Reno 10", "12GB", "256GB", "6.7\" AMOLED 120Hz", "Snapdragon 778G", "50MP Triple", "4600mAh", "Mid-Range", "Candy Bar"),
        ("OPPO Reno 10", 29999, "Standard Reno 10", "8GB", "256GB", "6.7\" AMOLED 90Hz", "Dimensity 7050", "64MP Triple", "5000mAh", "Budget", "Candy Bar"),
    ]
    
    # OPPO A Series - Budget (10 models)
    oppo_a = [
        ("OPPO A98 5G", 32999, "High-end A series with 5G", "8GB", "256GB", "6.72\" LCD 120Hz", "Snapdragon 695", "64MP Triple", "5000mAh", "Budget", "Candy Bar"),
        ("OPPO A80 5G", 27999, "Mid-range 5G phone", "8GB", "128GB/256GB", "6.67\" LCD 120Hz", "Dimensity 6100+", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("OPPO A79 5G", 24999, "Affordable 5G option", "8GB", "128GB/256GB", "6.72\" LCD 90Hz", "Dimensity 6020", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("OPPO A78", 22999, "Budget 4G/5G phone", "8GB", "128GB/256GB", "6.56\" LCD 90Hz", "Snapdragon 680", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("OPPO A60", 19999, "Mid-budget option", "8GB", "128GB/256GB", "6.67\" LCD 90Hz", "Snapdragon 680", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("OPPO A58", 17999, "Affordable smartphone", "6GB/8GB", "128GB", "6.56\" LCD 90Hz", "Dimensity 700", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("OPPO A38", 15999, "Entry-level A series", "4GB/6GB", "128GB", "6.56\" LCD 90Hz", "Helio G85", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("OPPO A3 Pro", 18999, "Budget pro model", "8GB", "128GB/256GB", "6.67\" LCD 120Hz", "Snapdragon 695", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("OPPO A18", 13999, "Basic smartphone", "4GB/6GB", "128GB", "6.56\" LCD 90Hz", "Helio G85", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("OPPO A17k", 11999, "Entry-level phone", "3GB/4GB", "64GB/128GB", "6.56\" LCD", "Helio G35", "8MP Single", "5000mAh", "Entry-Level", "Candy Bar"),
    ]
    
    # OPPO F Series - Fashion (5 models)
    oppo_f = [
        ("OPPO F29 Pro", 29999, "Fashion-focused with great selfie camera", "8GB", "256GB", "6.67\" AMOLED 120Hz", "Dimensity 7050", "64MP Triple", "5000mAh", "Budget", "Candy Bar"),
        ("OPPO F27 Pro+", 27999, "Premium F series", "8GB", "256GB", "6.67\" AMOLED 120Hz", "Dimensity 7050", "64MP Triple", "5000mAh", "Budget", "Candy Bar"),
        ("OPPO F27 5G", 24999, "5G fashion phone", "8GB", "128GB/256GB", "6.67\" AMOLED 90Hz", "Dimensity 6100+", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("OPPO F25 Pro", 25999, "Stylish mid-ranger", "8GB", "128GB/256GB", "6.67\" AMOLED 120Hz", "Dimensity 7050", "64MP Triple", "5000mAh", "Budget", "Candy Bar"),
        ("OPPO F23 5G", 22999, "Affordable fashion 5G", "8GB", "128GB", "6.72\" LCD 120Hz", "Snapdragon 695", "64MP Triple", "5000mAh", "Budget", "Candy Bar"),
    ]

    
    # ==================== vivo (50 models) ====================
    print("Adding vivo phones...")
    
    # vivo X Fold Series - Foldables (5 models)
    vivo_x_fold = [
        ("vivo X Fold 5", 169999, "Latest book-style foldable with ZEISS optics", "12GB/16GB", "256GB/512GB", "8.03\" Foldable AMOLED", "Snapdragon 8 Gen 3", "50MP ZEISS Quad", "4800mAh", "Ultra-Premium", "Foldable Book"),
        ("vivo X Fold 4 Pro", 159999, "Premium foldable with advanced cameras", "12GB/16GB", "256GB/512GB", "8.03\" Foldable AMOLED", "Snapdragon 8 Gen 3", "50MP ZEISS Quad", "4800mAh", "Ultra-Premium", "Foldable Book"),
        ("vivo X Fold 4", 149999, "Flagship foldable", "12GB", "256GB/512GB", "8.03\" Foldable AMOLED", "Snapdragon 8 Gen 2", "50MP ZEISS Triple", "4600mAh", "Premium Flagship", "Foldable Book"),
        ("vivo X Flip 2", 84999, "Latest clamshell foldable", "12GB", "256GB/512GB", "6.74\" Foldable AMOLED", "Snapdragon 8+ Gen 2", "50MP Dual", "4400mAh", "Premium Flagship", "Foldable Clamshell"),
        ("vivo X Flip", 74999, "Stylish flip phone", "12GB", "256GB", "6.74\" Foldable AMOLED", "Snapdragon 8+ Gen 1", "50MP Dual", "4400mAh", "Flagship Killer", "Foldable Clamshell"),
    ]
    
    # vivo X Series - Professional Photography (15 models)
    vivo_x = [
        ("vivo X300 Ultra", 134999, "Ultimate camera flagship with ZEISS", "16GB", "512GB/1TB", "6.78\" AMOLED 120Hz", "Snapdragon 8 Gen 4", "50MP ZEISS Quad", "5500mAh", "Ultra-Premium", "Candy Bar"),
        ("vivo X300 Pro", 104999, "Pro camera flagship", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 120Hz", "Snapdragon 8 Gen 4", "50MP ZEISS Triple", "5400mAh", "Premium Flagship", "Candy Bar"),
        ("vivo X300", 84999, "Flagship with excellent cameras", "12GB", "256GB/512GB", "6.78\" AMOLED 120Hz", "Dimensity 9400", "50MP ZEISS Triple", "5000mAh", "Flagship Killer", "Candy Bar"),
        ("vivo X200 Ultra", 129999, "Photography powerhouse", "16GB", "512GB/1TB", "6.78\" AMOLED 120Hz", "Snapdragon 8 Gen 3", "50MP ZEISS Quad", "5500mAh", "Ultra-Premium", "Candy Bar"),
        ("vivo X200 Pro", 99999, "Pro camera phone", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 120Hz", "Snapdragon 8 Gen 3", "50MP ZEISS Triple", "5400mAh", "Premium Flagship", "Candy Bar"),
        ("vivo X200", 79999, "Flagship camera phone", "12GB", "256GB/512GB", "6.78\" AMOLED 120Hz", "Dimensity 9300", "50MP ZEISS Triple", "5000mAh", "Flagship Killer", "Candy Bar"),
        ("vivo X200 Pro Mini", 89999, "Compact flagship", "12GB", "256GB/512GB", "6.31\" AMOLED 120Hz", "Dimensity 9300", "50MP ZEISS Triple", "5000mAh", "Premium Flagship", "Candy Bar"),
        ("vivo X100 Ultra", 124999, "Previous gen ultra flagship", "16GB", "512GB/1TB", "6.78\" AMOLED 120Hz", "Snapdragon 8 Gen 3", "50MP ZEISS Quad", "5500mAh", "Ultra-Premium", "Candy Bar"),
        ("vivo X100 Pro", 94999, "Previous gen pro", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 120Hz", "Dimensity 9300", "50MP ZEISS Triple", "5400mAh", "Premium Flagship", "Candy Bar"),
        ("vivo X100", 74999, "Previous gen flagship", "12GB", "256GB", "6.78\" AMOLED 120Hz", "Dimensity 9300", "50MP ZEISS Triple", "5000mAh", "Flagship Killer", "Candy Bar"),
        ("vivo X100s", 79999, "Refined X100", "12GB", "256GB/512GB", "6.78\" AMOLED 120Hz", "Dimensity 9300+", "50MP ZEISS Triple", "5000mAh", "Flagship Killer", "Candy Bar"),
        ("vivo X90 Pro+", 109999, "Older flagship ultra", "12GB", "256GB/512GB", "6.78\" AMOLED 120Hz", "Snapdragon 8 Gen 2", "50MP ZEISS Quad", "4700mAh", "Premium Flagship", "Candy Bar"),
        ("vivo X90 Pro", 84999, "Older flagship pro", "12GB", "256GB/512GB", "6.78\" AMOLED 120Hz", "Dimensity 9200", "50MP ZEISS Triple", "4870mAh", "Flagship Killer", "Candy Bar"),
        ("vivo X90", 69999, "Older flagship", "12GB", "256GB", "6.78\" AMOLED 120Hz", "Dimensity 9200", "50MP ZEISS Triple", "4810mAh", "Flagship Killer", "Candy Bar"),
        ("vivo X80 Pro", 79999, "Classic flagship", "12GB", "256GB/512GB", "6.78\" AMOLED 120Hz", "Snapdragon 8 Gen 1", "50MP ZEISS Quad", "4700mAh", "Flagship Killer", "Candy Bar"),
    ]
    
    # vivo V Series - Selfie & Design (16 models)
    vivo_v = [
        ("vivo V60 Pro", 44999, "Premium selfie phone", "12GB", "256GB/512GB", "6.78\" AMOLED 120Hz", "Snapdragon 7 Gen 3", "50MP Triple", "5000mAh", "Mid-Range", "Candy Bar"),
        ("vivo V60", 37999, "Selfie specialist", "8GB/12GB", "256GB", "6.78\" AMOLED 120Hz", "Snapdragon 7 Gen 3", "50MP Dual", "5000mAh", "Mid-Range", "Candy Bar"),
        ("vivo V60e", 32999, "Affordable V60", "8GB", "256GB", "6.67\" AMOLED 90Hz", "Snapdragon 6 Gen 1", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("vivo V60 Lite", 27999, "Budget V series", "8GB", "128GB/256GB", "6.67\" AMOLED 90Hz", "Snapdragon 4 Gen 2", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("vivo V50 Pro", 42999, "Previous gen pro selfie", "12GB", "256GB", "6.78\" AMOLED 120Hz", "Dimensity 8200", "50MP Triple", "4800mAh", "Mid-Range", "Candy Bar"),
        ("vivo V50", 35999, "Previous gen selfie phone", "8GB/12GB", "256GB", "6.78\" AMOLED 120Hz", "Dimensity 8200", "50MP Dual", "4800mAh", "Mid-Range", "Candy Bar"),
        ("vivo V50e", 30999, "Affordable V50", "8GB", "256GB", "6.67\" AMOLED 90Hz", "Snapdragon 6 Gen 1", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("vivo V50 Lite", 25999, "Budget V50", "8GB", "128GB/256GB", "6.67\" AMOLED 90Hz", "Snapdragon 4 Gen 1", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("vivo V40 Pro", 39999, "Older pro selfie phone", "12GB", "256GB", "6.78\" AMOLED 120Hz", "Dimensity 9000", "50MP Triple", "4600mAh", "Mid-Range", "Candy Bar"),
        ("vivo V40", 33999, "Older selfie specialist", "8GB/12GB", "256GB", "6.78\" AMOLED 120Hz", "Snapdragon 778G", "50MP Dual", "4500mAh", "Mid-Range", "Candy Bar"),
        ("vivo V40 SE", 28999, "Budget V40", "8GB", "256GB", "6.67\" AMOLED 90Hz", "Snapdragon 685", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("vivo V40 Lite", 23999, "Entry V40", "8GB", "128GB", "6.67\" AMOLED 90Hz", "Helio G99", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("vivo V30 Pro", 37999, "Classic pro selfie", "12GB", "256GB", "6.78\" AMOLED 120Hz", "Dimensity 8200", "50MP Triple", "5000mAh", "Mid-Range", "Candy Bar"),
        ("vivo V30", 31999, "Classic selfie phone", "8GB/12GB", "256GB", "6.78\" AMOLED 120Hz", "Snapdragon 7 Gen 3", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("vivo V30e", 26999, "Affordable V30", "8GB", "256GB", "6.67\" AMOLED 90Hz", "Snapdragon 6 Gen 1", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("vivo V30 Lite", 21999, "Budget V30", "8GB", "128GB", "6.67\" AMOLED 90Hz", "Snapdragon 4 Gen 1", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
    ]

    
    # vivo Y Series - Youth/Budget (10 models)
    vivo_y = [
        ("vivo Y300 Pro", 29999, "Premium Y series", "8GB", "256GB", "6.78\" AMOLED 120Hz", "Snapdragon 7 Gen 1", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("vivo Y200 GT", 24999, "Performance Y series", "8GB", "256GB", "6.78\" LCD 120Hz", "Snapdragon 7s Gen 2", "64MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("vivo Y200 Pro", 22999, "Pro budget phone", "8GB", "256GB", "6.78\" LCD 120Hz", "Snapdragon 695", "64MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("vivo Y200e", 19999, "Affordable Y200", "8GB", "128GB/256GB", "6.67\" LCD 90Hz", "Snapdragon 4 Gen 2", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("vivo Y58 5G", 17999, "Budget 5G phone", "6GB/8GB", "128GB", "6.72\" LCD 120Hz", "Dimensity 6100+", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("vivo Y28s 5G", 15999, "Affordable 5G", "6GB/8GB", "128GB", "6.56\" LCD 90Hz", "Dimensity 6020", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("vivo Y28 5G", 14999, "Entry 5G phone", "4GB/6GB", "128GB", "6.56\" LCD 90Hz", "Dimensity 6020", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("vivo Y19s", 12999, "Basic smartphone", "4GB/6GB", "128GB", "6.56\" LCD", "Helio G85", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("vivo Y18", 11999, "Entry-level phone", "4GB/6GB", "64GB/128GB", "6.56\" LCD", "Helio G85", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("vivo Y03", 9999, "Ultra-budget phone", "3GB/4GB", "64GB", "6.56\" LCD", "Helio G35", "13MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
    ]
    
    # vivo T Series - Online Exclusive Performance (4 models)
    vivo_t = [
        ("vivo T4 Ultra", 39999, "Performance flagship killer", "12GB", "256GB/512GB", "6.78\" AMOLED 120Hz", "Dimensity 9300", "50MP Triple", "5000mAh", "Mid-Range", "Candy Bar"),
        ("vivo T4 Pro", 32999, "Pro performance phone", "8GB/12GB", "256GB", "6.78\" AMOLED 120Hz", "Dimensity 8300", "50MP Dual", "5000mAh", "Mid-Range", "Candy Bar"),
        ("vivo T4x 5G", 24999, "Budget performance 5G", "8GB", "128GB/256GB", "6.72\" LCD 120Hz", "Dimensity 7200", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("vivo T3 Ultra", 37999, "Previous gen performance", "12GB", "256GB", "6.78\" AMOLED 120Hz", "Dimensity 9200+", "50MP Triple", "5000mAh", "Mid-Range", "Candy Bar"),
    ]
    
    # ==================== OnePlus (15 models) ====================
    print("Adding OnePlus phones...")
    
    # OnePlus Number Series - Flagship (6 models)
    oneplus_number = [
        ("OnePlus 14", 84999, "Latest flagship with Hasselblad cameras", "12GB/16GB", "256GB/512GB", "6.82\" AMOLED 120Hz", "Snapdragon 8 Gen 4", "50MP Hasselblad Triple", "5400mAh", "Premium Flagship", "Candy Bar"),
        ("OnePlus 14R", 54999, "Budget flagship with great performance", "8GB/12GB", "256GB", "6.78\" AMOLED 120Hz", "Snapdragon 8 Gen 2", "50MP Triple", "5500mAh", "Flagship Killer", "Candy Bar"),
        ("OnePlus 13", 79999, "Previous flagship", "12GB/16GB", "256GB/512GB", "6.82\" AMOLED 120Hz", "Snapdragon 8 Gen 3", "50MP Hasselblad Triple", "5400mAh", "Premium Flagship", "Candy Bar"),
        ("OnePlus 13R", 49999, "Previous budget flagship", "8GB/12GB", "256GB", "6.78\" AMOLED 120Hz", "Snapdragon 8 Gen 2", "50MP Triple", "5500mAh", "Flagship Killer", "Candy Bar"),
        ("OnePlus 12", 74999, "Older flagship", "12GB/16GB", "256GB/512GB", "6.82\" AMOLED 120Hz", "Snapdragon 8 Gen 3", "50MP Hasselblad Triple", "5400mAh", "Premium Flagship", "Candy Bar"),
        ("OnePlus 12R", 44999, "Older budget flagship", "8GB/12GB", "256GB", "6.78\" AMOLED 120Hz", "Snapdragon 8 Gen 2", "50MP Triple", "5500mAh", "Flagship Killer", "Candy Bar"),
    ]
    
    # OnePlus Open Series - Foldable (2 models)
    oneplus_open = [
        ("OnePlus Open 2", 159999, "Latest book-style foldable", "16GB", "512GB/1TB", "7.82\" Foldable AMOLED", "Snapdragon 8 Gen 4", "50MP Hasselblad Triple", "4805mAh", "Ultra-Premium", "Foldable Book"),
        ("OnePlus Open", 139999, "Original foldable flagship", "16GB", "512GB", "7.82\" Foldable AMOLED", "Snapdragon 8 Gen 2", "48MP Hasselblad Triple", "4805mAh", "Ultra-Premium", "Foldable Book"),
    ]
    
    # OnePlus Nord Series - Mid-Range (7 models)
    oneplus_nord = [
        ("OnePlus Nord 6", 39999, "Premium mid-range", "12GB", "256GB", "6.74\" AMOLED 120Hz", "Snapdragon 7+ Gen 3", "50MP Triple", "5000mAh", "Mid-Range", "Candy Bar"),
        ("OnePlus Nord 5", 34999, "Mid-range performer", "8GB/12GB", "256GB", "6.74\" AMOLED 120Hz", "Snapdragon 7+ Gen 2", "50MP Triple", "5000mAh", "Mid-Range", "Candy Bar"),
        ("OnePlus Nord CE 6", 29999, "Core edition mid-range", "8GB", "256GB", "6.72\" AMOLED 120Hz", "Snapdragon 7 Gen 1", "64MP Triple", "5000mAh", "Budget", "Candy Bar"),
        ("OnePlus Nord CE 5", 26999, "Affordable core edition", "8GB", "128GB/256GB", "6.72\" AMOLED 120Hz", "Snapdragon 695", "64MP Triple", "5000mAh", "Budget", "Candy Bar"),
        ("OnePlus Nord CE 4", 24999, "Budget core edition", "8GB", "128GB/256GB", "6.72\" AMOLED 90Hz", "Snapdragon 695", "64MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("OnePlus Nord CE 6 Lite", 22999, "Lite mid-range", "8GB", "128GB", "6.59\" LCD 120Hz", "Snapdragon 695", "64MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("OnePlus Nord CE 5 Lite", 19999, "Budget lite edition", "6GB/8GB", "128GB", "6.59\" LCD 120Hz", "Snapdragon 695", "64MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
    ]

    
    # ==================== Realme (40 models) ====================
    print("Adding Realme phones...")
    
    # Realme GT Series - Performance Flagships (6 models)
    realme_gt = [
        ("Realme GT 8 Pro", 64999, "Latest flagship killer", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 144Hz", "Snapdragon 8 Gen 4", "50MP Triple", "5400mAh", "Flagship Killer", "Candy Bar"),
        ("Realme GT 8", 49999, "Flagship performance", "12GB", "256GB", "6.78\" AMOLED 144Hz", "Snapdragon 8 Gen 3", "50MP Triple", "5000mAh", "Flagship Killer", "Candy Bar"),
        ("Realme GT 7 Pro", 59999, "Previous flagship killer", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 144Hz", "Snapdragon 8 Gen 3", "50MP Triple", "5400mAh", "Flagship Killer", "Candy Bar"),
        ("Realme GT 6", 44999, "Performance flagship", "12GB", "256GB", "6.78\" AMOLED 120Hz", "Snapdragon 8s Gen 3", "50MP Triple", "5000mAh", "Mid-Range", "Candy Bar"),
        ("Realme GT 6T", 39999, "Affordable GT", "8GB/12GB", "256GB", "6.78\" AMOLED 120Hz", "Snapdragon 7+ Gen 3", "50MP Triple", "5000mAh", "Mid-Range", "Candy Bar"),
        ("Realme GT 5 Pro", 54999, "Older flagship killer", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 144Hz", "Snapdragon 8 Gen 3", "50MP Triple", "5400mAh", "Flagship Killer", "Candy Bar"),
    ]
    
    # Realme Number Series - Hero Line (12 models)
    realme_number = [
        ("Realme 14 Pro+", 34999, "Premium number series", "12GB", "256GB/512GB", "6.7\" AMOLED 120Hz", "Dimensity 7300", "50MP Triple", "5000mAh", "Mid-Range", "Candy Bar"),
        ("Realme 14 Pro", 28999, "Pro number series", "8GB/12GB", "256GB", "6.7\" AMOLED 120Hz", "Snapdragon 7s Gen 2", "50MP Triple", "5000mAh", "Budget", "Candy Bar"),
        ("Realme 14", 22999, "Standard number series", "8GB", "128GB/256GB", "6.72\" LCD 120Hz", "Dimensity 7050", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("Realme 14x", 17999, "Budget number series", "6GB/8GB", "128GB", "6.67\" LCD 120Hz", "Dimensity 6100+", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("Realme 13 Pro+", 32999, "Previous pro+", "12GB", "256GB/512GB", "6.7\" AMOLED 120Hz", "Dimensity 7300", "50MP Triple", "5000mAh", "Mid-Range", "Candy Bar"),
        ("Realme 13 Pro", 26999, "Previous pro", "8GB/12GB", "256GB", "6.7\" AMOLED 120Hz", "Snapdragon 7s Gen 2", "50MP Triple", "5000mAh", "Budget", "Candy Bar"),
        ("Realme 13", 20999, "Previous standard", "8GB", "128GB/256GB", "6.72\" LCD 120Hz", "Dimensity 7050", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("Realme 13+", 24999, "Previous plus model", "8GB/12GB", "256GB", "6.67\" AMOLED 120Hz", "Dimensity 7300", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("Realme 12 Pro+", 30999, "Older pro+", "12GB", "256GB", "6.7\" AMOLED 120Hz", "Snapdragon 7s Gen 2", "50MP Triple", "5000mAh", "Mid-Range", "Candy Bar"),
        ("Realme 12 Pro", 24999, "Older pro", "8GB/12GB", "256GB", "6.7\" AMOLED 120Hz", "Snapdragon 7s Gen 2", "50MP Triple", "5000mAh", "Budget", "Candy Bar"),
        ("Realme 12", 18999, "Older standard", "8GB", "128GB/256GB", "6.72\" LCD 120Hz", "Dimensity 6100+", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("Realme 12x", 15999, "Older budget", "6GB/8GB", "128GB", "6.67\" LCD 120Hz", "Dimensity 6100+", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
    ]
    
    # Realme P Series - Power/Gaming Budget (4 models)
    realme_p = [
        ("Realme P3 Pro", 24999, "Gaming budget pro", "8GB/12GB", "256GB", "6.7\" AMOLED 120Hz", "Snapdragon 7s Gen 2", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("Realme P3", 19999, "Gaming budget phone", "8GB", "128GB/256GB", "6.72\" LCD 120Hz", "Dimensity 7050", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("Realme P2 Pro", 22999, "Previous gaming pro", "8GB/12GB", "256GB", "6.7\" AMOLED 120Hz", "Dimensity 7050", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("Realme P1", 17999, "Entry gaming phone", "8GB", "128GB", "6.72\" LCD 120Hz", "Dimensity 7050", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
    ]
    
    # Realme C Series - Budget/Entry (8 models)
    realme_c = [
        ("Realme C75", 16999, "Premium C series", "8GB", "128GB/256GB", "6.72\" LCD 90Hz", "Helio G99", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("Realme C75x", 15999, "C75 variant", "6GB/8GB", "128GB", "6.72\" LCD 90Hz", "Helio G99", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("Realme C67", 14999, "Mid C series", "6GB/8GB", "128GB", "6.72\" LCD 90Hz", "Snapdragon 685", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("Realme C65", 13999, "Affordable C series", "6GB", "128GB", "6.67\" LCD 90Hz", "Helio G85", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("Realme C63", 12999, "Budget C series", "6GB", "128GB", "6.74\" LCD 90Hz", "Unisoc T612", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("Realme C61", 11999, "Entry C series", "4GB/6GB", "64GB/128GB", "6.74\" LCD 90Hz", "Unisoc T612", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("Realme C55", 13999, "Classic C series", "6GB/8GB", "128GB", "6.72\" LCD 90Hz", "Helio G88", "64MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("Realme C53", 11999, "Budget classic", "6GB", "128GB", "6.74\" LCD 90Hz", "Unisoc T612", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
    ]
    
    # Realme Narzo Series - Online Exclusive (6 models)
    realme_narzo = [
        ("Realme Narzo 90x", 19999, "Latest Narzo performance", "8GB", "128GB/256GB", "6.72\" LCD 120Hz", "Dimensity 7050", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("Realme Narzo 80 Pro", 22999, "Narzo pro model", "8GB/12GB", "256GB", "6.7\" AMOLED 120Hz", "Dimensity 7050", "50MP Triple", "5000mAh", "Budget", "Candy Bar"),
        ("Realme Narzo 70 Pro", 20999, "Previous Narzo pro", "8GB/12GB", "256GB", "6.7\" AMOLED 120Hz", "Dimensity 7050", "50MP Triple", "5000mAh", "Budget", "Candy Bar"),
        ("Realme Narzo 70x", 16999, "Affordable Narzo", "6GB/8GB", "128GB", "6.72\" LCD 120Hz", "Dimensity 6100+", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("Realme Narzo N65", 13999, "Budget Narzo", "6GB", "128GB", "6.67\" LCD 90Hz", "Helio G85", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("Realme Narzo N63", 11999, "Entry Narzo", "4GB/6GB", "64GB/128GB", "6.74\" LCD 90Hz", "Unisoc T612", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
    ]
    
    # Realme Note Series (2 models)
    realme_note = [
        ("Realme Note 60", 10999, "Basic Note phone", "4GB/6GB", "64GB/128GB", "6.74\" LCD", "Unisoc T612", "13MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("Realme Note 50", 8999, "Ultra-budget Note", "3GB/4GB", "64GB", "6.74\" LCD", "Unisoc T612", "13MP Single", "5000mAh", "Entry-Level", "Candy Bar"),
    ]

    
    # ==================== iQOO (20 models) ====================
    print("Adding iQOO phones...")
    
    # iQOO Number Series - Top Tier Gaming (6 models)
    iqoo_number = [
        ("iQOO 14", 69999, "Latest gaming flagship", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 144Hz", "Snapdragon 8 Gen 4", "50MP Triple", "5000mAh", "Premium Flagship", "Candy Bar"),
        ("iQOO 14 Pro", 79999, "Pro gaming flagship", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 144Hz", "Snapdragon 8 Gen 4", "50MP Triple", "5100mAh", "Premium Flagship", "Candy Bar"),
        ("iQOO 13", 64999, "Previous gaming flagship", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 144Hz", "Snapdragon 8 Gen 3", "50MP Triple", "5000mAh", "Flagship Killer", "Candy Bar"),
        ("iQOO 13 Pro", 74999, "Previous pro gaming", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 144Hz", "Snapdragon 8 Gen 3", "50MP Triple", "5100mAh", "Premium Flagship", "Candy Bar"),
        ("iQOO 12", 59999, "Older gaming flagship", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 144Hz", "Snapdragon 8 Gen 3", "50MP Triple", "5000mAh", "Flagship Killer", "Candy Bar"),
        ("iQOO 12 Pro", 69999, "Older pro gaming", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 144Hz", "Snapdragon 8 Gen 3", "50MP Triple", "5100mAh", "Premium Flagship", "Candy Bar"),
    ]
    
    # iQOO Neo Series - Flagship Killers (4 models)
    iqoo_neo = [
        ("iQOO Neo 10 Pro", 44999, "Latest Neo pro", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 144Hz", "Dimensity 9400", "50MP Dual", "5000mAh", "Mid-Range", "Candy Bar"),
        ("iQOO Neo 10", 37999, "Latest Neo", "8GB/12GB", "256GB", "6.78\" AMOLED 144Hz", "Snapdragon 8s Gen 3", "50MP Dual", "5000mAh", "Mid-Range", "Candy Bar"),
        ("iQOO Neo 9 Pro", 42999, "Previous Neo pro", "12GB/16GB", "256GB/512GB", "6.78\" AMOLED 144Hz", "Dimensity 9300", "50MP Dual", "5000mAh", "Mid-Range", "Candy Bar"),
        ("iQOO Neo 9", 35999, "Previous Neo", "8GB/12GB", "256GB", "6.78\" AMOLED 144Hz", "Snapdragon 8 Gen 2", "50MP Dual", "5000mAh", "Mid-Range", "Candy Bar"),
    ]
    
    # iQOO Z Series - Budget Gaming (10 models)
    iqoo_z = [
        ("iQOO Z10 Pro", 29999, "Latest Z pro", "8GB/12GB", "256GB", "6.78\" AMOLED 120Hz", "Snapdragon 7 Gen 3", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("iQOO Z10", 24999, "Latest Z series", "8GB", "128GB/256GB", "6.72\" LCD 120Hz", "Dimensity 7300", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("iQOO Z10x", 19999, "Budget Z series", "6GB/8GB", "128GB", "6.72\" LCD 120Hz", "Snapdragon 6 Gen 1", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("iQOO Z9 Turbo", 32999, "Turbo performance", "12GB", "256GB/512GB", "6.78\" AMOLED 144Hz", "Snapdragon 8s Gen 3", "50MP Dual", "5000mAh", "Mid-Range", "Candy Bar"),
        ("iQOO Z9s Pro", 27999, "Z9s pro model", "8GB/12GB", "256GB", "6.78\" AMOLED 120Hz", "Snapdragon 7 Gen 3", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("iQOO Z9s", 22999, "Z9s standard", "8GB", "128GB/256GB", "6.72\" LCD 120Hz", "Dimensity 7300", "50MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("iQOO Z9x", 17999, "Z9x budget", "6GB/8GB", "128GB", "6.72\" LCD 120Hz", "Snapdragon 6 Gen 1", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("iQOO Z9 Lite", 15999, "Z9 lite edition", "6GB", "128GB", "6.56\" LCD 90Hz", "Dimensity 6300", "50MP Dual", "5000mAh", "Entry-Level", "Candy Bar"),
        ("iQOO Z8 Pro", 25999, "Previous Z pro", "8GB/12GB", "256GB", "6.78\" AMOLED 120Hz", "Dimensity 8200", "64MP Dual", "5000mAh", "Budget", "Candy Bar"),
        ("iQOO Z8", 20999, "Previous Z series", "8GB", "128GB/256GB", "6.72\" LCD 120Hz", "Dimensity 7200", "64MP Dual", "5000mAh", "Budget", "Candy Bar"),
    ]
    
    # Combine all phone data
    all_phones = []
    
    # Process OPPO phones
    for series in [oppo_find_n, oppo_find_x, oppo_reno, oppo_a, oppo_f]:
        for phone in series:
            all_phones.append({
                "name": phone[0],
                "brand": "Oppo",
                "price": phone[1] * 100,
                "description": phone[2],
                "ram": phone[3],
                "storage": phone[4],
                "display": phone[5],
                "processor": phone[6],
                "camera": phone[7],
                "battery": phone[8],
                "price_tier": phone[9],
                "form_factor": phone[10]
            })
    
    # Process vivo phones
    for series in [vivo_x_fold, vivo_x, vivo_v, vivo_y, vivo_t]:
        for phone in series:
            all_phones.append({
                "name": phone[0],
                "brand": "vivo",
                "price": phone[1] * 100,
                "description": phone[2],
                "ram": phone[3],
                "storage": phone[4],
                "display": phone[5],
                "processor": phone[6],
                "camera": phone[7],
                "battery": phone[8],
                "price_tier": phone[9],
                "form_factor": phone[10]
            })
    
    # Process OnePlus phones
    for series in [oneplus_number, oneplus_open, oneplus_nord]:
        for phone in series:
            all_phones.append({
                "name": phone[0],
                "brand": "OnePlus",
                "price": phone[1] * 100,
                "description": phone[2],
                "ram": phone[3],
                "storage": phone[4],
                "display": phone[5],
                "processor": phone[6],
                "camera": phone[7],
                "battery": phone[8],
                "price_tier": phone[9],
                "form_factor": phone[10]
            })
    
    # Process Realme phones
    for series in [realme_gt, realme_number, realme_p, realme_c, realme_narzo, realme_note]:
        for phone in series:
            all_phones.append({
                "name": phone[0],
                "brand": "Realme",
                "price": phone[1] * 100,
                "description": phone[2],
                "ram": phone[3],
                "storage": phone[4],
                "display": phone[5],
                "processor": phone[6],
                "camera": phone[7],
                "battery": phone[8],
                "price_tier": phone[9],
                "form_factor": phone[10]
            })
    
    # Process iQOO phones
    for series in [iqoo_number, iqoo_neo, iqoo_z]:
        for phone in series:
            all_phones.append({
                "name": phone[0],
                "brand": "iQOO",
                "price": phone[1] * 100,
                "description": phone[2],
                "ram": phone[3],
                "storage": phone[4],
                "display": phone[5],
                "processor": phone[6],
                "camera": phone[7],
                "battery": phone[8],
                "price_tier": phone[9],
                "form_factor": phone[10]
            })

    
    # Add all phones to database
    print(f"\nTotal BBK Electronics phones to add: {len(all_phones)}")
    print("=" * 60)
    
    added_count = 0
    skipped_count = 0
    
    for phone_data in all_phones:
        try:
            # Check if phone already exists
            existing = AstraProduct.get_all({"name": phone_data["name"]})
            if existing:
                print(f"⏭️  Skipped (exists): {phone_data['name']}")
                skipped_count += 1
                continue
            
            # Determine chipset category
            processor = phone_data["processor"].lower()
            if "snapdragon 8" in processor or "dimensity 9" in processor:
                chipset_category = "Snapdragon Flagship" if "snapdragon" in processor else "Dimensity/Helio"
            elif "snapdragon 7" in processor or "dimensity 8" in processor or "dimensity 7" in processor:
                chipset_category = "Snapdragon Mid-Range" if "snapdragon" in processor else "Dimensity/Helio"
            elif "snapdragon 6" in processor or "dimensity 6" in processor:
                chipset_category = "Snapdragon Budget" if "snapdragon" in processor else "Dimensity/Helio"
            elif "helio" in processor or "unisoc" in processor:
                chipset_category = "Dimensity/Helio"
            else:
                chipset_category = "Other"
            
            # Determine use case based on brand and specs
            brand = phone_data["brand"]
            if brand == "iQOO" or "GT" in phone_data["name"] or "gaming" in phone_data["description"].lower():
                use_case = "Gaming"
            elif "camera" in phone_data["description"].lower() or "photography" in phone_data["description"].lower() or "hasselblad" in phone_data["description"].lower() or "zeiss" in phone_data["description"].lower():
                use_case = "Camera & Photography"
            elif "battery" in phone_data["description"].lower() or int(phone_data["battery"].replace("mAh", "")) >= 5000:
                use_case = "Battery & Endurance"
            else:
                use_case = "General"
            
            # Determine software experience
            if brand == "Oppo":
                software = "ColorOS"
            elif brand == "vivo" or brand == "iQOO":
                software = "Funtouch OS"
            elif brand == "OnePlus":
                software = "OxygenOS"
            elif brand == "Realme":
                software = "Realme UI"
            else:
                software = "Android"
            
            # Determine target demographic
            price_tier = phone_data["price_tier"]
            if price_tier in ["Ultra-Premium", "Premium Flagship"]:
                demographic = "Professionals"
            elif "Foldable" in phone_data["form_factor"]:
                demographic = "Professionals"
            elif use_case == "Gaming":
                demographic = "Gamers"
            elif use_case == "Camera & Photography":
                demographic = "Content Creators"
            elif price_tier == "Entry-Level":
                demographic = "Students"
            else:
                demographic = "General"
            
            # Get images (try to get real images from GSMArena for flagships)
            images = get_generic_images(3)
            if phone_data["price_tier"] in ["Ultra-Premium", "Premium Flagship", "Flagship Killer"]:
                # Try to get real images for flagships
                name_lower = phone_data["name"].lower().replace(" ", "-")
                brand_lower = brand.lower()
                
                # Construct GSMArena URLs
                gsmarena_base = f"https://fdn2.gsmarena.com/vv/pics/{brand_lower}/{name_lower}"
                images = [
                    f"{gsmarena_base}-1.jpg",
                    f"{gsmarena_base}-2.jpg",
                    f"{gsmarena_base}-3.jpg"
                ]
            
            # Create product
            product = {
                "name": phone_data["name"],
                "brand": brand,
                "category": "Smartphones",
                "price": phone_data["price"],
                "description": phone_data["description"],
                "in_stock": True,
                "images": images,
                "specs": {
                    "ram": phone_data["ram"],
                    "storage": phone_data["storage"],
                    "display": phone_data["display"],
                    "processor": phone_data["processor"],
                    "camera": phone_data["camera"],
                    "battery": phone_data["battery"],
                    "price_tier": phone_data["price_tier"],
                    "use_case": use_case,
                    "form_factor": phone_data["form_factor"],
                    "software_experience": software,
                    "chipset_category": chipset_category,
                    "market_origin": "Chinese Powerhouses",
                    "target_demographic": demographic
                }
            }
            
            AstraProduct.create(product)
            print(f"✅ Added: {phone_data['name']} ({brand}) - KES {phone_data['price'] // 100:,}")
            added_count += 1
            
        except Exception as e:
            print(f"❌ Error adding {phone_data['name']}: {str(e)}")
            continue
    
    print("\n" + "=" * 60)
    print(f"✅ Successfully added: {added_count} phones")
    print(f"⏭️  Skipped (already exist): {skipped_count} phones")
    print(f"📱 Total BBK Electronics phones: {added_count + skipped_count}")
    print("=" * 60)

if __name__ == "__main__":
    add_phones()
