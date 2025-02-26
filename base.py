from ingrediente import Ingrediente


class Base(Ingrediente):
    def __init__(self, nombre, precio, calorias, inventario, es_vegetariano, sabor):
        super().__init__(nombre, precio, calorias, inventario, es_vegetariano)
        self._sabor = sabor

    def abastecer(self):
        # Abastecer una base, aumentando el inventario en 5 unidades por cada abastecimiento.
        self._inventario += 5

    def __str__(self):
        return f"Base {self.nombre} ({self.sabor}) - Precio: {self.precio}, Calorías: {self.calorias}, Inventario: {self.inventario}, Vegetariano: {self.es_vegetariano}"

    @property
    def sabor(self):
        return self._sabor

    @sabor.setter
    def sabor(self, valor):
        self._sabor = valor