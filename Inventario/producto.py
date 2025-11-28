import csv
import os 
from datetime import datetime

class Producto:
    def __init__(self, codigo, nombre, tipo , precio, stock, fecha_ingreso=None):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__stock = stock
        self.__precio = precio
        self.__tipo = tipo
        self.__fecha_ingreso = fecha_ingreso or datetime.now()

    def get_codigo(self):
        return self.__codigo
    
    def get_nombre(self):
        return self.__nombre

    def get_stock(self):
        return self.__stock

    def get_precio(self):
        return self.__precio

    def get_tipo(self):
        return self.__tipo

    def get_fecha_ingreso(self):
        return self.__fecha_ingreso


    def set_codigo(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("El código debe ser una cadena no vacía")
        self.__codigo = valor

    def set_nombre(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre debe ser una cadena no vacía")
        self.__nombre = valor

    def set_stock(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("El stock debe ser un número entero no negativo")
        self.__stock = valor

    def set_precio(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El precio debe ser un número positivo")
        self.__precio = valor

    def set_tipo(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("El tipo debe ser una cadena no vacía")
        self.__tipo = valor

    def set_fecha_ingreso(self, valor):
        if not isinstance(valor, datetime):
            raise ValueError("La fecha de ingreso debe ser un objeto datetime")
        self.__fecha_ingreso = valor

    def to_dict(self):
        """Convierte el producto a diccionario para guardar en CSV"""
        return {
            'codigo': self.__codigo,
            'nombre': self.__nombre,
            'tipo': self.__tipo,
            'precio': self.__precio,
            'stock': self.__stock,
            'fecha_ingreso': self.__fecha_ingreso,
        }

    def __str__(self):
        return f"Producto: {self.__nombre} (Código: {self.__codigo}) - Tipo: {self.__tipo} - Precio: ${self.__precio:.2f} - Stock: {self.__stock} - Fecha: {self.__fecha_ingreso}"

    
class Inventario:
    def __init___(self, archivo_csv='productos.csv'):
        self.archivo_csv= archivo_csv 
        self.productos = []
        self.cargar_desde_csv()


    def cargar_desde_csv(self):
        """Carga los productos desde el archivo CSV"""
        if not os.path.exists(self.archivo_csv):
            # Si el archivo no existe, crea uno con headers
            with open(self.archivo_csv, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['codigo', 'nombre', 'tipo', 'precio', 'stock', 'fecha_ingreso'])
            return

        try:
            with open(self.archivo_csv, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        producto = Producto(
                            codigo=row['codigo'],
                            nombre=row['nombre'],
                            tipo=row['tipo'],
                            precio=float(row['precio']),
                            stock=int(row['stock']),
                            fecha_ingreso=row['fecha_ingreso']
                        )
                        self.productos.append(producto)
                    except (ValueError, KeyError) as e:
                        print(f"Error al cargar producto: {row}. Error: {e}")
        except Exception as e:
            print(f"Error al abrir el archivo CSV: {e}")
