from typing import Dict, List
from enum import Enum

class TipoProducto(Enum):
    """Categorías de productos"""
    VIDEOJUEGO = "videojuego"
    CONSOLA = "consola"
    CONTROL = "control"
    AURICULARES = "auriculares"
    TECLADO = "teclado"
    MOUSE = "mouse"
    MONITOR = "monitor"
    SILLA = "silla"
    ACCESORIO = "accesorio"
    OTRO = "otro"

class CondicionFisica(Enum):
    """Estados físicos del producto"""
    COMO_NUEVO = ("Como Nuevo", 0.95)
    EXCELENTE = ("Excelente", 0.85)
    BUENO = ("Bueno", 0.70)
    REGULAR = ("Regular", 0.50)
    MALO = ("Malo", 0.30)
    
    def __init__(self, descripcion, factor):
        self.descripcion = descripcion
        self.factor = factor

class CondicionFuncional(Enum):
    """Estados funcionales del producto"""
    PERFECTO = ("Funciona Perfectamente", 1.0)
    FUNCIONAL = ("Funcional con detalles menores", 0.85)
    PROBLEMAS_MENORES = ("Problemas menores", 0.60)
    PROBLEMAS_GRAVES = ("Problemas graves", 0.30)
    NO_FUNCIONA = ("No funciona", 0.05)
    
    def __init__(self, descripcion, factor):
        self.descripcion = descripcion
        self.factor = factor

class DepreciacionProducto:
    """Calcula depreciación simple por tiempo de uso"""
    
    # Porcentaje que pierde por año
    DEPRECIACION_ANUAL = {
        TipoProducto.VIDEOJUEGO: 0.35,      # Pierde 35% por año
        TipoProducto.CONSOLA: 0.20,          # Pierde 20% por año
        TipoProducto.CONTROL: 0.25,
        TipoProducto.AURICULARES: 0.30,
        TipoProducto.TECLADO: 0.20,
        TipoProducto.MOUSE: 0.25,
        TipoProducto.MONITOR: 0.15,
        TipoProducto.SILLA: 0.18,
        TipoProducto.ACCESORIO: 0.25,
        TipoProducto.OTRO: 0.25
    }
    
    @staticmethod
    def calcular(tipo: TipoProducto, meses_uso: int) -> float:
        """Retorna cuánto vale el producto según su antigüedad (0.0 a 1.0)"""
        años = meses_uso / 12
        tasa = DepreciacionProducto.DEPRECIACION_ANUAL.get(tipo, 0.25)
        
        # Mientras más viejo, menos vale
        valor = (1 - tasa) ** años
        return max(0.10, min(1.0, valor))  # Mínimo 10%, máximo 100%

class DefectosComunes:
    """Lista de defectos comunes y su impacto en el precio"""
    
    DEFECTOS = {
        # Defectos físicos
        "rasguños_leves": ("Rasguños leves", -0.05),
        "rasguños_profundos": ("Rasguños profundos", -0.15),
        "abolladuras": ("Abolladuras o golpes", -0.15),
        "decoloración": ("Decoloración o manchas", -0.10),
        "partes_rotas": ("Partes rotas o faltantes", -0.25),
        
        # Defectos funcionales (controles/periféricos)
        "botones_desgastados": ("Botones desgastados", -0.10),
        "joystick_drift": ("Joystick con drift", -0.20),
        "teclas_no_responden": ("Teclas que no responden", -0.20),
        "sensor_defectuoso": ("Sensor defectuoso", -0.25),
        
        # Defectos de pantallas
        "pantalla_rayada": ("Pantalla rayada", -0.15),
        "pixeles_muertos": ("Píxeles muertos", -0.20),
        "manchas_pantalla": ("Manchas en pantalla", -0.15),
        
        # Falta de accesorios
        "sin_caja": ("Sin caja original", -0.10),
        "sin_cables": ("Sin cables o adaptador", -0.15),
        "sin_manual": ("Sin manual", -0.03),
        "sin_accesorios": ("Sin accesorios originales", -0.15),
        
        # Otros problemas
        "olor_humo": ("Olor a humo/cigarro", -0.30),
        "batería_gastada": ("Batería degradada", -0.15),
        "ruidos_anormales": ("Ruidos o vibración anormal", -0.20),
        "sobrecalentamiento": ("Sobrecalentamiento", -0.25),
    }
    
    @staticmethod
    def seleccionar_defectos() -> List[tuple]:
        """Permite seleccionar defectos de forma interactiva"""
        print("\n" + "="*70)
        print("EVALUACIÓN DE DEFECTOS")
        print("="*70)
        print("\nRevise el producto y marque los defectos encontrados:")
        print("Responda 's' para SÍ o 'n' para NO\n")
        
        defectos_encontrados = []
        
        for clave, (descripcion, penalizacion) in DefectosComunes.DEFECTOS.items():
            respuesta = input(f"  ¿{descripcion}? (s/n): ").lower().strip()
            if respuesta == 's':
                defectos_encontrados.append((descripcion, penalizacion))
                print(f"    → Descuento: {abs(penalizacion)*100:.0f}%")
        
        return defectos_encontrados

