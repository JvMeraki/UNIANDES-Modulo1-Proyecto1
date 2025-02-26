from calculadora import calcular_calorias, calcular_rentabilidad
from iproducto import IProducto


class Copa(IProducto):
    def __init__(self, nombre, precio_publico, ingredientes, tipo_vaso):
        if len(ingredientes) != 3:
            raise ValueError(f"La Copa {nombre} debe tener exactamente 3 ingredientes.")
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.ingredientes = ingredientes
        self.tipo_vaso = tipo_vaso

    @property
    def tipo_vaso(self):
        return self._tipo_vaso

    @tipo_vaso.setter
    def tipo_vaso(self, valor):
        self._tipo_vaso = valor

    def calcular_costo(self):
        costo_total = sum(ingrediente.precio for ingrediente in self.ingredientes)
        return costo_total

    def calcular_rentabilidad(self):
        return calcular_rentabilidad(self.precio_publico, self.ingredientes)

    def calcular_calorias(self):
        return calcular_calorias(self.ingredientes, "Copa")

    def __str__(self):
        return f"Copa {self.nombre} - Precio: {self.precio_publico}, Calorías: {self.calcular_calorias()}, Rentabilidad: {self.calcular_rentabilidad()}, Tipo de vaso: {self.tipo_vaso}"
