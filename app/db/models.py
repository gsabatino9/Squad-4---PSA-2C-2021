from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


reclamos = Table("reclamos", Base.metadata,
                       Column("numero_cliente", ForeignKey("clientes.id"), primary_key=True),
                       Column("ticket_id", ForeignKey("tickets.id"), primary_key=True))


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    id_producto = Column(Integer, ForeignKey("productos.id"))
    id_version = Column(Integer, ForeignKey("productos.id_version"))
    id_empleado = Column(Integer)
    tittle = Column(String)
    description = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True)
    tipo = Column(String)
    severidad = Column(Integer)
    estado = Column(String)
    horas_dedicadas = Column(Integer, nullable= True)
    clientes = relationship("Cliente", secondary= reclamos,back_populates = "tickets")

class Producto(Base):
    __tablename__ = "productos"


    id = Column(Integer, primary_key=True, index=True)
    id_version = Column(Integer, primary_key=True, index=True)
    nombre_producto = Column(String)
    version = Column(Integer)



class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    razon_social = Column(String)
    cuit = Column(String)
    tickets = relationship("Ticket",secondary = reclamos, back_populates = "clientes")

class Resolucion(Base):
    __tablename__ = "resoluciones"
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    tarea_id = Column(Integer)



