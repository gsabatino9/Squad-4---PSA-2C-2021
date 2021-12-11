from sqlalchemy.orm import Session

from . import models, schemas

def get_ticket(db: Session, ticket_id: int):
    db_ticket = db.query(models.Ticket).filter(models.Ticket.id==ticket_id).first()
    return db_ticket

def get_tickets(db: Session, skip: int = 0, limit: int = 100):
    db_tickets = db.query(models.Ticket).offset(skip).limit(limit).all()
    return db_tickets


def create_ticket(db: Session, ticket: schemas.TicketCreate):
    db_ticket = models.Ticket(title=ticket.title, description=ticket.description, product_id=ticket.product_id,
                              employee_id=ticket.employee_id, ticket_type=ticket.ticket_type, severity=ticket.severity, state=ticket.state)
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket
