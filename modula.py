import sqlite3
import os
import requests

class Database(object):
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Pedidos (id INTEGER PRIMARY KEY AUTOINCREMENT, cliente TEXT,  fecha TEXT);")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS PedidosProductos (id INTEGER REFERENCES Pedidos(id), nombre TEXT,  cantidad NUMERIC, precio NUMERIC);")
        self.db.commit()
    def registrar_pedido(self, pedido):
        self.cursor.execute("INSERT INTO Pedidos(cliente, fecha) VALUES (?,?)", (pedido['cliente'], pedido['fecha']))
        id_last=self.cursor.lastrowid
        for producto in pedido['productos']:
            self.cursor.execute("INSERT INTO PedidosProductos(id, nombre, cantidad, precio) VALUES (?,?,?,?)", (id_last, producto['nombre'], producto['cantidad'], producto['precio']))
        #return {"ok": True, "id": id_last}
        self.db.commit()
        return {"ok": True, "id": id_last}
    def close(self):
        self.db.close()