from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.schemas.DTO import GastoDTOPeticion, GastoDTORespuesta
from app.api.schemas.DTO import CategoriaDTOPeticion, CategoriaDTORespuesta
from app.api.schemas.DTO import MetodoPagoDTOPeticion, MetodoPagoDTORespuesta
from app.api.models.modelosApp import Usuario
from app.api.models.modelosApp import Gasto
from app.api.models.modelosApp import Categoria
from app.api.models.modelosApp import MetodoPago

from app.database.configuration import sessionLocal, engine

#Para que un api funcione debe tener un archivo enrutador
rutas=APIRouter() #ENDPOINTS

#Crear una funcion para establecer cuando yo quiera y necesite
#conexion hacia la base de datos
def getDataBase():
    basedatos=sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()

#PROGRAMACION DE CADA UNO DE LOS SERVICIOS
#QUE OFRECERA NUESTRA API

#SERVICIO PARA REGISTRAR O GUARDAR UN USUARIO EN BD
@rutas.post("/usuarios", response_model=UsuarioDTORespuesta)
def guardarUsuario(datosPeticion:UsuarioDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        usuario=Usuario(
            nombres=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            correo=datosPeticion.correo,
            contraseña=datosPeticion.contraseña,
            fechaRegistro=datosPeticion.fechaRegistro,
            ciudad=datosPeticion.ciudad
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return UsuarioDTORespuesta(
            id=usuario.id,
            nombre=usuario.nombres,  # Asegúrate de usar el campo correcto
            telefono=usuario.telefono,
            ciudad=usuario.ciudad
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario")
    
@rutas.get("/usuarios", response_model=List[UsuarioDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Usuario).all()
        return [
            UsuarioDTORespuesta(
                id=usuario.id,
                nombre=usuario.nombres, 
                telefono=usuario.telefono,
                ciudad=usuario.ciudad
            ) for usuario in listadoDeUsuarios
        ]
    except Exception as error:
        db.rollback()
        raise HTTPException()
    
@rutas.post("/gastos", response_model=GastoDTORespuesta)
def guardarGasto(datosPeticion:GastoDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        gasto=Gasto(
            descripcion=datosPeticion.descripcion,   
            monto=datosPeticion.monto,
            fechaGasto=datosPeticion.fechaGasto,
            categoria=datosPeticion.categoria
        )
        db.add(gasto)
        db.commit()
        db.refresh(gasto)
        return GastoDTORespuesta(
            id=gasto.id,
            categoria=gasto.categoria,
            monto=gasto.monto,
            fechaGasto=gasto.fechaGasto
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el gasto {error}")
    
@rutas.get("/gastos", response_model=List[GastoDTORespuesta])
def buscarGasto(db:Session=Depends(getDataBase)):
    try:
        listadoDeGastos=db.query(Gasto).all()
        return [
            GastoDTORespuesta(
                id=gasto.id,
                categoria=gasto.categoria,
                monto=gasto.monto,
                fechaGasto=gasto.fechaGasto
            ) for gasto in listadoDeGastos
        ]
    except Exception as error:
        db.rollback()
        raise HTTPException()

@rutas.post("/categorias", response_model=CategoriaDTORespuesta)
def guardarCategoria(datosPeticion:CategoriaDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        categoria=Categoria(
            nombreCategoria=datosPeticion.nombreCategoria,
            descripcionCategoria=datosPeticion.descripcionCategoria
        )
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return CategoriaDTORespuesta(
            id=categoria.id,
            nombreCategoria=categoria.nombreCategoria,
            descripcionCategoria=categoria.descripcionCategoria
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar la categoria")
    
@rutas.get("/categorias", response_model=List[CategoriaDTORespuesta])
def buscarCategoria(db:Session=Depends(getDataBase)):
    try:
        listadoDeCategorias=db.query(Categoria).all()
        return [
            CategoriaDTORespuesta(
                id=categoria.id,
                nombreCategoria=categoria.nombreCategoria,
                descripcionCategoria=categoria.descripcionCategoria
            ) for categoria in listadoDeCategorias
        ]
    except Exception as error:
        db.rollback()
        raise HTTPException()
    
@rutas.post("/metodosPago", response_model=MetodoPagoDTORespuesta)
def guardarMetodoPago(datosPeticion: MetodoPagoDTOPeticion, db: Session = Depends(getDataBase)):
    try:
        metodoPago = MetodoPago(
            nombreMetodo=datosPeticion.nombreMetodo,
            descripcionPago=datosPeticion.descripcionPago, 
            tipoPago=datosPeticion.tipoPago
        )
        db.add(metodoPago)
        db.commit()
        db.refresh(metodoPago)
        return MetodoPagoDTORespuesta(
            id=metodoPago.id,
            nombreMetodo=metodoPago.nombreMetodo,
            descripcionPago=metodoPago.descripcionPago,
            tipoPago=metodoPago.tipoPago
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el metodo de pago: {str(error)}")
    
@rutas.get("/metodosPago", response_model=List[MetodoPagoDTORespuesta])
def buscarMetodoPago(db: Session = Depends(getDataBase)):
    try:
        listadoDeMetodosDePago = db.query(MetodoPago).all()
        return [
            MetodoPagoDTORespuesta(
                id=metodoPago.id,
                nombreMetodo=metodoPago.nombreMetodo,
                descripcionPago=metodoPago.descripcionPago,
                tipoPago=metodoPago.tipoPago
            ) for metodoPago in listadoDeMetodosDePago
        ]
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al buscar los métodos de pago")
    

    



