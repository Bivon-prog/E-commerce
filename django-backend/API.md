# API Documentation

## Base URL
```
http://localhost:8080/api/v1
```

## Endpoints

### Products

#### List Products
```
GET /products
```

**Query Parameters:**
- `brand` - Filter by brand (e.g., Apple, Samsung)
- `category` - Filter by category
- `price_tier` - Filter by price tier (Entry-Level, Budget, Mid-Range, etc.)
- `use_case` - Filter by use case (Gaming, Photography, etc.)
- `min_price` - Minimum price in cents
- `max_price` - Maximum price in cents

**Example:**
```
GET /products?brand=Apple&price_tier=Premium Flagship
```

#### Create Product
```
POST /products
```

**Body:**
```json
{
  "name": "iPhone 15 Pro",
  "brand": "Apple",
  "category": "Phone",
  "price": 14999900,
  "description": "Latest iPhone with A17 Pro chip",
  "images": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg"
  ],
  "in_stock": true,
  "stock_quantity": 50,
  "specs": {
    "ram": "8GB",
    "storage": "256GB"
  }
}
```

#### Get Product
```
GET /products/{id}
```

#### Update Product
```
PUT /products/{id}
```

#### Delete Product
```
DELETE /products/{id}
```

### Filter Options

#### Get Available Filters
```
GET /filter-options
```

**Response:**
```json
{
  "brands": ["Apple", "Samsung", "Google"],
  "price_tiers": ["Entry-Level", "Budget", "Mid-Range"],
  "use_cases": ["Gaming", "Photography", "General"],
  "price_range": {"min": 1000000, "max": 20000000}
}
```

### Health Check

#### Check API Status
```
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "database": "astra (connected)",
  "message": "Django backend is running with Astra database"
}
```

## Response Format

All responses follow this format:

**Success (200):**
```json
{
  "data": [...],
  "message": "Success"
}
```

**Error (400/500):**
```json
{
  "error": "Error message",
  "message": "Detailed error description"
}
```

## Notes

- Prices are stored in Kenyan Shillings (KES) as cents
- All products require at least one image
- Images are validated before saving