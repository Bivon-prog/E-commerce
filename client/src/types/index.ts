export interface Product {
    id: string;
    name: string;
    category: 'Phone' | 'Accessory';
    brand: string;
    price: number; // Price in cents from Rust backend
    description: string;
    images: string[]; // Array of image URLs (3-5 images per product)
    specs?: {
        screen_size?: string;
        ram?: string;
        storage?: string;
        battery?: string;
        camera?: string;
        processor?: string;
    };
    in_stock?: boolean;
    created_at?: string;
}

export interface CartItem extends Product {
    quantity: number;
}

// Request type for creating products (matches Rust backend)
export interface CreateProductRequest {
    name: string;
    brand: string;
    category: string;
    price: number;
    description: string;
    images: string[]; // Array of image URLs
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
