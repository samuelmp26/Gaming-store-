from datetime import datetime

class Reporte:
    def __init__(self, inventario):
        self.inventario = inventario
        self.fecha_generacion = datetime.now()

    def generar_txt(self, ruta):
        pass

    def generar_csv(self, ruta):
        pass

    def generar_resumen(self):
        print("\n=== RESUMEN DEL INVENTARIO ===")
        total_productos = len(self.inventario.productos)
        total_unidades = sum(p.cantidad for p in self.inventario.productos.values())
        valor_total = sum(p.precio * p.cantidad for p in self.inventario.productos.values())

        print(f"Fecha de generación: {self.fecha_generacion.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Productos registrados: {total_productos}")
        print(f"Unidades totales: {total_unidades}")
        print(f"Valor total estimado del inventario: ${valor_total:,.2f}")
        print("=================================")
