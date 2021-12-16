from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .routers import tickets, products
from .config import settings
from .db.database import get_db

app = FastAPI(dependencies=[Depends(get_db)])

app.include_router(tickets.router)
app.include_router(products.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
