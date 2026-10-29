from enum import Enum
from pydantic import BaseModel, Field


class Categoria(str, Enum):
    software = "software"
    hardware = "hardware"
    impacto_social = "impacto social"
    IA = "Inteligencia Artificial"

class ProyectoIn(BaseModel):
    nombre: str = Field(min_length=2, max_length=120)
    equipo: list[str] = Field(min_length=1, max_length=5)
    categoria: Categoria

class Proyecto(ProyectoIn):
    id: int
