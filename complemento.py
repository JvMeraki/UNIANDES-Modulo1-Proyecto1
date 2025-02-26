from ingrediente import Ingrediente


class Complemento(Ingrediente):
    def __init__(self, nombre, precio, calorias, inventario, es_vegetariano):
        super().__init__(nombre, precio, calorias, inventario, es_vegetariano)

    def abastecer(self):
        # Abastecer un complemento, aumentando el inventario en 10 unidades por cada abastecimiento.
        self._inventario += 10

    def renovar_inventario(self):
        # Renueva el inventario del complemento, poniendo el inventario en 10 unidades.
        self._inventario = 0

    def __str__(self):
        return f"Complemento {self.nombre} - Precio: {self.precio}, Calorías: {self.calorias}, Inventario: {self.inventario}, Vegetariano: {self.es_vegetariano}"
