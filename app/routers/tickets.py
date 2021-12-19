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

@router.get("/{ticket_id}", response_model=schemas.TicketOut)
async def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    return crud.get_ticket(db, ticket_id)

@router.get("/", response_model=List[schemas.TicketOut])
async def get_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tickets(db, skip, limit)

@router.post("/", response_model=schemas.TicketOut)
async def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    return crud.create_ticket(db, ticket)  

@router.put("/{ticket_id}/title", response_model=schemas.TicketOut)
async def update_title(ticket_id: int, title: str, db: Session = Depends(get_db)):
    return crud.update_ticket(db, ticket_id, {'title': title})

@router.put("/{ticket_id}/clients", response_model=schemas.TicketOut)
async def update_clients(ticket_id: int, clients: List[int], db: Session = Depends(get_db)):
    return crud.update_claims(db, ticket_id, clients)

@router.put("/{ticket_id}/tasks", response_model=schemas.TicketOut)
async def update_tasks(ticket_id: int, tasks: List[int], db: Session = Depends(get_db)):
    return crud.update_tasks(db, ticket_id, tasks)

@router.put("/{ticket_id}", response_model=schemas.TicketOut)
async def update_ticket(ticket_id: int, ticket: schemas.TicketUpdate, db: Session = Depends(get_db)):
    ticketFiltered = {k: v for k, v in ticket.dict().items() if v is not None}
    return crud.update_ticket(db, ticket_id, ticketFiltered)
