import requests

pedidos={
    "cliente": "Juan",
    "productos":[
        {"nombre":"Manzanas", "cantidad":2,"precio":10},
        {"nombre":"Manzanas", "cantidad":2,"precio":10},
        {"nombre":"Manzanas", "cantidad":2,"precio":10}
    ],
    "fecha":"2020-01-01",
}

if __name__ == "__main__":
    r=requests.post("http://localhost:8000/pedidos", json=pedidos)
    if r.status_code==200:
        print(r.json())