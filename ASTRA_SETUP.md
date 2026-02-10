# DataStax Astra Setup Guide (Cloud Cassandra)

DataStax Astra is a managed Cassandra database-as-a-service with a free tier. Perfect for development and production!

## Step 1: Create Astra Account

1. Go to https://astra.datastax.com/
2. Click "Get Started Free"
3. Sign up with email or Google/GitHub
4. Verify your email

## Step 2: Create Database

1. Click "Create Database"
2. Fill in details:
   - **Database name**: `ecommerce-db`
   - **Keyspace name**: `ecommerce`
   - **Provider**: AWS, Google Cloud, or Azure (choose closest region)
   - **Region**: Choose closest to you (e.g., us-east-1)
3. Click "Create Database"
4. Wait 2-3 minutes for database to become "Active"

## Step 3: Get Connection Details

### Option A: Secure Connect Bundle (Recommended)

1. In your database dashboard, click "Connect"
2. Click "Drivers" tab
3. Download "Secure Connect Bundle" (a .zip file)
4. Save it to: `django-backend/secure-connect-ecommerce-db.zip`

### Option B: Get Connection Details

1. In database dashboard, note:
   - **Database ID**: (long UUID)
   - **Region**: (e.g., us-east-1)
   - **Keyspace**: ecommerce

## Step 4: Create Application Token

1. Go to "Settings" → "Application Tokens"
2. Click "Generate Token"
3. Select role: "Database Administrator"
4. Click "Generate Token"
5. **IMPORTANT**: Copy and save these (shown only once):
   - **Client ID**: `xxxxx`
   - **Client Secret**: `xxxxx`
   - **Token**: `AstraCS:xxxxx`

## Step 5: Configure Django Backend

Update `django-backend/.env`:

```env
# Astra Configuration
ASTRA_DB_ID=your-database-id
ASTRA_DB_REGION=us-east-1
ASTRA_DB_KEYSPACE=ecommerce
ASTRA_CLIENT_ID=your-client-id
ASTRA_CLIENT_SECRET=your-client-secret
ASTRA_TOKEN=AstraCS:your-token

# Or use Secure Connect Bundle
ASTRA_SECURE_BUNDLE_PATH=secure-connect-ecommerce-db.zip

# Django settings
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Step 6: Install Astra Driver

```bash
cd django-backend
pip install cassandra-driver
pip install astrapy
```

## Step 7: Initialize Database

```bash
python manage.py init_cassandra
```

## Step 8: Start Backend

```bash
python manage.py runserver 8080
```

## Step 9: Test

```bash
curl http://localhost:8080/api/v1/health
```

Expected response:
```json
{
  "status": "healthy",
  "database": "connected",
  "message": "Django backend is running with Cassandra"
}
```

## Astra Free Tier Limits

- **Storage**: 25 GB
- **Reads**: 30 million per month
- **Writes**: 5 million per month
- **Bandwidth**: 50 GB per month

Perfect for development and small production apps!

## Connection Methods

### Method 1: Secure Connect Bundle (Easiest)

```python
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config = {
    'secure_connect_bundle': 'secure-connect-ecommerce-db.zip'
}

auth_provider = PlainTextAuthProvider(
    username='token',
    password='AstraCS:your-token'
)

cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('ecommerce')
```

### Method 2: Direct Connection

```python
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

auth_provider = PlainTextAuthProvider(
    username='your-client-id',
    password='your-client-secret'
)

cluster = Cluster(
    contact_points=[f'{db_id}-{region}.db.astra.datastax.com'],
    port=29042,
    auth_provider=auth_provider
)
session = cluster.connect('ecommerce')
```

## Astra Dashboard Features

- **CQL Console**: Run queries directly in browser
- **Metrics**: Monitor database performance
- **Data Explorer**: Browse tables and data
- **Backups**: Automatic daily backups
- **Monitoring**: Real-time metrics and alerts

## Using CQL Console

1. Go to your database in Astra
2. Click "CQL Console"
3. Run queries:

```sql
USE ecommerce;

-- View tables
DESCRIBE TABLES;

-- View products
SELECT * FROM products;

-- Count products
SELECT COUNT(*) FROM products;
```

## Troubleshooting

### "Unable to connect"
- Check database is "Active" in Astra dashboard
- Verify token is correct
- Ensure secure bundle path is correct

### "Keyspace not found"
- Run: `python manage.py init_cassandra`
- Or create manually in CQL Console:
  ```sql
  CREATE KEYSPACE IF NOT EXISTS ecommerce
  WITH replication = {'class': 'NetworkTopologyStrategy', 'datacenter1': 3};
  ```

### "Authentication failed"
- Regenerate token in Astra dashboard
- Update .env with new token

## Benefits of Astra

✅ No local installation needed
✅ Automatic backups
✅ High availability (3 replicas)
✅ Global distribution
✅ Free tier (25GB storage)
✅ Managed updates and patches
✅ Built-in monitoring
✅ CQL console in browser

## Production Considerations

- Use environment variables for credentials
- Never commit secure bundle or tokens to git
- Enable IP allowlist in Astra for security
- Monitor usage in Astra dashboard
- Set up alerts for quota limits

## Resources

- Astra Docs: https://docs.datastax.com/en/astra/
- Astra Dashboard: https://astra.datastax.com/
- Python Driver Docs: https://docs.datastax.com/en/developer/python-driver/
- Support: https://community.datastax.com/
