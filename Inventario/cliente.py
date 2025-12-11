class Cliente:
    """Clase para gestionar clientes"""
    def __init__(self, id_cliente: str, nombre: str, email: str, telefono: str):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.historial_compras = []


    def __str__(self):
        return f"ID: {self.id_cliente} | {self.nombre} | {self.email} | {self.telefono}"