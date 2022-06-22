import requests

pedidos={
    "cliente": "Juan",
    "productos":[
        {"id":2,"nombre":"Manzanas", "cantidad":2,"precio":10},
        {"id":12,"nombre":"gabs-deepweb", "cantidad":2,"precio":10},
        {"id":5,"nombre":"GabsPapper", "cantidad":2,"precio":10}
    ],
    "fecha":"2020-01-01"
}

if __name__ == "__main__":
    r=requests.post("https://microservicio-pedidos-distribu.herokuapp.com/pedidos", json=pedidos)
    if r.status_code==200:
        print(r.json())