from sqlalchemy.orm import Session
from typing import List, Optional

from . import models, schemas

def get_ticket(db: Session, ticket_id: int):
    db_ticket = db.query(models.Ticket).filter(models.Ticket.id==ticket_id).first()
    return db_ticket

def get_tickets(db: Session, skip: int = 0, limit: int = 100):
    db_tickets = db.query(models.Ticket).offset(skip).limit(limit).all()
    return db_tickets


def create_ticket(db: Session, ticket: schemas.TicketCreate):
    db_ticket = models.Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def update_ticket(db: Session, ticket_id: int, ticket_update: schemas.TicketUpdate):
    db.query(models.Ticket).filter(models.Ticket.id==ticket_id).update(ticket_update)
    db.commit()
    db_ticket = db.query(models.Ticket).filter(models.Ticket.id==ticket_id).first()
    return db_ticket

def update_claims(db: Session, ticket_id: int, clients_id: List[int]):
    db.query(models.Claim).filter(models.Claim.ticket_id==ticket_id).delete()
    db.add_all(map(lambda client_id: models.Claim(ticket_id=ticket_id, client_id=client_id), clients_id))
    db.commit()
    db_ticket = db.query(models.Ticket).filter(models.Ticket.id==ticket_id).first()
    return db_ticket

def update_tasks(db: Session, ticket_id: int, tasks_id: List[int]):
    db.query(models.Resolution).filter(models.Resolution.ticket_id==ticket_id).delete()
    db.add_all(map(lambda task_id: models.Resolution(ticket_id=ticket_id, task_id=task_id), tasks_id))
    db.commit()
    db_ticket = db.query(models.Ticket).filter(models.Ticket.id==ticket_id).first()
    return db_ticket
