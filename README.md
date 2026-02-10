# E-commerce Platform - Django Backend + React Frontend

A modern e-commerce platform built with Django REST Framework backend and React frontend, featuring mobile phones and accessories with multiple images per product.

## 🚀 Quick Start

```bash
# Install dependencies
npm run install-all

# Start both backend and frontend
npm start
```

## 📁 Project Structure

```
├── client/                 # React frontend (TypeScript + Vite)
├── django-backend/        # Django REST Framework backend + MongoDB
├── package.json           # Root package.json for scripts
└── SETUP.md              # Detailed setup instructions
```

## 🔧 Technology Stack

### Backend (Django + Cassandra)
- **Django 4.2.7** - Python web framework
- **Django REST Framework 3.14** - RESTful API toolkit
- **Apache Cassandra** - Distributed NoSQL database
- **scylla-driver** - Cassandra Python driver
- **django-cors-headers** - CORS support for React frontend
- **Requests** - HTTP client for image URL validation

### Frontend (React)
- **React 18** with TypeScript
- **Vite** - Fast build tool and dev server
- **React Router v6** - Client-side routing
- **Bootstrap 5** - UI framework
- **Axios** - HTTP client

## 🌟 Key Features

- **Multiple Images** - 3-5 images per product with carousel navigation
- **Image URL Validation** - Validates external image URLs before saving
- **Kenyan Shillings** - Prices stored in cents (KES)
- **Type Safety** - Full TypeScript on frontend
- **Connection Pooling** - Automatic MongoDB connection management
- **Real-time Cart** - React Context for cart state management
- **Backward Compatible** - Supports both old (single image) and new (multiple images) formats

## 📡 API Endpoints

- `GET /api/v1/health` - Health check
- `GET /api/v1/products` - Get all products (with filtering)
- `GET /api/v1/products/{id}` - Get product by ID
- `POST /api/v1/products` - Create new product
- `PUT /api/v1/products/{id}` - Update product
- `DELETE /api/v1/products/{id}` - Delete product

### Query Parameters
- `?brand=Apple` - Filter by brand
- `?category=Phone` - Filter by category
- `?in_stock=true` - Filter by stock status

## 🛠️ Development

```bash
# Backend only
cd django-backend && python manage.py runserver 8080

# Frontend only  
cd client && npm run dev

# Both together
npm start
```

## 📦 Product Catalog

- **11 Brands**: Apple, Samsung, Google, Xiaomi, OnePlus, Tecno, Infinix, Itel, Realme, Oppo, Vivo
- **57 Products**: 38 phones + 19 accessories
- **Multiple Images**: 16 products with 3-5 images each
- **Categories**: Phones, Chargers, Cases, Screen Protectors, Earphones, Power Banks

## 📚 Documentation

- [SETUP.md](./SETUP.md) - Detailed installation and configuration
- [django-backend/README.md](./django-backend/README.md) - Backend API documentation
- [FEATURES.md](./FEATURES.md) - Feature list and implementation details

## 🚀 Production Ready

- Environment-based configuration
- Comprehensive logging
- Error handling
- CORS configuration
- Image validation
- MongoDB connection pooling


