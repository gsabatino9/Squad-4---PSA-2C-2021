import enum
from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class TicketState(str, enum.Enum):
    OPEN =  "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    WAITING_DEVELOP = "WAITING_DEVELOP"
    WAITING_CLIENT = "WAITING_CLIENT"
    CLOSE = "CLOSE"

class TicketType(str, enum.Enum):
    BUG = "BUG"
    QUERY = "QUERY"

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    employee_id = Column(Integer)
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True)
    ticket_type = Column(Enum(TicketType))
    severity = Column(Integer)
    state = Column(Enum(TicketState))
    dedicated_hours = Column(Integer, nullable=True)
    
    product = relationship("Product", back_populates="tickets")
    resolutions = relationship("Resolution", back_populates="tickets")
    claims = relationship("Claim", back_populates="tickets")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    version = Column(Integer)
    name = Column(String)
    created_at = Column(DateTime, server_default=func.now())

    tickets = relationship("Ticket", back_populates="product")

class Resolution(Base):
    __tablename__ = "resolutions"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    task_id = Column(Integer)

    tickets = relationship("Ticket", back_populates="resolutions")

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    client_id = Column(Integer)
    
    tickets = relationship("Ticket", back_populates="claims")

