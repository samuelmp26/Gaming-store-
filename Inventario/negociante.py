class Negociante:
    def _init_(self, margen_ganancia=0.2):
        self.margen_ganancia = margen_ganancia
        self.reglas_demanda = {}

    def ofrecer_precio_compra(self, producto):
        pass

    def ofrecer_precio_venta(self, producto):
        pass

    def simular_negociacion(self, producto, tipo="venta"):
        pass
