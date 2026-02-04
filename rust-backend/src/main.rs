mod models;
mod database;
mod handlers;

use actix_web::{web, App, HttpServer, middleware::Logger};
use actix_cors::Cors;
use reqwest::Client as HttpClient;
use std::env;
use dotenv::dotenv;

use database::DatabaseManager;
use handlers::{create_product, get_products, get_product_by_id, health_check};

/// Main entry point for the Rust e-commerce backend
/// 
/// This function sets up and starts the Actix-web HTTP server with all
/// necessary middleware, routes, and application state.
/// 
/// **Actix-web Architecture Explanation:**
/// 
/// Actix-web is built on the Actor model, but in v4 it primarily uses async/await:
/// 
/// 1. **HTTP Server**: HttpServer manages multiple worker processes
/// 2. **Workers**: Each worker runs an event loop (Tokio runtime)
/// 3. **App Factory**: Creates new App instances for each worker
/// 4. **Request Processing**: Each request is handled as an async task
/// 5. **Shared State**: Application data is shared across all workers
/// 
/// **Concurrency Model:**
/// - Multiple worker processes (default: number of CPU cores)
/// - Each worker handles thousands of concurrent connections
/// - Async/await allows non-blocking I/O operations
/// - Connection pooling for database and HTTP clients
/// 
/// **Memory Safety:**
/// - Rust's ownership system prevents data races
/// - Arc<T> (Atomic Reference Counting) for shared state
/// - No garbage collection overhead
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // Initialize environment variables from .env file
    dotenv().ok();
    
    // Initialize logging system
    env_logger::init();
    
    log::info!("Starting E-commerce Backend Server");
    
    // Get configuration from environment variables
    let mongodb_uri = env::var("MONGODB_URI")
        .unwrap_or_else(|_| "mongodb://localhost:27017".to_string());
    let database_name = env::var("DATABASE_NAME")
        .unwrap_or_else(|_| "ecommerce".to_string());
    let server_host = env::var("SERVER_HOST")
        .unwrap_or_else(|_| "127.0.0.1".to_string());
    let server_port = env::var("SERVER_PORT")
        .unwrap_or_else(|_| "8080".to_string())
        .parse::<u16>()
        .expect("SERVER_PORT must be a valid port number");
    
    log::info!("Configuration:");
    log::info!("  MongoDB URI: {}", mongodb_uri);
    log::info!("  Database: {}", database_name);
    log::info!("  Server: {}:{}", server_host, server_port);
    
    // Initialize database connection
    // 
    // **Database Connection Pooling Deep Dive:**
    // 
    // The MongoDB driver creates a connection pool with these characteristics:
    // 1. **Pool Size**: Default 10 connections, configurable via URI options
    // 2. **Connection Lifecycle**:
    //    - Connections are created lazily when needed
    //    - Idle connections are kept alive with periodic pings
    //    - Failed connections are automatically replaced
    //    - Pool shrinks during low activity periods
    // 3. **Thread Safety**: The Client is Arc<T> internally, safe to clone
    // 4. **Load Balancing**: Automatically distributes operations across connections
    // 5. **Monitoring**: Built-in connection monitoring and health checks
    let db_manager = DatabaseManager::new(&mongodb_uri, &database_name)
        .await
        .expect("Failed to connect to MongoDB");
    
    // Test database connection
    db_manager.ping().await.expect("Failed to ping MongoDB");
    
    // Create HTTP client for image URL validation
    // 
    // **HTTP Client Connection Pooling:**
    // - reqwest::Client maintains connection pools per host
    // - Reuses TCP connections for multiple requests (HTTP/1.1 keep-alive)
    // - Supports HTTP/2 multiplexing for better performance
    // - Automatic retry logic and timeout handling
    // - DNS caching to avoid repeated lookups
    let http_client = HttpClient::builder()
        .timeout(std::time::Duration::from_secs(30))
        .pool_max_idle_per_host(10)
        .build()
        .expect("Failed to create HTTP client");
    
    log::info!("Starting HTTP server on {}:{}", server_host, server_port);
    
    // Start the HTTP server
    // 
    // **HttpServer Architecture:**
    // 1. **Master Process**: Manages worker processes and handles signals
    // 2. **Worker Processes**: Each runs independently with its own event loop
    // 3. **Load Balancing**: OS kernel distributes incoming connections
    // 4. **Graceful Shutdown**: Workers finish current requests before stopping
    // 5. **Hot Reloading**: Can restart workers without dropping connections
    HttpServer::new(move || {
        // **App Factory Function:**
        // This closure is called once per worker process to create the App instance
        // Each worker gets its own copy of the application with shared state
        
        // Configure CORS for cross-origin requests
        // This allows our React frontend to make requests to the API
        let cors = Cors::default()
            .allowed_origin("http://localhost:3000") // React dev server
            .allowed_origin("http://localhost:5173") // Vite dev server
            .allowed_origin("http://localhost:5174") // Vite dev server (alt port)
            .allowed_origin("http://localhost:5175") // Vite dev server (alt port)
            .allowed_methods(vec!["GET", "POST", "PUT", "DELETE"])
            .allowed_headers(vec!["Content-Type", "Authorization"])
            .max_age(3600);
        
        App::new()
            // **Middleware Registration:**
            // Middleware runs in the order it's registered
            .wrap(Logger::default()) // HTTP request logging
            .wrap(cors) // CORS headers
            
            // **Application State:**
            // web::Data<T> makes data available to all handlers
            // It's essentially Arc<T> - atomic reference counting for thread safety
            // Each worker process gets a clone of this data
            .app_data(web::Data::new(db_manager.clone()))
            .app_data(web::Data::new(http_client.clone()))
            
            // **Route Configuration:**
            // Routes are matched in the order they're defined
            // Path parameters are extracted automatically
            // Query parameters are parsed into structs
            .route("/health", web::get().to(health_check))
            .service(
                web::scope("/api/v1")
                    .route("/products", web::post().to(create_product))
                    .route("/products", web::get().to(get_products))
                    .route("/products/{id}", web::get().to(get_product_by_id))
            )
    })
    .bind(format!("{}:{}", server_host, server_port))?
    .run()
    .await
}