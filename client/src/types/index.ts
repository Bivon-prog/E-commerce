export interface Product {
    _id: string; // Changed from id to _id to match API
    name: string;
    category: 'Phone' | 'Accessory';
    brand: string;
    price: number; // Price in cents from Django backend
    description: string;
    images: string[]; // Array of image URLs (3-5 images per product)
    specs?: {
        screen_size?: string;
        ram?: string;
        storage?: string;
        battery?: string;
        camera?: string;
        processor?: string;
        // Comprehensive categorization fields
        price_tier?: string;
        price_tier_description?: string;
        use_case?: string;
        use_case_description?: string;
        form_factor?: string;
        form_factor_description?: string;
        software_experience?: string;
        software_description?: string;
        chipset_category?: string;
        chipset_description?: string;
        market_origin?: string;
        origin_description?: string;
        target_demographic?: string;
        price_category?: string;
        performance_tier?: string;
        brand_series?: string;
        target_audience?: string;
    };
    in_stock?: boolean;
    stock_quantity?: number;
    created_at?: string;
}

export interface CartItem extends Product {
    quantity: number;
}

// Filter options from the API
export interface FilterOptions {
    brands: string[];
    price_tiers: string[];
    use_cases: string[];
    form_factors: string[];
    software_experiences: string[];
    chipset_categories: string[];
    market_origins: string[];
    target_demographics: string[];
    price_range: {
        min: number;
        max: number;
    };
}

// Request type for creating products
export interface CreateProductRequest {
    name: string;
    brand: string;
    category: string;
    price: number;
    description: string;
    images: string[];
    specs?: {
        screen_size?: string;
        ram?: string;
        storage?: string;
        battery?: string;
        camera?: string;
        processor?: string;
    };
    in_stock?: boolean;
}
