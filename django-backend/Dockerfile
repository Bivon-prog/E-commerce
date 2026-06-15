# Use official python slim image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (needed for compiling C-extensions in python packages like scylla-driver if wheels are missing)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency list and install them
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend files
COPY . /app/

# Expose port 8082
EXPOSE 8082

# Start the application using gunicorn with increased timeout for DB cache load
CMD ["gunicorn", "--bind", "0.0.0.0:8082", "--timeout", "120", "ecommerce.wsgi:application"]
