class Producto:
    def __init__(self, nombre, ingredientes, precio_publico):
        self.nombre = nombre
        self.ingredientes = ingredientes  # Lista de ingredientes (Base y Complemento)
        self.precio_publico = precio_publico

    def calcular_calorias(self):
        # Calcula el total de calorías del producto sumando las calorías de cada ingrediente.
        return sum(ingrediente.calorias for ingrediente in self.ingredientes)

    def calcular_costo(self):
        # Calcula el costo total del producto sumando los precios de los ingredientes.
        return sum(ingrediente.precio for ingrediente in self.ingredientes)

    def calcular_rentabilidad(self):
        # Calcula la rentabilidad del producto. Rentabilidad = precio de venta - costo total.
        costo_total = self.calcular_costo()
        return self.precio_publico - costo_total
