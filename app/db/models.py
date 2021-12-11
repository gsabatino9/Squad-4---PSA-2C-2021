import enum
from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


reclamos = Table("reclamos", Base.metadata,
                       Column("numero_cliente", ForeignKey("clientes.id"), primary_key=True),
                       Column("ticket_id", ForeignKey("tickets.id"), primary_key=True))


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
    
    product = relationship("Product", back_populates="ticket")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    version = Column(Integer)
    name = Column(String)
    created_at = Column(DateTime, server_default=func.now())

    ticket = relationship("Ticket", back_populates="product")




class Resolucion(Base):
    __tablename__ = "resoluciones"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    tarea_id = Column(Integer)
