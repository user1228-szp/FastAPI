from app.routers import projects
from fastapi import FastAPI, APIRouter
from app.routers import evaluation

app = FastAPI(title="Mini Evaluación EXPO IBERO")

api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(evaluation.router)
api_v1.include_router(projects.router)

app.include_router(api_v1)

@app.get("/")
def raiz():
    return {"message": "Hola Mundo desde FASTAPI!"}
