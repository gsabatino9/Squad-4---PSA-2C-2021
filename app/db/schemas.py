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

class Task(BaseModel):
    id: int
    name: str
    description: str
    state: str
    id_project: int

class Employee(BaseModel):
    id: int
    name: str
    last_name: str

class Client(BaseModel):
    id: int
    CUIT: str
    razon_social: str

class TicketCreate(BaseModel):
    title: str
    description: str
    product_id: int
    ticket_type: TicketType
    severity: int
    employee_id: int
    state: TicketState = TicketState.OPEN

class TicketUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    product_id: Optional[int]
    ticket_type: Optional[TicketType]
    severity: Optional[int]
    employee_id: Optional[int]
    state: Optional[TicketState]

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
    clients: Optional[List[Client]]
    tasks: Optional[List[Task]]
    employee: Optional[Employee]

