from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import requests

from modula import Database

app=FastAPI()

class Productos(BaseModel):
    id: int
    nombre: str
    cantidad: int
    precio: float
class Pedidos(BaseModel):
    cliente: str
    productos: List[Productos]
    fecha: str

def validate_product(pedido):
    for producto in pedido["productos"]:
        try:
            r=requests.get(f"http://localhost:8000/stock?id={producto['id']}",timeout=120)
            if r.status_code==200:
                prod=r.json()
                if prod["message"] != "true":
                    return {"ok": False, "error": "Producto no encontrado"}
                stock=prod["cantidad"]
                if stock<producto["cantidad"]:
                    return {"ok": False, "error": "No hay stock suficiente"}
        except:
            return {"ok": False, "error": "Error de conexion"}
    return {"ok": True, "error": None}

@app.post("/pedidos")
async def registrar_pedido(response: Pedidos):
    #primero consultamos el stock de la base de datos
    pedido=response.dict()
    #validamos los productos
    validacion=validate_product(pedido)
    if validacion["ok"]==False:
       # return validacion
       pass
    #registramos el pedido
    database=Database()
    result=database.registrar_pedido(pedido)
    database.close()

    #envio los datos al modulo de factura
    response=requests.post("https://microservicio-facturas.herokuapp.com/api/factura/create", json=pedido,timeout=120)
    return response.json()

@app.get("/")
async def home():
    return{"message":"Bienvenidos a la API de pedidos"}