from enum import Enum
from typing import Annotated
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from app.schemas import ProyectoIn, Proyecto, Categoria



app = FastAPI(title="Mini Evaluación EXPO IBERO")


#TODO: Cambiar despues a SQLModel
proyectos: dict[int, Proyecto] = {}
siguinete_id = 1


@app.get("/")
def raiz():
    return {"message": "Hola Mundo desde FASTAPI!"}

@app.post("/proyectos", response_model=Proyecto, status_code=201)
def crear_proyecto(datos: ProyectoIn):
    global siguinete_id
    proyecto = Proyecto(id = siguinete_id, **datos.dict())
    proyectos[proyecto.id] = proyecto
    siguinete_id += 1
    return proyecto

@app.get("/proyectos", response_model=list[Proyecto])
def listar_proyectos(
    categoria: Categoria | None = None,
    limite: Annotated[int, Query(ge=1, le=100)] = 10,
):
    resultado = [
        p for p in proyectos.values()
        if categoria is None or p.categoria == categoria
    ]
    return resultado[:limite]

@app.get("/proyectos/{proyecto_id}", response_model=Proyecto)
def obtener_proyecto(proyecto_id: int):
    if proyecto_id not in proyectos:
        raise HTTPException(status_code=404, detail="No hya proyecto")
    return proyectos[proyecto_id]