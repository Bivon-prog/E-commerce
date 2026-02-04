use mongodb::{Client, Collection, Database};
use crate::models::Product;
use anyhow::Result;

/// Database connection manager
/// 
/// This struct encapsulates the MongoDB connection and provides a clean interface
/// for database operations. It holds references to the database and collection
/// that we'll be working with.
/// 
/// **MongoDB Connection Pooling Explanation:**
/// The MongoDB Rust driver automatically manages connection pooling for us:
/// 
/// 1. **Connection Pool**: When we create a Client, it establishes a pool of
///    connections to the MongoDB server (default: 10 connections)
/// 
/// 2. **Automatic Management**: The driver automatically:
///    - Opens new connections when needed (up to max_pool_size)
///    - Reuses existing connections for new operations
///    - Closes idle connections after a timeout
///    - Handles connection failures and retries
/// 
/// 3. **Thread Safety**: The Client is thread-safe and can be shared across
///    multiple async tasks without additional synchronization
/// 
/// 4. **Performance Benefits**:
///    - Eliminates connection setup/teardown overhead
///    - Allows concurrent operations across multiple connections
///    - Automatically handles network issues and reconnection
#[derive(Clone)]
pub struct DatabaseManager {
    pub client: Client,
    pub database: Database,
    pub products: Collection<Product>,
}

impl DatabaseManager {
    /// Create a new database manager with connection to MongoDB
    /// 
    /// This function establishes the connection to MongoDB and sets up
    /// the database and collection references.
    /// 
    /// **Connection Process:**
    /// 1. Parse the MongoDB URI (contains host, port, credentials, options)
    /// 2. Create a Client with connection pool settings
    /// 3. Get reference to the specific database
    /// 4. Get reference to the products collection
    /// 
    /// **Error Handling:**
    /// - Returns Result<DatabaseManager, anyhow::Error>
    /// - Connection errors are propagated up to the caller
    /// - The actual connection is lazy - it happens on first operation
    pub async fn new(uri: &str, db_name: &str) -> Result<Self> {
        log::info!("Connecting to MongoDB at: {}", uri);
        
        // Create MongoDB client with automatic connection pooling
        // The client will manage a pool of connections automatically
        let client = Client::with_uri_str(uri).await?;
        
        // Get reference to the database
        let database = client.database(db_name);
        
        // Get reference to the products collection
        // MongoDB will create this collection automatically when we insert the first document
        let products = database.collection::<Product>("products");
        
        log::info!("Successfully connected to MongoDB database: {}", db_name);
        
        Ok(DatabaseManager {
            client,
            database,
            products,
        })
    }
    
    /// Test the database connection
    /// 
    /// This function performs a simple ping operation to verify that
    /// the database connection is working properly.
    pub async fn ping(&self) -> Result<()> {
        self.database.run_command(mongodb::bson::doc! {"ping": 1}, None).await?;
        log::info!("Database ping successful");
        Ok(())
    }
}