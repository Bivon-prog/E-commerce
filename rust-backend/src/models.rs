use serde::{Deserialize, Serialize};
use chrono::{DateTime, Utc};

/// Product specifications containing technical details
/// 
/// This struct represents the technical specifications of a mobile phone or accessory.
/// Each field is optional to accommodate different product types (phones vs accessories).
/// 
/// **Serde Integration Explanation:**
/// - `#[derive(Serialize, Deserialize)]` automatically generates code to convert between
///   this Rust struct and JSON format
/// - When a JSON request comes in, serde uses reflection-like mechanisms to map
///   JSON fields to struct fields by name
/// - The `#[serde(skip_serializing_if = "Option::is_none")]` attribute means that
///   if a field is None, it won't appear in the JSON output, keeping responses clean
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct ProductSpecs {
    #[serde(skip_serializing_if = "Option::is_none")]
    pub screen_size: Option<String>,
    
    #[serde(skip_serializing_if = "Option::is_none")]
    pub ram: Option<String>,
    
    #[serde(skip_serializing_if = "Option::is_none")]
    pub storage: Option<String>,
    
    #[serde(skip_serializing_if = "Option::is_none")]
    pub battery: Option<String>,
    
    #[serde(skip_serializing_if = "Option::is_none")]
    pub camera: Option<String>,
    
    #[serde(skip_serializing_if = "Option::is_none")]
    pub processor: Option<String>,
}

/// Main Product model representing a mobile phone or accessory
/// 
/// This is the core domain model that represents products in our e-commerce system.
/// 
/// **Field Explanations:**
/// - `id`: UUID v4 for globally unique identification, automatically generated
/// - `name`: Product display name (e.g., "iPhone 15 Pro")
/// - `brand`: Manufacturer (e.g., "Apple", "Samsung", "Google")
/// - `category`: Product type ("Phone" or "Accessory")
/// - `price`: Price in cents to avoid floating-point precision issues
/// - `description`: Marketing description of the product
/// - `images`: Array of external URLs pointing to product images (3-5 images per product)
/// - `specs`: Optional technical specifications
/// - `in_stock`: Inventory availability flag
/// - `created_at`: Timestamp when product was added to database
/// 
/// **MongoDB Integration:**
/// - The `_id` field in MongoDB will be mapped to our `id` field
/// - MongoDB's BSON format automatically handles the UUID serialization
/// - DateTime<Utc> is serialized as MongoDB's native Date type
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Product {
    #[serde(rename = "_id", skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    
    pub name: String,
    pub brand: String,
    pub category: String, // "Phone" or "Accessory"
    pub price: u32, // Price in cents to avoid floating point issues
    pub description: String,
    
    // Handle both old and new image formats
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    pub images: Vec<String>, // New format: Array of external URLs
    
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub image_url: Option<String>, // Old format: Single URL (for backward compatibility)
    
    #[serde(skip_serializing_if = "Option::is_none")]
    pub specs: Option<ProductSpecs>,
    
    #[serde(default = "default_stock_status")]
    pub in_stock: bool,
    
    #[serde(default = "chrono::Utc::now")]
    pub created_at: DateTime<Utc>,
}

/// Default function for stock status - new products are in stock by default
fn default_stock_status() -> bool {
    true
}

impl Product {
    /// Migrate old image_url format to new images array format
    pub fn migrate_images(&mut self) {
        if self.images.is_empty() && self.image_url.is_some() {
            if let Some(url) = &self.image_url {
                self.images = vec![url.clone()];
            }
        }
    }
    
    /// Get the primary image URL (first image or fallback to old format)
    pub fn get_primary_image(&self) -> Option<&String> {
        if !self.images.is_empty() {
            self.images.first()
        } else {
            self.image_url.as_ref()
        }
    }
}

/// Request payload for creating a new product
/// 
/// This struct represents the JSON payload that clients send when creating a product.
/// It's separate from the main Product struct because:
/// 1. Clients don't provide ID (auto-generated)
/// 2. Clients don't provide created_at (auto-generated)
/// 3. We want to validate the payload before creating the full Product
/// 
/// **Validation Strategy:**
/// - Required fields are not Option<T>, so serde will return an error if missing
/// - Optional fields use Option<T> and have sensible defaults
/// - The images will be validated asynchronously before saving
#[derive(Debug, Deserialize)]
pub struct CreateProductRequest {
    pub name: String,
    pub brand: String,
    pub category: String,
    pub price: u32,
    pub description: String,
    pub images: Vec<String>, // Array of image URLs - these will be validated with HTTP HEAD requests
    pub specs: Option<ProductSpecs>,
    pub in_stock: Option<bool>,
}

impl From<CreateProductRequest> for Product {
    /// Convert a CreateProductRequest into a Product
    /// 
    /// This implementation of the From trait allows us to easily convert
    /// the request payload into our domain model. The conversion:
    /// 1. Generates a new UUID for the product
    /// 2. Sets the current timestamp
    /// 3. Uses provided values or sensible defaults
    fn from(req: CreateProductRequest) -> Self {
        Product {
            id: Some(uuid::Uuid::new_v4().to_string()),
            name: req.name,
            brand: req.brand,
            category: req.category,
            price: req.price,
            description: req.description,
            images: req.images,
            image_url: None, // New products use images array, not single image_url
            specs: req.specs,
            in_stock: req.in_stock.unwrap_or(true),
            created_at: Utc::now(),
        }
    }
}

/// Query parameters for filtering products
/// 
/// This struct captures the query parameters that can be used to filter
/// the product list. Actix-web will automatically deserialize URL query
/// parameters into this struct.
/// 
/// Example: GET /products?brand=Apple&category=Phone&in_stock=true
#[derive(Debug, Deserialize)]
pub struct ProductQuery {
    pub brand: Option<String>,
    pub category: Option<String>,
    pub in_stock: Option<bool>,
}