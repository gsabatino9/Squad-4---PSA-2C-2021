from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import crud, schemas
from ..db.database import get_db


router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[schemas.Product])
async def get_tickets(db: Session = Depends(get_db)):
    return crud.get_products(db)
