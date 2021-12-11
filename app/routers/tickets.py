from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import crud, schemas
from ..db.database import get_db


router = APIRouter(
    prefix="/tickets",
    tags=["tickets"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[schemas.TicketOut])
async def get_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tickets(db, skip, limit)

@router.post("/", response_model=schemas.TicketOut)
async def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    return crud.create_ticket(db, ticket)

@router.get("/{ticket_id}", response_model=schemas.TicketOut)
async def read_item(ticket_id: int, db: Session = Depends(get_db)):
    return crud.get_ticket(db, ticket_id)
