from datetime import datetime

class RegistroMovimiento:
    def _init_(self, id_movimiento, tipo, codigo_producto, cantidad, precio_unitario, fecha=None):
        self.id_movimiento = id_movimiento
        self.tipo = tipo
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.fecha = fecha or datetime.now()

    def to_dict(self):
        return {
            "id_movimiento": self.id_movimiento,
            "tipo": self.tipo,
            "codigo_producto": self.codigo_producto,
            "cantidad": self.cantidad,
            "precio_unitario": self.precio_unitario,
            "fecha": self.fecha.isoformat()
        }

    def _str_(self):
        return f"{self.id_movimiento}: {self.tipo.upper()} {self.cantidad} uds de {self.codigo_producto} el {self.fecha.strftime('%Y-%m-%d %H:%M')}"
