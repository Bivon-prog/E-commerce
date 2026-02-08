# Django E-commerce Backend

High-performance REST API backend for mobile phone e-commerce platform using Django REST Framework and MongoDB.

## Features

- **Django REST Framework**: Modern REST API with automatic serialization
- **MongoDB Integration**: NoSQL database using pymongo
- **Image Validation**: Validates external image URLs before saving
- **Multiple Images**: Support for 3-5 images per product with backward compatibility
- **CORS Enabled**: Configured for React frontend on multiple ports
- **Kenyan Shillings**: Prices stored in cents (KES)

## Tech Stack

- Python 3.8+
- Django 4.2.7
- Django REST Framework 3.14.0
- MongoDB (pymongo 4.6.0)
- django-cors-headers 4.3.1

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables in `.env`:
```
MONGODB_URI=mongodb://localhost:27017
DATABASE_NAME=ecommerce_db
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

3. Run migrations (for Django admin only):
```bash
python manage.py migrate
```

4. Start the server:
```bash
python manage.py runserver 8080
```

## API Endpoints

### Health Check
- `GET /api/v1/health` - Check server and database status

### Products
- `GET /api/v1/products` - List all products (supports filtering)
- `POST /api/v1/products` - Create new product
- `GET /api/v1/products/<id>` - Get single product
- `PUT /api/v1/products/<id>` - Update product
- `DELETE /api/v1/products/<id>` - Delete product

### Query Parameters
- `?brand=Apple` - Filter by brand
- `?category=Phone` - Filter by category
- `?in_stock=true` - Filter by stock status

## Product Schema

```json
{
  "name": "iPhone 15 Pro",
  "brand": "Apple",
  "category": "Phone",
  "price": 14999900,
  "description": "Latest iPhone with A17 Pro chip",
  "specs": {
    "ram": "8GB",
    "storage": "256GB",
    "display": "6.1 inch"
  },
  "images": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpg"
  ],
  "in_stock": true,
  "stock_quantity": 50
}
```

## Image Validation

The backend validates all image URLs using HTTP HEAD requests before saving:
- Checks if URL is accessible (200 OK status)
- Validates each image in the array
- Returns error if any image fails validation

## Backward Compatibility

The API supports both old and new data formats:
- Old format: `image_url` (single string)
- New format: `images` (array of strings)
- Automatic migration on read operations

## Development

Run in development mode:
```bash
python manage.py runserver 8080
```

View logs:
```bash
# Logs are printed to console with INFO level
```

## MongoDB Connection

The backend connects to MongoDB using pymongo with connection pooling:
- Connection is established on first request
- Reused across all requests
- Automatic reconnection on failure

## CORS Configuration

Configured to accept requests from:
- http://localhost:3000
- http://localhost:5173
- http://localhost:5174
- http://localhost:5175

## Notes

- Prices are stored in cents (KES)
- All products require at least one image
- Image URLs must be publicly accessible
- MongoDB must be running on localhost:27017
