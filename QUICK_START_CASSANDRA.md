# Quick Start with Cassandra

## 🚀 Fastest Way to Get Started

### 1. Start Cassandra (Docker)
```bash
docker run --name cassandra -p 9042:9042 -d cassandra:latest
```

Wait 30-60 seconds for Cassandra to initialize.

### 2. Initialize Database
```bash
cd django-backend
python manage.py init_cassandra
```

### 3. Start Backend
```bash
python manage.py runserver 8080
```

### 4. Start Frontend
```bash
cd client
npm run dev
```

### 5. Test
Open http://localhost:5173 in your browser.

## ✅ Verify Installation

```bash
# Check Cassandra is running
docker ps

# Check health endpoint
curl http://localhost:8080/api/v1/health

# Should return:
# {
#   "status": "healthy",
#   "database": "connected",
#   "message": "Django backend is running with Cassandra"
# }
```

## 🔧 Useful Commands

### Cassandra Management
```bash
# Stop Cassandra
docker stop cassandra

# Start Cassandra
docker start cassandra

# View logs
docker logs cassandra

# Remove container
docker rm -f cassandra
```

### CQL Shell (Cassandra Query Language)
```bash
# Connect to Cassandra
docker exec -it cassandra cqlsh

# Inside cqlsh:
USE ecommerce;
SELECT * FROM products;
SELECT COUNT(*) FROM products;
DESCRIBE TABLE products;
```

### Django Management
```bash
# Initialize Cassandra
python manage.py init_cassandra

# Run migrations (for Django admin)
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver 8080
```

## 📊 Test API

### Create Product
```bash
curl -X POST http://localhost:8080/api/v1/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Phone",
    "brand": "TestBrand",
    "category": "Phone",
    "price": 50000,
    "description": "Test product",
    "specs": {"ram": "8GB", "storage": "128GB"},
    "images": ["https://via.placeholder.com/400"],
    "in_stock": true,
    "stock_quantity": 10
  }'
```

### Get All Products
```bash
curl http://localhost:8080/api/v1/products
```

### Filter by Brand
```bash
curl "http://localhost:8080/api/v1/products?brand=Apple"
```

## 🐛 Troubleshooting

### "Connection refused"
- Wait 30-60 seconds after starting Cassandra
- Check: `docker logs cassandra`

### "Keyspace does not exist"
- Run: `python manage.py init_cassandra`

### "Module not found: cassandra"
- Run: `pip install -r requirements.txt`

### Port 9042 already in use
```bash
# Find process using port
netstat -ano | findstr :9042

# Kill process or use different port
docker run --name cassandra -p 9043:9042 -d cassandra:latest
```

## 📚 Full Documentation

- [CASSANDRA_SETUP.md](django-backend/CASSANDRA_SETUP.md) - Detailed setup
- [CASSANDRA_MIGRATION.md](CASSANDRA_MIGRATION.md) - Migration details
- [django-backend/README.md](django-backend/README.md) - API documentation

## 🎯 Production Checklist

- [ ] Set `DEBUG=False` in `.env`
- [ ] Change `SECRET_KEY` to secure random value
- [ ] Configure replication factor > 1
- [ ] Set up monitoring (DataStax OpsCenter)
- [ ] Configure backups (`nodetool snapshot`)
- [ ] Enable authentication
- [ ] Configure SSL/TLS
- [ ] Set up load balancer
- [ ] Configure proper ALLOWED_HOSTS
- [ ] Set up logging aggregation

## 💡 Tips

1. **Use Docker for Development**: Easiest way to run Cassandra locally
2. **Wait for Initialization**: Cassandra takes 30-60 seconds to start
3. **Check Logs**: `docker logs cassandra` shows startup progress
4. **Use cqlsh**: Great for debugging and manual queries
5. **Indexes**: Already created for brand and category filtering
6. **UUIDs**: Products use UUID instead of ObjectId
7. **Specs**: Stored as JSON string, parsed automatically

## 🔗 Quick Links

- Cassandra: http://localhost:9042
- Django Backend: http://localhost:8080
- React Frontend: http://localhost:5173
- Health Check: http://localhost:8080/api/v1/health
- API Docs: http://localhost:8080/api/v1/products
