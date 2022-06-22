import sqlite3
import os
import requests

class Database(object):
    def __init__(self):
        self.db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/database.db")
        self.cursor = self.db.cursor()
        #self.cursor.execute("CREATE TABLE IF NOT EXISTS pedidos (id INTEGER PRIMARY KEY, nombre TEXT, direccion TEXT, telefono TEXT, email TEXT, fecha TEXT, hora TEXT, productos TEXT)")
    
    def registrar_pedido(self, item):
        self.cursor.execute("INSERT INTO pedidos (cliente, fecha) VALUES (%s, %s)", (item['cliente'], item['fecha']))
        id_last=self.cursor.lastrowid
        print(id_last)
        self.db.commit()