from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None

@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "description": item.description}

