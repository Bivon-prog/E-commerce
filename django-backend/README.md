# E-commerce Backend

Django REST API backend for phone e-commerce platform using DataStax Astra (Cloud Cassandra).

## Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment**
   ```bash
   cp .env.astra.example .env
   # Edit .env with your Astra credentials
   ```

3. **Run server**
   ```bash
   python manage.py runserver 0.0.0.0:8080
   ```

## Features

- 44 phone products across 15 brands
- Advanced filtering (7 categories)
- Multiple images per product
- Cloud database (Astra)
- RESTful API

## API Endpoints

- `GET /api/v1/products` - List products with filtering
- `POST /api/v1/products` - Create product
- `GET /api/v1/products/{id}` - Get product
- `PUT /api/v1/products/{id}` - Update product
- `DELETE /api/v1/products/{id}` - Delete product
- `GET /api/v1/filter-options` - Get filter options
- `GET /api/v1/health` - Health check

## Management Scripts

- `python list_all_phones.py` - List all products
- `python update_images.py` - Update product images
- `python populate_full_catalog.py` - Populate database

## Tech Stack

- Django 4.2 + Django REST Framework
- DataStax Astra (Cloud Cassandra)
- AstraPy for database operations