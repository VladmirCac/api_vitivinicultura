from fastapi import FastAPI

from .core.database import Base, engine
from .models.usuario import Usuario

app = FastAPI(
    title="api_vitivinicultura",
    version="1.0.0",
    description="API inserção de dados de modelo de predição"
)

@app.get("/")
async def home():
    return "Olá todo mundo"