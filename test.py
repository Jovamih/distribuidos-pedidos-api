import requests
import json

with open('data.json') as f:
    pedidos = json.load(f)

if __name__ == "__main__":
    online="https://microservicio-pedidos-distribu.herokuapp.com/pedidos"
    offline="http://127.0.0.1:85/pedidos"

    print(pedidos)
    r=requests.post(offline, json=pedidos)
    if r.status_code==200:
        print(r.json())