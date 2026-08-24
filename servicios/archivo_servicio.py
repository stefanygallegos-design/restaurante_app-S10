import json
from pathlib import Path

from modelos.producto import Producto


class ArchivoServicio:

    def __init__(self, ruta_productos: str) -> None:
        self._ruta_productos = Path(ruta_productos)

    def cargar_productos(self) -> list[Producto]:

        try:
            with open(
                self._ruta_productos,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

        except FileNotFoundError:
            print(
                "El archivo productos.json no existe. "
                "Se iniciará con una colección vacía."
            )
            return []

        except json.JSONDecodeError:
            print(
                "El archivo productos.json "
                "no contiene un JSON válido."
            )
            return []

        except PermissionError:
            print(
                "No existen permisos suficientes "
                "para leer productos.json."
            )
            return []

        if not isinstance(datos, list):
            print(
                "El archivo debe contener "
                "una lista de productos."
            )
            return []

        productos = []

        for item in datos:

            if not isinstance(item, dict):
                print(
                    "Se encontró un registro inválido "
                    "y fue omitido."
                )
                continue

            try:
                producto = Producto(
                    item["codigo"],
                    item["nombre"],
                    item["categoria"],
                    float(item["precio"])
                )

                productos.append(producto)

            except KeyError:
                print(
                    "Se encontró un producto incompleto "
                    "y fue omitido."
                )

            except (ValueError, TypeError) as error:
                print(
                    f"Se encontró un producto inválido: {error}"
                )

        return productos

    def guardar_productos(
        self,
        productos: list[Producto]
    ) -> bool:

        datos = []

        for producto in productos:
            datos.append(
                producto.convertir_a_diccionario()
            )

        try:

            self._ruta_productos.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            with open(
                self._ruta_productos,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

            return True

        except PermissionError:
            print(
                "No existen permisos suficientes "
                "para guardar productos.json."
            )
            return False
