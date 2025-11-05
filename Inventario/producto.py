from datetime import datetime

class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad, fecha_ingreso=None):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        self.fecha_ingreso = fecha_ingreso or datetime.now()

    def actualizar_cantidad(self, cantidad):
        self.cantidad += cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "fecha_ingreso": self.fecha_ingreso.isoformat()
        }

    def from_dict(self, data):
        self.codigo = data["codigo"]
        self.nombre = data["nombre"]
        self.categoria = data["categoria"]
        self.precio = data["precio"]
        self.cantidad = data["cantidad"]
        self.fecha_ingreso = datetime.fromisoformat(data["fecha_ingreso"])
        return self

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - ${self.precio:.2f} ({self.cantidad} uds)"
