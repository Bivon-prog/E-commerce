use actix_web::{web, HttpResponse, Result as ActixResult};
use mongodb::bson::doc;
use reqwest::Client as HttpClient;
use futures::stream::TryStreamExt;
use crate::database::DatabaseManager;
use crate::models::{Product, CreateProductRequest, ProductQuery};
use log::{info, error, warn};

/// Handler for creating a new product (POST /products)
/// 
/// This is an async function that handles HTTP POST requests to create new products.
/// 
/// **Actix-web Request Processing Flow:**
/// 1. Actix-web receives HTTP request on the configured route
/// 2. The framework deserializes the JSON body into CreateProductRequest using serde
/// 3. Dependency injection provides DatabaseManager and HttpClient from app state
/// 4. Our handler function executes asynchronously
/// 5. The return value is serialized back to JSON and sent as HTTP response
/// 
/// **Async Runtime Explanation:**
/// - This function runs on Tokio's async runtime
/// - When we hit an `.await` point, the current task yields control
/// - Other tasks can run while we wait for I/O operations (HTTP request, DB insert)
/// - This allows handling thousands of concurrent requests efficiently
/// 
/// **Parameters:**
/// - `product_data`: JSON payload automatically deserialized by Actix-web
/// - `db`: Database manager injected from application state
/// - `http_client`: HTTP client for image URL validation
pub async fn create_product(
    product_data: web::Json<CreateProductRequest>,
    db: web::Data<DatabaseManager>,
    http_client: web::Data<HttpClient>,
) -> ActixResult<HttpResponse> {
    info!("Received request to create product: {}", product_data.name);
    
    // Step 1: Validate all external image URLs
    // 
    // **Why HEAD Request Instead of GET:**
    // - HEAD returns only headers, no body content
    // - Much faster and uses less bandwidth (important for large images)
    // - We only need to verify the URL exists and is accessible
    // - Status code 200 means the resource exists and is reachable
    // - Reduces server load on the image hosting service
    for (index, image_url) in product_data.images.iter().enumerate() {
        match validate_image_url(&http_client, image_url).await {
            Ok(true) => {
                info!("Image URL {} validation successful: {}", index + 1, image_url);
            }
            Ok(false) => {
                warn!("Image URL {} validation failed: {}", index + 1, image_url);
                return Ok(HttpResponse::BadRequest().json(serde_json::json!({
                    "error": "Invalid image URL",
                    "message": format!("Image URL {} is not accessible: {}", index + 1, image_url)
                })));
            }
            Err(e) => {
                error!("Error validating image URL {}: {}", index + 1, e);
                return Ok(HttpResponse::BadRequest().json(serde_json::json!({
                    "error": "Image URL validation error",
                    "message": format!("Failed to validate image URL {}: {}", index + 1, e)
                })));
            }
        }
    }
    
    // Step 2: Convert request to Product model
    // This uses the From trait implementation we defined in models.rs
    let product: Product = product_data.into_inner().into();
    
    // Step 3: Insert into MongoDB
    // 
    // **MongoDB Operation Explanation:**
    // - insert_one() is an async operation that returns a Future
    // - The operation is sent to MongoDB over the network
    // - MongoDB assigns an ObjectId and stores the document
    // - The driver automatically handles connection pooling
    // - If the operation fails, we get a detailed error
    match db.products.insert_one(&product, None).await {
        Ok(result) => {
            info!("Product created successfully with ID: {:?}", result.inserted_id);
            Ok(HttpResponse::Created().json(serde_json::json!({
                "message": "Product created successfully",
                "id": product.id,
                "inserted_id": result.inserted_id
            })))
        }
        Err(e) => {
            error!("Failed to insert product into database: {}", e);
            Ok(HttpResponse::InternalServerError().json(serde_json::json!({
                "error": "Database error",
                "message": "Failed to create product"
            })))
        }
    }
}

