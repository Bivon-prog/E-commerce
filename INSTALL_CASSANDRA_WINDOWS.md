# Install Cassandra on Windows

You have 3 options to install Cassandra on Windows:

## Option 1: Docker (Recommended - Easiest)

### Install Docker Desktop
1. Download Docker Desktop from: https://www.docker.com/products/docker-desktop/
2. Install and restart your computer
3. Start Docker Desktop

### Run Cassandra
```powershell
# Pull and start Cassandra
docker run --name cassandra -p 9042:9042 -d cassandra:latest

# Wait 30-60 seconds for initialization
Start-Sleep -Seconds 60

# Check if running
docker ps

# View logs
docker logs cassandra
```

### Verify
```powershell
# Should show cassandra container running
docker ps
```

---

## Option 2: Native Installation (More Complex)

### Prerequisites
1. **Install Java 8 or 11**
   - Download from: https://adoptium.net/
   - Choose: OpenJDK 11 (LTS)
   - Install and verify: `java -version`

### Download Cassandra
1. Go to: https://cassandra.apache.org/download/
2. Download latest 4.x version (e.g., apache-cassandra-4.1.3-bin.tar.gz)
3. Extract to `C:\cassandra`

### Configure Environment Variables
```powershell
# Run as Administrator
[System.Environment]::SetEnvironmentVariable('CASSANDRA_HOME', 'C:\cassandra', 'Machine')
[System.Environment]::SetEnvironmentVariable('Path', $env:Path + ';C:\cassandra\bin', 'Machine')
```

### Start Cassandra
```powershell
# Open new PowerShell window (to load new environment variables)
cd C:\cassandra\bin
.\cassandra.bat
```

### Verify
```powershell
# In another terminal
cd C:\cassandra\bin
.\cqlsh.bat localhost 9042
```

---

## Option 3: Use DataStax Astra (Cloud - Free Tier)

If local installation is problematic, use DataStax Astra (managed Cassandra):

1. Sign up at: https://astra.datastax.com/
2. Create a free database
3. Get connection details
4. Update `.env` with Astra credentials

---

## After Installation

### Initialize Database
```powershell
cd django-backend
python manage.py init_cassandra
```

### Start Backend
```powershell
python manage.py runserver 8080
```

### Test Connection
```powershell
curl http://localhost:8080/api/v1/health
```

---

## Troubleshooting

### "Connection refused" Error
- **Docker**: Wait 60 seconds after starting container
- **Native**: Check if Cassandra process is running in Task Manager
- **Port**: Ensure port 9042 is not blocked by firewall

### Java Not Found (Native Install)
```powershell
# Verify Java installation
java -version

# Should show: openjdk version "11.x.x"
```

### Cassandra Won't Start (Native)
- Check logs in `C:\cassandra\logs\system.log`
- Ensure you have at least 2GB free RAM
- Try running as Administrator

### Docker Not Starting
- Ensure Hyper-V is enabled (Windows Features)
- Restart Docker Desktop
- Check Docker Desktop logs

---

## Quick Test

After Cassandra is running:

```powershell
# Test with cqlsh (Docker)
docker exec -it cassandra cqlsh

# Test with cqlsh (Native)
cd C:\cassandra\bin
.\cqlsh.bat

# Inside cqlsh, run:
SELECT now() FROM system.local;
# Should return current timestamp
```

---

## Recommended: Docker

For development, Docker is the easiest option:
- No Java installation needed
- Easy to start/stop
- Easy to remove
- Consistent across all platforms

```powershell
# Install Docker Desktop, then:
docker run --name cassandra -p 9042:9042 -d cassandra:latest
Start-Sleep -Seconds 60
docker ps
```

That's it!
