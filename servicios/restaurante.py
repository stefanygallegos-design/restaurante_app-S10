from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:

    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []

    def registrar_producto(
        self,
        producto: Producto
    ) -> bool:

        if self.buscar_producto(producto.codigo):
            return False

        self._productos.append(producto)
        return True

    def buscar_producto(
        self,
        codigo: str
    ) -> Producto | None:

        for producto in self._productos:

            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nuevo_nombre: str,
        nueva_categoria: str,
        nuevo_precio: float
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        if not nuevo_nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not nueva_categoria.strip():
            raise ValueError(
                "La categoría no puede estar vacía."
            )

        if nuevo_precio < 0:
            raise ValueError(
                "El precio no puede ser negativo."
            )

        producto.nombre = nuevo_nombre.strip()
        producto.categoria = nueva_categoria.strip()
        producto.precio = nuevo_precio

        return True

    def eliminar_producto(
        self,
        codigo: str
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)

        return True

    def listar_productos(self) -> list[Producto]:
        return self._productos.copy()

    def registrar_usuario(
        self,
        usuario: Usuario
    ) -> bool:

        if self.buscar_usuario(usuario.identificacion):
            return False

        self._usuarios.append(usuario)

        return True

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:

        for usuario in self._usuarios:

            if usuario.identificacion == identificacion:
                return usuario

        return None

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    def obtener_categorias_unicas(self) -> set[str]:

        categorias = set()

        for producto in self._productos:
            categorias.add(producto.categoria)

        return categorias