/// Handler for retrieving products (GET /products)
/// 
/// This handler supports filtering by brand, category, and stock status
/// through query parameters.
/// 
/// **Query Parameter Processing:**
/// - Actix-web automatically deserializes URL query params into ProductQuery struct
/// - Example: GET /products?brand=Apple&category=Phone&in_stock=true
/// - Missing parameters become None in the Option<T> fields
/// 
/// **MongoDB Query Building:**
/// - We build a BSON document with filter conditions
/// - Only non-None query parameters are added to the filter
/// - Empty filter document matches all products
pub async fn get_products(
    query: web::Query<ProductQuery>,
    db: web::Data<DatabaseManager>,
) -> ActixResult<HttpResponse> {
    info!("Received request to get products with filters: {:?}", query);
    
    // Build MongoDB filter document based on query parameters
    let mut filter = doc! {};
    
    if let Some(brand) = &query.brand {
        filter.insert("brand", brand);
    }
    
    if let Some(category) = &query.category {
        filter.insert("category", category);
    }
    
    if let Some(in_stock) = query.in_stock {
        filter.insert("in_stock", in_stock);
    }
    
    info!("MongoDB filter: {:?}", filter);
    
    // Execute the query
    // 
    // **MongoDB find() Operation:**
    // - find() returns a Cursor that can iterate over results
    // - try_collect() consumes the cursor and collects all results into a Vec
    // - This is efficient for reasonable result sets
    // - For large datasets, we'd implement pagination instead
    match db.products.find(filter, None).await {
        Ok(cursor) => {
            match cursor.try_collect::<Vec<Product>>().await {
                Ok(mut products) => {
                    // Migrate old image_url format to new images array format
                    for product in &mut products {
                        product.migrate_images();
                    }
                    info!("Retrieved {} products from database", products.len());
                    Ok(HttpResponse::Ok().json(products))
                }
                Err(e) => {
                    error!("Failed to collect products from cursor: {}", e);
                    Ok(HttpResponse::InternalServerError().json(serde_json::json!({
                        "error": "Database error",
                        "message": "Failed to retrieve products"
                    })))
                }
            }
        }
        Err(e) => {
            error!("Failed to query products from database: {}", e);
            Ok(HttpResponse::InternalServerError().json(serde_json::json!({
                "error": "Database error",
                "message": "Failed to query products"
            })))
        }
    }
}

/// Handler for retrieving a single product by ID (GET /products/{id})
/// 
/// This handler extracts the product ID from the URL path and queries
/// the database for that specific product.
pub async fn get_product_by_id(
    path: web::Path<String>,
    db: web::Data<DatabaseManager>,
) -> ActixResult<HttpResponse> {
    let product_id = path.into_inner();
    info!("Received request to get product by ID: {}", product_id);
    
    // Query MongoDB for the product
    let filter = doc! { "_id": &product_id };
    
    match db.products.find_one(filter, None).await {
        Ok(Some(product)) => {
            info!("Found product: {}", product.name);
            Ok(HttpResponse::Ok().json(product))
        }
        Ok(None) => {
            warn!("Product not found with ID: {}", product_id);
            Ok(HttpResponse::NotFound().json(serde_json::json!({
                "error": "Product not found",
                "message": format!("No product found with ID: {}", product_id)
            })))
        }
        Err(e) => {
            error!("Database error while finding product: {}", e);
            Ok(HttpResponse::InternalServerError().json(serde_json::json!({
                "error": "Database error",
                "message": "Failed to retrieve product"
            })))
        }
    }
}

/// Validate that an image URL is accessible
/// 
/// This function performs an HTTP HEAD request to verify that the image URL
/// is valid and accessible.
/// 
/// **HTTP HEAD Request Explanation:**
/// - HEAD is like GET but returns only headers, no body
/// - Perfect for checking if a resource exists without downloading it
/// - Much more efficient than GET for large images
/// - Returns the same status codes as GET would
/// 
/// **Async HTTP Client:**
/// - reqwest::Client maintains its own connection pool
/// - Reuses connections for multiple requests to the same host
/// - Handles redirects, timeouts, and retries automatically
/// - The operation is fully async and non-blocking
async fn validate_image_url(client: &HttpClient, url: &str) -> Result<bool, reqwest::Error> {
    info!("Validating image URL: {}", url);
    
    // Send HEAD request with a reasonable timeout
    let response = client
        .head(url)
        .timeout(std::time::Duration::from_secs(10))
        .send()
        .await?;
    
    let is_valid = response.status().is_success();
    info!("Image URL validation result: {} (status: {})", is_valid, response.status());
    
    Ok(is_valid)
}

/// Health check endpoint
/// 
/// Simple endpoint to verify that the server is running and can connect
/// to the database.
pub async fn health_check(db: web::Data<DatabaseManager>) -> ActixResult<HttpResponse> {
    match db.ping().await {
        Ok(_) => Ok(HttpResponse::Ok().json(serde_json::json!({
            "status": "healthy",
            "database": "connected",
            "timestamp": chrono::Utc::now()
        }))),
        Err(e) => {
            error!("Health check failed: {}", e);
            Ok(HttpResponse::ServiceUnavailable().json(serde_json::json!({
                "status": "unhealthy",
                "database": "disconnected",
                "error": e.to_string(),
                "timestamp": chrono::Utc::now()
            })))
        }
    }
}