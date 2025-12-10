from datetime import datetime
from typing import List, Dict
import Inventario.cliente as cliente
import Inventario.productos as producto
class ItemFactura:
    """Clase para items individuales en una factura"""
    def __init__(self, producto: producto.Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = producto.precio * cantidad
    
    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad} - ${self.subtotal:.2f}"

class Factura:
    """Clase para gestionar facturas"""
    def __init__(self, id_factura: str, cliente: cliente.Cliente):
        self.id_factura = id_factura
        self.cliente = cliente
        self.items: List[ItemFactura] = []
        self.fecha = datetime.now()
        self.total = 0.0
    
    def agregar_item(self, producto: producto.Producto, cantidad: int):
        if producto.stock >= cantidad:
            item = ItemFactura(producto, cantidad)
            self.items.append(item)
            producto.stock -= cantidad
            self.calcular_total()
            return True
        return False
    
    def calcular_total(self):
        self.total = sum(item.subtotal for item in self.items)
    
    def generar_resumen(self) -> str:
        resumen = f"\n{'='*60}\n"
        resumen += f"FACTURA #{self.id_factura}\n"
        resumen += f"Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}\n"
        resumen += f"Cliente: {self.cliente.nombre}\n"
        resumen += f"{'='*60}\n\n"
        
        for item in self.items:
            resumen += f"{item}\n"
        
        resumen += f"\n{'='*60}\n"
        resumen += f"TOTAL: ${self.total:.2f}\n"
        resumen += f"{'='*60}\n"
        return resumen