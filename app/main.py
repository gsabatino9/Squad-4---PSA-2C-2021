from fastapi import FastAPI

from .routers import tickets

app = FastAPI()

app.include_router(tickets.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
