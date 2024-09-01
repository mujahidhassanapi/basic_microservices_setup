import httpx
from fastapi import FastAPI

app = FastAPI()

@app.get("/create-item/")
async def create_item():
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8000/items/", json={"name": "Test Item", "description": "This is a test item"})
        return response.json()
