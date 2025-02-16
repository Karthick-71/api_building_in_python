# API Building in Python with Redis

This project demonstrates how to build a RESTful API using FastAPI and Redis in Python for key-value data storage operations.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
- [Testing with cURL](#testing-with-curl)

## Overview

This project implements a simple key-value store API using:
- FastAPI for the web framework
- Redis for data storage
- Uvicorn as the ASGI server

## Prerequisites

- Python 3.7+
- Redis server
- FastAPI
- Uvicorn
- Redis Python client

## Installation

1. Install the required Python packages:
```bash
pip install fastapi
pip install uvicorn
pip install redis
```

2. Ensure Redis server is installed and running:
```bash
# Ubuntu/Debian
sudo apt-get install redis-server
sudo service redis-server start

# MacOS with Homebrew
brew install redis
brew services start redis
```

## Running the Server

Start the API server using Uvicorn:

```bash
uvicorn main:app --reload
```

The server will be available at:
- URL: `http://127.0.0.1:8000`
- The `--reload` flag enables auto-reload during development

## API Endpoints

### 1. Read Data
Retrieve a value by its key from Redis

```http
GET /read/{key}
```

**Response Example:**
```json
{
    "key": "Test2",
    "value": "Tk1"
}
```

### 2. Add Data
Add a new key-value pair to Redis

```http
POST /add/
```

**Request Body:**
```json
{
    "key": "Test2",
    "value": "Tk1"
}
```

### 3. Delete Data
Remove a key-value pair from Redis

```http
DELETE /delete/{key}
```

## Testing with cURL

### Read Data
```bash
curl --location --globoff 'http://127.0.0.1:8000/read/{key}'
```

### Add Data
```bash
curl --location 'http://0.0.0.0:8000/add/' \
--header 'Content-Type: application/json' \
--data '{
    "key": "Test2",
    "value": "Tk1"
}'
```

### Delete Data
```bash
curl --location --request DELETE 'http://127.0.0.1:8000/delete/{key}'
```

## Configuration

### Redis Configuration
By default, the application connects to Redis at:
- Host: localhost
- Port: 6379

To modify Redis connection settings, update the connection parameters in your application code:

```python
redis_client = redis.Redis(host='localhost', port=6379, db=0)
```

## Error Handling

The API includes error handling for common scenarios:
- Key not found
- Invalid data format
- Redis connection issues

## Development

To extend or modify this API:
1. The main application logic is in `main.py`
2. Redis operations are handled through the Redis Python client
3. API endpoints are defined using FastAPI decorators

