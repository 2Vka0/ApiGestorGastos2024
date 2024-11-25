from sqlalchemy import Column,Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Crear una instancia de la base para crear tablas
Base=declarative_base()



class Usuario(Base):
    __tablename__='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(20))
    contraseña=Column(String(10))
    fechaRegistro=Column(Date)
    ciudad=Column(String(50))

class Gasto(Base):
    __tablename__='gastos'
    id=Column(Integer, primary_key=True, autoincrement=True)
    descripcion=Column(String(100))
    monto=Column(String(50))
    fechaGasto=Column(Date)
    categoria=Column(String(50))
    
class Categoria(Base):
    __tablename__='categorias'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreCategoria=Column(String(50))
    descripcionCategoria=Column(String(50))

    
class MetodoPago(Base):
    __tablename__='metodosPago'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreMetodo=Column(String(50))
    descripcionPago=Column(String(50))
    tipoPago=Column(String(50))




