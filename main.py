from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app=FastAPI()

class Productos(BaseModel):
    nombre: str
    cantidad: int
    precio: float
class Pedidos(BaseModel):
    cliente: str
    productos: List[Productos]
    fecha: str

@app.post("/pedidos")
async def registrar_pedido(pedido: Pedidos):
    return {"ok": True,"pedido":pedido}

@app.get("/")
async def home():
    return{"message":"Bienvenidos a la API de pedidos"}