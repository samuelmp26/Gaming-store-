# Pyrants T-Store

Este repo contiene hasta la fecha, el desarrollo de un proyecto que busca aplicar todos los conceptos de programacion orientada a objetos en python, que consta de una tienda de videojuegos y perifericos relacionados al gaming, todo esto presentado mediante código y aun mas importante una estructuración organizada de todo el sistema de clases que gestiona la tienda. 
## Objetivos
#### Objetivos general
* Aplicar de manera integral y didáctica todos los conceptos fundamentales de la Programación Orientada a Objetos (POO) utilizando Python.
#### Objetivos especificos 
* Diseñar e implementar un sistema de gestión para una tienda de videojuegos que permita registrar, consultar y administrar productos, clientes y ventas de forma eficiente.
* Crear una interfaz amigable para el usuario que simplifique la aplicacion de el codigo.
## Justificacion
Más allá de enfocarse en la tienda de videojuegos y destinar todo el proposito a la creación como tal , el proyecto busca utilizar de forma muy aplicada todos los conceptos aprendidos de la programacion orientada a objetos de forma dinámica. Al estar buscando alternativas que cumplieran este propósito , hemos seleccionado deliberadamente el contexto del comercio electrónico de gaming porque sus características inherentes—la diversidad de productos (juegos, consolas, periféricos), la complejidad de las interacciones (clientes, carritos, pedidos) y la necesidad de clasificación detallada (géneros, plataformas, especificaciones)—ofrecen el escenario perfecto para aplicar de forma dinámica los 4 pilares de POO , tales como herencia, polimorfismo , abstraccion y encapsulamiento. 
## ¿ Como se aborda el problema?
Para abordar el "problema" o el diseño estructurado del codigo,se opta por primero crear un diagrama de clases que describe el sistema de relación entre clases, para que el diagrama sea mas entendible se explica por partes. 
 ````mermaid
classDiagram
direction TB
 class Inventario {
	    - dict~str, Producto~ productos
	    - list~RegistroMovimiento~ movimientos
	    + agregar_producto(producto)
	    + registrar_entrada(codigo, cantidad)
	    + registrar_salida(codigo, cantidad)
	    + listar_inventario()
	    + buscar_producto(codigo)
	    + valor_total()
	    + guardar_datos()
	    + cargar_datos()
    }
 class RegistroMovimiento {
	    - str id_movimiento
	    - str tipo
	    - str codigo_producto
	    - int cantidad
	    - float precio_unitario
	    - datetime fecha
	    + to_dict()
	    + __str__()
    }
 class Persistencia {
	    - str ruta_inventario
	    - str ruta_movimientos
	    + guardar_inventario(inventario)
	    + cargar_inventario()
	    + guardar_registros(registros)
	    + cargar_registros()
    }
 class Reporte {
	    - Inventario inventario
	    - datetime fecha_generacion
	    + generar_txt(ruta)
	    + generar_csv(ruta)
	    + generar_resumen()
    }

 class CargaMasiva {
	    - str ruta_archivo
	    + importar_csv(inventario)
	    + importar_json(inventario)
    }

 class InterfazConsola {
	    - Inventario inventario
	    + mostrar_menu()
	    + ejecutar_opcion(opcion)
 }
 class Negociante {
	    - float margen_ganancia
	    - dict reglas_demanda
	    + ofrecer_precio_compra(producto)
	    + ofrecer_precio_venta(producto)
	    + simular_negociacion(producto, tipo)
    }

    Inventario "1" *-- "*" RegistroMovimiento : registra >
    Inventario --> Persistencia : usa >
    Inventario --> Negociante : usa >
    Reporte --> Inventario : obtiene datos de >
    CargaMasiva --> Inventario : importa productos a >
    InterfazConsola --> Inventario : manipula >
    RegistroMovimiento -- Negociante









```` 
## Como ejecutar el programa?


