# restaurante_app - Semana 10

## Datos del estudiante

**Nombre completo:** Stefany Gallegos Zari

**Asignatura:** Programación Orientada a Objetos

**Semana:** 10

## Descripción del proyecto

El proyecto `restaurante_app` corresponde a una evolución del sistema desarrollado durante las semanas anteriores de la asignatura Programación Orientada a Objetos.

En esta Semana 10 se incorporan el manejo de archivos, el control de excepciones y la persistencia de productos mediante un archivo JSON.

El sistema permite administrar productos y usuarios de un restaurante mediante un menú de consola. Los productos pueden registrarse, buscarse, actualizarse, eliminarse y listarse.

La principal mejora de esta semana consiste en conservar los productos registrados aunque el programa se cierre. Para ello, la información se almacena en el archivo `datos/productos.json` y posteriormente se recupera cuando la aplicación vuelve a ejecutarse.

Durante la ejecución, el programa continúa trabajando con objetos de la clase `Producto`. El archivo JSON solamente se utiliza como medio de persistencia.

## Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   └── productos.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── main.py
│
└── README.md
