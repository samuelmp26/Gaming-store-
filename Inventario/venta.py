
from typing import Dict
class EvaluacionProductoUsado:
    """Clase para evaluar productos usados que los clientes quieren vender"""
    
    CONDICIONES = {
        "excelente": 0.85,
        "bueno": 0.65,
        "medio": 0.45,
        "malo": 0.20
    }
    
    def __init__(self, producto_base: str, precio_original: float):
        self.producto_base = producto_base
        self.precio_original = precio_original
        self.condicion_fisica = ""
        self.funcionalidad = ""
        self.accesorios_completos = True
        self.precio_estimado = 0.0
    
    def evaluar(self, condicion_fisica: str, funcionalidad: str, accesorios: bool) -> Dict:
        self.condicion_fisica = condicion_fisica
        self.funcionalidad = funcionalidad
        self.accesorios_completos = accesorios
        
        # Calcular precio estimado basado en múltiples factores
        factor_condicion = self.CONDICIONES.get(condicion_fisica.lower(), 0.3)
        factor_funcionalidad = self.CONDICIONES.get(funcionalidad.lower(), 0.3)
        factor_accesorios = 1.0 if accesorios else 0.8
        
        # Promedio ponderado
        factor_total = (factor_condicion * 0.4 + factor_funcionalidad * 0.5 + 
                       (factor_accesorios - 0.8) * 0.5 + 0.8)
        
        self.precio_estimado = self.precio_original * factor_total
        
        return {
            "precio_estimado": self.precio_estimado,
            "condicion_general": self._determinar_condicion_general(factor_total)
        }
    
    def _determinar_condicion_general(self, factor: float) -> str:
        if factor >= 0.75:
            return "excelente"
        elif factor >= 0.55:
            return "bueno"
        elif factor >= 0.35:
            return "medio"
        else:
            return "malo"
    
    def recomendar_negocio(self, precio_ofrecido: float) -> Dict:
        """Analiza si conviene aceptar el negocio basado en el precio ofrecido"""
        porcentaje_precio = (precio_ofrecido / self.precio_estimado) * 100
        
        # Lógica de recomendación
        if precio_ofrecido <= self.precio_estimado * 1.1:
            probabilidad_aceptar = 90
            recomendacion = "ACEPTAR"
            razon = "El precio está dentro del rango esperado"
        elif precio_ofrecido <= self.precio_estimado * 1.3:
            probabilidad_aceptar = 60
            recomendacion = "CONSIDERAR"
            razon = "El precio es un poco alto pero negociable"
        elif precio_ofrecido <= self.precio_estimado * 1.5:
            probabilidad_aceptar = 30
            recomendacion = "DUDOSO"
            razon = "El precio es significativamente alto"
        else:
            probabilidad_aceptar = 10
            recomendacion = "RECHAZAR"
            razon = "El precio excede el valor del producto"
        
        return {
            "recomendacion": recomendacion,
            "probabilidad_aceptar": probabilidad_aceptar,
            "probabilidad_rechazar": 100 - probabilidad_aceptar,
            "razon": razon,
            "porcentaje_precio": porcentaje_precio
        }