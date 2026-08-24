from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:

    print("\n" + "=" * 45)
    print("       SISTEMA DE RESTAURANTE")
    print("=" * 45)
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("8. Mostrar categorías")
    print("9. Salir")
    print("=" * 45)


def leer_precio() -> float:

    while True:

        try:

            precio = float(
                input("Precio: ")
            )

            if precio < 0:
                print(
                    "El precio no puede ser negativo."
                )
                continue

            return precio

        except ValueError:

            print(
                "Ingrese un precio válido."
            )


def guardar_productos(
    archivo_servicio: ArchivoServicio,
    restaurante: Restaurante
) -> None:

    guardado = archivo_servicio.guardar_productos(
        restaurante.listar_productos()
    )

    if guardado:
        print(
            "Productos guardados correctamente."
        )
    else:
        print(
            "Los cambios no pudieron guardarse."
        )


def registrar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    precio = leer_precio()

    try:

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        registrado = restaurante.registrar_producto(
            producto
        )

        if registrado:

            print(
                "Producto registrado correctamente."
            )

            guardar_productos(
                archivo_servicio,
                restaurante
            )

        else:

            print(
                "Ya existe un producto con ese código."
            )

    except ValueError as error:

        print(f"Error: {error}")


def buscar_producto(
    restaurante: Restaurante
) -> None:

    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input(
        "Código del producto: "
    ).strip()

    producto = restaurante.buscar_producto(
        codigo
    )

    if producto is None:

        print(
            "Producto no encontrado."
        )

    else:

        print("\nProducto encontrado:")
        print(producto)


def actualizar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n--- ACTUALIZAR PRODUCTO ---")

    codigo = input(
        "Código del producto: "
    ).strip()

    producto = restaurante.buscar_producto(
        codigo
    )

    if producto is None:

        print(
            "Producto no encontrado."
        )
        return

    nombre = input(
        "Nuevo nombre: "
    ).strip()

    categoria = input(
        "Nueva categoría: "
    ).strip()

    precio = leer_precio()

    try:

        actualizado = restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        if actualizado:

            print(
                "Producto actualizado correctamente."
            )

            guardar_productos(
                archivo_servicio,
                restaurante
            )

    except ValueError as error:

        print(f"Error: {error}")


def eliminar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input(
        "Código del producto: "
    ).strip()

    eliminado = restaurante.eliminar_producto(
        codigo
    )

    if eliminado:

        print(
            "Producto eliminado correctamente."
        )

        guardar_productos(
            archivo_servicio,
            restaurante
        )

    else:

        print(
            "Producto no encontrado."
        )


def listar_productos(
    restaurante: Restaurante
) -> None:

    print("\n--- PRODUCTOS ---")

    productos = restaurante.listar_productos()

    if not productos:

        print(
            "No existen productos registrados."
        )
        return

    for producto in productos:
        print(producto)


def registrar_usuario(
    restaurante: Restaurante
) -> None:

    print("\n--- REGISTRAR USUARIO ---")

    identificacion = input(
        "Identificación: "
    ).strip()

    nombre = input(
        "Nombre: "
    ).strip()

    correo = input(
        "Correo: "
    ).strip()

    try:

        usuario = Usuario(
            identificacion,
            nombre,
            correo
        )

        registrado = restaurante.registrar_usuario(
            usuario
        )

        if registrado:

            print(
                "Usuario registrado correctamente."
            )

        else:

            print(
                "Ya existe ese usuario."
            )

    except ValueError as error:

        print(f"Error: {error}")


def listar_usuarios(
    restaurante: Restaurante
) -> None:

    print("\n--- USUARIOS ---")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:

        print(
            "No existen usuarios registrados."
        )
        return

    for usuario in usuarios:
        print(usuario)


def mostrar_categorias(
    restaurante: Restaurante
) -> None:

    print("\n--- CATEGORÍAS ---")

    categorias = restaurante.obtener_categorias_unicas()

    if not categorias:

        print(
            "No existen categorías."
        )
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


def ejecutar() -> None:

    ruta_productos = (
        Path(__file__).resolve().parent
        / "datos"
        / "productos.json"
    )

    archivo_servicio = ArchivoServicio(
        str(ruta_productos)
    )

    # Cargar productos guardados.
    productos = (
        archivo_servicio.cargar_productos()
    )

    restaurante = Restaurante()

    # Reconstruir la colección de objetos Producto.
    for producto in productos:

        restaurante.registrar_producto(
            producto
        )

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        if opcion == "1":

            registrar_producto(
                restaurante,
                archivo_servicio
            )

        elif opcion == "2":

            buscar_producto(
                restaurante
            )

        elif opcion == "3":

            actualizar_producto(
                restaurante,
                archivo_servicio
            )

        elif opcion == "4":

            eliminar_producto(
                restaurante,
                archivo_servicio
            )

        elif opcion == "5":

            listar_productos(
                restaurante
            )

        elif opcion == "6":

            registrar_usuario(
                restaurante
            )

        elif opcion == "7":

            listar_usuarios(
                restaurante
            )

        elif opcion == "8":

            mostrar_categorias(
                restaurante
            )

        elif opcion == "9":

            print(
                "Gracias por utilizar el sistema."
            )
            break

        else:

            print(
                "Opción inválida."
            )


if __name__ == "__main__":
    ejecutar()
