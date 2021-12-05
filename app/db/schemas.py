from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

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