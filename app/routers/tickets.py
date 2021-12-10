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

@router.get("/", response_model=List[schemas.Ticket])
async def get_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tickets(db, skip, limit)

@router.post("/", response_model=schemas.Ticket)
async def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    return crud.create_ticket(db, ticket)

@router.get("/{ticket_id}")
async def read_item(ticket_id: str):
    return "Esto es un ticket con id" + ticket_id
