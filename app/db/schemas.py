from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

from app.db.models import Cliente


class TicketCreate(BaseModel):
    tittle: str
    description: str

class Ticket(TicketCreate):
    id: int
    tittle: str
    description: str
    created_at: datetime
    deleted_at: datetime = None


    class Config:
        orm_mode = True


class TicketOut(Ticket):
    clientes: List[Cliente]

class ClienteOut(Cliente):
    tickets: List[Ticket]