class EvaluadorProducto:
    """Sistema principal de evaluación simplificado"""
    
    def __init__(self):
        self.producto_nombre = ""
        self.precio_nuevo = 0.0
        self.tipo_producto = None
        self.meses_uso = 0
        
        self.condicion_fisica = None
        self.condicion_funcional = None
        self.defectos = []
        
        self.precio_estimado = 0.0
        self.precio_minimo_compra = 0.0
        self.precio_maximo_compra = 0.0
    
    def iniciar_evaluacion(self):
        """Proceso completo de evaluación paso a paso"""
        print("\n" + "="*80)
        print("SISTEMA DE EVALUACIÓN DE PRODUCTOS USADOS".center(80))
        print("="*80)
        
        # 1. Información básica del producto
        self._obtener_info_basica()
        
        # 2. Evaluación de condición
        self._evaluar_condicion()
        
        # 3. Revisar defectos
        self._revisar_defectos()
        
        # 4. Calcular precio
        self._calcular_precios()
        
        # 5. Mostrar resumen
        self._mostrar_resumen()
        
        # 6. Negociar
        self._iniciar_negociacion()
    
    def _obtener_info_basica(self):
        """Solicita información básica del producto"""
        print("\n--- INFORMACIÓN DEL PRODUCTO ---")
        
        self.producto_nombre = input("Nombre del producto: ").strip()
        self.precio_nuevo = float(input("Precio cuando es nuevo ($): "))
        
        # Seleccionar tipo
        print("\nTipo de producto:")
        tipos = list(TipoProducto)
        for i, tipo in enumerate(tipos, 1):
            print(f"  {i}. {tipo.value.title()}")
        
        try:
            tipo_idx = int(input("\nSeleccione el tipo (número): ")) - 1
            self.tipo_producto = tipos[tipo_idx]
        except:
            print("⚠ Selección inválida, usando 'Otro'")
            self.tipo_producto = TipoProducto.OTRO
        
        self.meses_uso = int(input("¿Cuántos meses de uso tiene aproximadamente?: "))
    
    def _evaluar_condicion(self):
        """Evalúa la condición física y funcional"""
        print("\n--- EVALUACIÓN DE CONDICIÓN ---")
        
        # Condición física
        print("\nCondición FÍSICA:")
        for i, cond in enumerate(CondicionFisica, 1):
            print(f"  {i}. {cond.descripcion}")
        
        try:
            fisica_idx = int(input("\nSeleccione (número): ")) - 1
            self.condicion_fisica = list(CondicionFisica)[fisica_idx]
        except:
            self.condicion_fisica = CondicionFisica.BUENO
        
        # Condición funcional
        print("\nCondición FUNCIONAL:")
        for i, cond in enumerate(CondicionFuncional, 1):
            print(f"  {i}. {cond.descripcion}")
        
        try:
            funcional_idx = int(input("\nSeleccione (número): ")) - 1
            self.condicion_funcional = list(CondicionFuncional)[funcional_idx]
        except:
            self.condicion_funcional = CondicionFuncional.FUNCIONAL
    
    def _revisar_defectos(self):
        """Revisa defectos específicos del producto"""
        respuesta = input("\n¿Desea revisar defectos específicos? (s/n): ").lower()
        if respuesta == 's':
            self.defectos = DefectosComunes.seleccionar_defectos()
    
    def _calcular_precios(self):
        """Calcula el precio estimado y rango de compra"""
        # Factor de depreciación por tiempo
        factor_tiempo = DepreciacionProducto.calcular(self.tipo_producto, self.meses_uso)
        
        # Factores de condición
        factor_fisica = self.condicion_fisica.factor
        factor_funcional = self.condicion_funcional.factor
        
        # Descuentos por defectos
        descuento_defectos = sum(abs(d[1]) for d in self.defectos)
        
        # Precio estimado de mercado
        self.precio_estimado = (self.precio_nuevo * factor_tiempo * 
                               factor_fisica * factor_funcional * 
                               (1 - descuento_defectos))
        
        # Rango de compra (lo que pagaríamos nosotros)
        # Compramos entre 40% y 60% del valor estimado de mercado
        self.precio_minimo_compra = self.precio_estimado * 0.40
        self.precio_maximo_compra = self.precio_estimado * 0.60
    
    def _mostrar_resumen(self):
        """Muestra resumen completo de la evaluación"""
        print("\n" + "="*80)
        print("RESUMEN DE EVALUACIÓN".center(80))
        print("="*80)
        
        print(f"\n Producto: {self.producto_nombre}")
        print(f" Precio nuevo: ${self.precio_nuevo:.2f}")
        print(f" Tiempo de uso: {self.meses_uso} meses ({self.meses_uso//12} años)")
        
        print(f"\n CONDICIÓN:")
        print(f"  • Física: {self.condicion_fisica.descripcion}")
        print(f"  • Funcional: {self.condicion_funcional.descripcion}")
        
        if self.defectos:
            print(f"\n⚠ DEFECTOS ENCONTRADOS:")
            for descripcion, penalizacion in self.defectos:
                print(f"  • {descripcion}: -{abs(penalizacion)*100:.0f}%")
        else:
            print(f"\n✓ Sin defectos adicionales detectados")
        
        print(f"\n" + "-"*80)
        print(f" VALOR ESTIMADO DE MERCADO: ${self.precio_estimado:.2f}")
        print(f"-"*80)
        
        print(f"\n RANGO DE COMPRA RECOMENDADO:")
        print(f"  • Mínimo a ofrecer: ${self.precio_minimo_compra:.2f}")
        print(f"  • Máximo a pagar:   ${self.precio_maximo_compra:.2f}")
        print(f"\n Intenta comprar lo más cerca del mínimo posible")
        print("="*80)
    
    def _iniciar_negociacion(self):
        """Proceso de negociación con el cliente"""
        print("\n" + "="*80)
        print("NEGOCIACIÓN".center(80))
        print("="*80)
        
        # Precio que pide el cliente
        precio_cliente = float(input("\n¿Cuánto pide el cliente por el producto? $"))
        
        # Analizar la oferta
        print(f"\n--- ANÁLISIS DE LA OFERTA ---")
        
        if precio_cliente <= self.precio_minimo_compra:
            print(" EXCELENTE OFERTA - Acepta inmediatamente!")
            print(f"   El cliente pide ${precio_cliente:.2f}, está por debajo de nuestro mínimo.")
            decision = "ACEPTAR"
            
        elif precio_cliente <= self.precio_maximo_compra:
            print(" BUENA OFERTA - Es aceptable")
            print(f"   El cliente pide ${precio_cliente:.2f}, está dentro de nuestro rango.")
            porcentaje = ((precio_cliente - self.precio_minimo_compra) / 
                         (self.precio_maximo_compra - self.precio_minimo_compra)) * 100
            print(f"   Está al {porcentaje:.0f}% de nuestro rango de compra.")
            decision = "ACEPTAR"
            
        elif precio_cliente <= self.precio_estimado:
            print(" OFERTA ALTA - Intenta negociar")
            print(f"   El cliente pide ${precio_cliente:.2f}, está por encima de nuestro máximo.")
            diferencia = precio_cliente - self.precio_maximo_compra
            print(f"   Diferencia: ${diferencia:.2f}")
            print(f"\n Contraoferta sugerida: ${self.precio_maximo_compra:.2f}")
            decision = "NEGOCIAR"
            
        else:
            print(" OFERTA MUY ALTA - No conviene")
            print(f"   El cliente pide ${precio_cliente:.2f}, está muy por encima del valor de mercado.")
            diferencia = precio_cliente - self.precio_estimado
            print(f"   Está ${diferencia:.2f} por encima del valor estimado.")
            print(f"\n Si insistes, no ofrezcas más de: ${self.precio_maximo_compra:.2f}")
            decision = "RECHAZAR"
        
        # Simulación de negociación
        if decision == "NEGOCIAR":
            print(f"\n--- SIMULACIÓN DE NEGOCIACIÓN ---")
            oferta_nuestra = self.precio_minimo_compra
            
            print(f"\nRonda 1: Ofrecemos ${oferta_nuestra:.2f}")
            print(f"         Cliente pide ${precio_cliente:.2f}")
            
            # Punto medio
            punto_medio = (oferta_nuestra + precio_cliente) / 2
            print(f"\nRonda 2: Contraofrecemos ${punto_medio:.2f} (punto medio)")
            
            if punto_medio <= self.precio_maximo_compra:
                print(f" Este precio (${punto_medio:.2f}) aún nos conviene")
            else:
                print(f" No subas más de ${self.precio_maximo_compra:.2f}")
        
        # Decisión final
        print(f"\n" + "="*80)
        print("DECISIÓN FINAL")
        print("="*80)
        
        decision_final = input("\n¿Cerraste el trato? (s/n): ").lower()
        
        if decision_final == 's':
            precio_final = float(input("¿A qué precio compraste? $"))
            
            # Calcular ganancia potencial
            ganancia = self.precio_estimado - precio_final
            porcentaje_ganancia = (ganancia / precio_final) * 100 if precio_final > 0 else 0
            
            print(f"\n ¡TRATO CERRADO!")
            print(f"  Precio de compra: ${precio_final:.2f}")
            print(f"  Precio de venta estimado: ${self.precio_estimado:.2f}")
            print(f"  Ganancia esperada: ${ganancia:.2f} ({porcentaje_ganancia:.1f}%)")
            
            if precio_final <= self.precio_maximo_compra:
                print(f"\n ¡Excelente negociación!")
            else:
                print(f"\n Pagaste un poco más de lo recomendado, pero puede funcionar.")
        else:
            print("\n Trato rechazado - Fue la decisión correcta si el precio era muy alto.")


# Función principal para integrar con el sistema
def evaluar_producto_usado():
    """Función principal que se llama desde el menú del sistema"""
    evaluador = EvaluadorProducto()
    evaluador.iniciar_evaluacion()