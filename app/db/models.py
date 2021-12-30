import enum
import requests
from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.hybrid import hybrid_property

from .database import Base
from ..config import settings


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

    @hybrid_property
    def clients(self):
        clientsResponse = requests.get(settings.clients_url)
        clients_mapped = list(map(lambda client: {**client, 'razon_social': client['razon social']}, clientsResponse.json()))
        clients_id = list(map(lambda claim: claim.client_id, self.claims))
        clients = list(filter(lambda client: client['id'] in clients_id, clients_mapped))
        return clients
    
    @hybrid_property
    def tasks(self):
        tasks = []
        for resolution in self.resolutions:
            task = requests.get(settings.tickets_url.format(resolution.task_id)).json()['results']
            if len(task) == 0:
                continue
            tasks.append(task[0])
        return tasks

    @hybrid_property
    def employee(self):
        if(self.employee_id == None):
            return None
        payload = {'ids': [self.employee_id]}
        employees = requests.get(settings.employee_url.format(self.employee_id), data=payload).json()
        if len(employees['data']) == 0:
            return None
        employee = list(filter(lambda e: e['id'] == self.employee_id, employees['data']))
        return employee[0] if len(employee) > 0 else None
        





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

