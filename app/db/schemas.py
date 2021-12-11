from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

from ..db.models import TicketState, TicketType

class Product(BaseModel):
    id: int
    name: str
    version: int

    class Config:
        orm_mode = True

class TicketCreate(BaseModel):
    title: str
    description: str
    product_id: int
    ticket_type: TicketType
    severity: int
    employee_id: int
    state: TicketState = TicketState.OPEN

class Ticket(TicketCreate):
    id: int
    employee_id: int
    created_at: datetime
    deleted_at: Optional[datetime]
    state: TicketState
    dedicated_hours: Optional[int]

    class Config:
        orm_mode = True


class TicketOut(Ticket):
    product: Product
