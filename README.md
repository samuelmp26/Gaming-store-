# Pyrants T-Store

Este repo contiene hasta la fecha, el desarrollo de un proyecto que busca aplicar todos los conceptos de programacion orientada a objetos en python, que consta de una tienda de videojuegos y perifericos relacionados al gaming, todo esto presentado mediante código y aun mas importante una estructuración organizada de todo el sistema de clases que gestiona la tienda. 
#### Integrantes:
* Samuel Medina Pulido
* Miguel Angel Moreno 
* Sebastian Burtica Velasco 
## Objetivos
#### Objetivos general
* Aplicar de manera integral y didáctica todos los conceptos fundamentales de la Programación Orientada a Objetos (POO) utilizando Python.
#### Objetivos especificos 
* Diseñar e implementar un sistema de gestión para una tienda de videojuegos que permita registrar, consultar y administrar productos, clientes y ventas de forma eficiente.
* Crear una interfaz amigable para el operador que simplifique la aplicacion de el codigo, ya que se requiere para agilizar los procesos al momento de vender.
## Marco teórico 
Para dar contexto del proyecto es necesario abordar algunos conceptos importantes en POO. Para empezar ¿Cual es el enfoque de POO? Esta rama de la programacion utiliza objetos para modelar sistemas del mundo real , ademas almacena colecciones de objetos que interactuan entre si, el proposito de POO es la reusabilidad, la mantenibilidad y la escalabilidad del código, agrupando datos (atributos) y el comportamiento (métodos). A forma de resumen los 4 pilares de POO son los siguientes:
* Abstracción: Se trata de mostrar todo lo importante al usuario, ocultando el codigo base o todos los mecanismos que permiten la operacion del codigo abstraido.
* Encapsulamiento: Restringe el acceso a los datos que el programador decida , esto con el fin de conservar la privacidad y la integracion de los datos.
* Herencia: Permite que una clase hija herede los atributos y métodos de la clase madre , esto simplifica y reutiliza el codigo, ya que en la parte de programacion para datos que tienen este tipo de relación se ahorra la escritura de c´digo.
* Polimorfismo: Este concepto nos dice que un objeto puede tener muchas formas , es decir , dependiendo de quien lo invoca se comporta de manera diferente, con ello simplifica el entendimiento y la extension del codigo ya que se pueden tratar objetos de difrentes clases de manera uniforme.
## Justificacion
Más allá de enfocarse en la tienda de videojuegos y destinar todo el proposito a la creación como tal , el proyecto busca utilizar de forma muy aplicada todos los conceptos aprendidos de la programacion orientada a objetos de forma dinámica. Al estar buscando alternativas que cumplieran este propósito , hemos seleccionado deliberadamente el contexto del comercio electrónico de gaming porque sus características inherentes—la diversidad de productos (juegos, consolas, periféricos), la complejidad de las interacciones (clientes, carritos, pedidos) y la necesidad de clasificación detallada (géneros, plataformas, especificaciones)—ofrecen el escenario perfecto para aplicar de forma dinámica los 4 pilares de POO , tales como herencia, polimorfismo , abstraccion y encapsulamiento. 

## ¿ Como se aborda el problema?
Para abordar el "problema" o el diseño estructurado del codigo,se opta, primero pot crear un diagrama de clases que describe el sistema de relación entre clases. Para que el diagrama sea mas entendible se explica a continuación por partes. 
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
    class cliente{
       + str nombre 
       + str id 
       + str telefono 
       + str correo 
       + str fecha_de_registro
       + list() historial_de_compras

       + comprar()
       + vender()
    }

    Inventario "1" *-- "*" RegistroMovimiento : registra >
    Inventario --> Persistencia : usa >
    Inventario --> Negociante : usa >
    Reporte --> Inventario : obtiene datos de >
    CargaMasiva --> Inventario : importa productos a >
    InterfazConsola --> Inventario : manipula >
    RegistroMovimiento -- Negociante


````
Cabe resaltar que el diagrama de clases anterior corresponde a un planteamiento de resolución del proyecto , las clases serian las necesarias para el flujo del sistema,
* La clase principal es inventario (nucleo del sistema)  que gestiona los productos y los movimientos, y está rodeada de clases que manejan la persistencia, la interfaz, los reportes y la lógica de negocio.
*  La clase registro movimiento actúa como un objeto de datos (Data Object) que registra cada transacción (entrada o salida de stock). Almacena detalles cruciales como la cantidad, el precio unitario y la fecha.
*  La clase persistencia su única tarea es saber cómo guardar el estado actual del Inventario y sus Movimientos en almacenamiento permanente (disco duro) y luego cargarlos de vuelta.
*  La clase reporte necesita acceder a los datos del Inventario para crear resúmenes, y exportar esa información en formatos estructurados.
*  Carga Masiva encargada de procesar datos externos (como archivos CSV o JSON) e integrarlos al inventario.
*  La interfaz de consola permite la interacción entre el programa y el usuario de una forma comprenmsible e amigable.
* La clase negociante contiene la lógica económica del negocio. Determina los precios de compra y venta basándose en reglas (margen_ganancia, reglas_demanda)



Aqui se presenta la relación entre inventario y producto 

````mermaid
classDiagram
direction TB
class Producto {
	    - str codigo
	    - str nombre
	    - str categoria
	    - float precio
	    - int cantidad
	    - datetime fecha_ingreso
	    + actualizar_cantidad(cantidad)
	    + actualizar_precio(precio)
	    + to_dict()
	    + from_dict(data)
	    + __str__()
    }

    class JuegoDisco {
    }

    class JuegoCartucho {
    }

    class Consola {
    }

    class Control {
    }

    class AccesorioControl {
    }

    class Auricular {
    }

    class Microfono {
    }

    class Monitor {
    }

    class Cable {
    }

    class Manubrio {
    }

    class LentesVR {
    }

    class Mouse {
    }

    class Teclado {
    }

    class SillaGamer {
    }

    class TarjetaRegalo {
    }

    class Camara {
    }

    class BaseConsola {
    }

    class MemoriaExterna {
    }

    class LuzAmbiental {
    }

    class CapturadoraVideo {
    }



   Producto <|-- JuegoDisco
    Producto <|-- JuegoCartucho
    Producto <|-- Consola
    Producto <|-- Control
    Producto <|-- AccesorioControl
    Producto <|-- Auricular
    Producto <|-- Microfono
    Producto <|-- Monitor
    Producto <|-- Cable
    Producto <|-- Manubrio
    Producto <|-- LentesVR
    Producto <|-- Mouse
    Producto <|-- Teclado
    Producto <|-- SillaGamer
    Producto <|-- TarjetaRegalo
    Producto <|-- Camara
    Producto <|-- BaseConsola
    Producto <|-- MemoriaExterna
    Producto <|-- LuzAmbiental
    Producto <|-- CapturadoraVideo

````
Como se puede observar hay muchos tipos de productos , ya que cada producto tiene atributos distintos , pero que hereden de la clase madre que es producto, en su momoento se defeniran con atributos de instancia. 


Cabe resaltar que para codigo futuro mucho mas realizado , se plantea el manejo de una clase madre que maneje excepciones pata todo el código, estas excepciones son las sugeridas en general.
```mermaid
classDiagram
direction TB

    Excepciones <|-- ProductoNoEncontradoError
    Excepciones <|-- StockInsuficienteError
    Excepciones <|-- CodigoDuplicadoError
    Excepciones <|-- ArchivoInvalidoError


````



 
## Ejecucion del programa...


