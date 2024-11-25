from pydantic import BaseModel, Field
from datetime import date

class UsuarioDTOPeticion(BaseModel):
    nombre:str
    edad:int
    telefono:str
    correo:str 
    contraseña:str
    fechaRegistro:date
    ciudad:str 
    class Config:
        orm_mode=True

class UsuarioDTORespuesta(BaseModel):
    id:int
    nombre:str
    telefono: str
    ciudad: str
    class Config:
        orm_mode=True


class GastoDTOPeticion(BaseModel):
    descripcion:str
    monto:str
    fechaGasto:date
    categoria:str
    class Config:
        orm_model=True

class GastoDTORespuesta(BaseModel):
    id:int
    categoria:str
    monto:str
    fechaGasto:date
    class Config:
        orm_mode:True


class CategoriaDTOPeticion(BaseModel):
    nombreCategoria:str
    descripcionCategoria:str
    class Config:
        orm_mode:True

class CategoriaDTORespuesta(BaseModel):
    id:int
    nombreCategoria:str
    descripcionCategoria:str
    class Config:
        orm_mode:True

class MetodoPagoDTOPeticion(BaseModel):
    nombreMetodo: str
    descripcionPago:str
    tipoPago:str
    class Config:
        orm_mode:True

class MetodoPagoDTORespuesta(BaseModel):
    id:int
    nombreMetodo:str
    descripcionPago:str
    tipoPago:str
    class Config:
        orm_mode:True


        





