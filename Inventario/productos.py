class Producto:
    """Clase base para todos los productos"""
    def __init__(self, id_producto: str, nombre: str, categoria: str, precio: float, stock: int):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
    
    def __str__(self):
        return f"{self.id_producto} | {self.nombre} | ${self.precio:.2f} | Stock: {self.stock}"

class Videojuego(Producto):
    """Clase específica para videojuegos"""
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, 
                 plataforma: str, genero: str, año: int):
        super().__init__(id_producto, nombre, "Videojuego", precio, stock)
        self.plataforma = plataforma
        self.genero = genero
        self.año = año
    
    def __str__(self):
        return f"{super().__str__()} | {self.plataforma} | {self.genero} | {self.año}"

class ProductoGaming(Producto):
    """Clase para productos gaming (accesorios, hardware, etc.)"""
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, 
                 tipo: str, marca: str):
        super().__init__(id_producto, nombre, "Gaming", precio, stock)
        self.tipo = tipo
        self.marca = marca
    
    def __str__(self):
        return f"{super().__str__()} | {self.tipo} | {self.marca}"