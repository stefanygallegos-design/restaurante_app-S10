class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> None:

        codigo = codigo.strip()
        nombre = nombre.strip()
        categoria = categoria.strip()

        if not codigo:
            raise ValueError("El código no puede estar vacío.")

        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")

        if not categoria:
            raise ValueError("La categoría no puede estar vacía.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def convertir_a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }

    def __str__(self) -> str:
        return (
            f"{self.codigo} | "
            f"{self.nombre} | "
            f"{self.categoria} | "
            f"${self.precio:.2f}"
        )
