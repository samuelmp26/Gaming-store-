import json
from .producto import Producto
from .movimiento import RegistroMovimiento

class Persistencia:
    def _init_(self, ruta_inventario="data/inventario.json", ruta_movimientos="data/movimientos.json"):
        self.ruta_inventario = ruta_inventario
        self.ruta_movimientos = ruta_movimientos

    def guardar_inventario(self, inventario):
        pass

    def cargar_inventario(self):
        pass
    def guardar_registros(self, movimientos):
        pass    
    def cargar_registros(self):
        pass
