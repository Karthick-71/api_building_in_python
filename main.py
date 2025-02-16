from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from radis_connection import *

### Set env = local_redis_client (or) qa_redis_client
# redis_client = local_redis_client
redis_client = qa_redis_client

# Initialize FastAPI app
app = FastAPI()


# Define a Pydantic model for the request body when adding a new key
class KeyValue(BaseModel):
    key: str
    value: str


# Endpoint to add or update data in Redis
@app.post("/add")
async def add_data(data: KeyValue):
    try:
        # Set the key-value pair in Redis
        redis_client.set(data.key, data.value)
        return {"message": f"Key '{data.key}' set successfully with value '{data.value}'"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint to read data by index/key
@app.get("/read/{key}")
async def read_data(key: str):
    try:
        # Retrieve data from Redis
        value = redis_client.get(key)

        if value is None:
            raise HTTPException(status_code=404, detail="Key not found")

        # Return the retrieved value
        return {"key": key, "value": value}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint to delete data by index/key
@app.delete("/delete/{key}")
async def delete_data(key: str):
    try:
        # Delete the key from Redis
        result = redis_client.delete(key)

        if result == 0:
            raise HTTPException(status_code=404, detail="Key not found")

        return {"message": f"Key '{key}' deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Run the server using uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
