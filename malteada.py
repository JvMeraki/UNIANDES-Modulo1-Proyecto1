from calculadora import calcular_calorias, calcular_rentabilidad
from iproducto import IProducto


class Malteada(IProducto):
    def __init__(self, nombre, precio_publico, ingredientes, volumen):
        if len(ingredientes) != 3:
            raise ValueError(f"La Malteada {nombre} debe tener exactamente 3 ingredientes.")
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.ingredientes = ingredientes
        self.volumen = volumen

    @property
    def volumen(self):
        return self._volumen

    @volumen.setter
    def volumen(self, valor):
        self._volumen = valor

    def calcular_costo(self):
        costo_total = sum(ingrediente.precio for ingrediente in self.ingredientes) + 500
        return costo_total

    def calcular_rentabilidad(self):
        return calcular_rentabilidad(self.precio_publico, self.ingredientes)

    def calcular_calorias(self):
        return calcular_calorias(self.ingredientes, "Malteada")

    def __str__(self):
        return f"Malteada {self.nombre} - Precio: {self.precio_publico}, Calorías: {self.calcular_calorias()}, Rentabilidad: {self.calcular_rentabilidad()}, Volumen: {self.volumen} onzas"
