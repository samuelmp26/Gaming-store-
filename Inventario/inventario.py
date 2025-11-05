from .producto import Producto
from .movimiento import RegistroMovimiento
from .excepciones import ProductoNoEncontradoError, CodigoDuplicadoError

class Inventario:
    def __init__(self):
        self.productos = {}
        self.movimientos = []

    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            raise CodigoDuplicadoError(f"Ya existe el código {producto.codigo}")
        self.productos[producto.codigo] = producto
        print(f"Producto '{producto.nombre}' agregado correctamente.")

    def registrar_entrada(self, codigo, cantidad):
        if codigo not in self.productos:
            raise ProductoNoEncontradoError(f"Producto con código '{codigo}' no encontrado.")
        producto = self.productos[codigo]
        producto.actualizar_cantidad(cantidad)
        mov = RegistroMovimiento(
            f"MOV{len(self.movimientos)+1:04}",
            "entrada",
            codigo,
            cantidad,
            producto.precio
        )
        self.movimientos.append(mov)
        print(f"Entrada registrada: +{cantidad} unidades de '{producto.nombre}'.")

    def registrar_salida(self, codigo, cantidad):
        if codigo not in self.productos:
            raise ProductoNoEncontradoError(f"Producto con código '{codigo}' no encontrado.")
        producto = self.productos[codigo]
        if producto.cantidad < cantidad:
            raise Exception("Stock insuficiente para realizar la salida.")
        producto.actualizar_cantidad(-cantidad)
        mov = RegistroMovimiento(
            f"MOV{len(self.movimientos)+1:04}",
            "salida",
            codigo,
            cantidad,
            producto.precio
        )
        self.movimientos.append(mov)
        print(f"Salida registrada: -{cantidad} unidades de '{producto.nombre}'.")

    def listar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n=== Inventario actual ===")
            for p in self.productos.values():
                print(p)

    def guardar_datos(self):
        pass

    def cargar_datos(self):
        pass
