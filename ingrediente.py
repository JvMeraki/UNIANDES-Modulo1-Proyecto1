from abc import ABC, abstractmethod


class Ingrediente(ABC):
    def __init__(self, nombre: str, precio: float, calorias: int, inventario, es_vegetariano):
        self._nombre = nombre
        self._precio = precio
        self._calorias = calorias
        self._inventario = inventario
        self._es_vegetariano = es_vegetariano

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = valor

    @property
    def calorias(self):
        return self._calorias

    @calorias.setter
    def calorias(self, valor):
        self._calorias = valor

    @property
    def inventario(self):
        return self._inventario

    @inventario.setter
    def inventario(self, valor):
        self._inventario = valor

    @property
    def es_vegetariano(self):
        return self._es_vegetariano

    @es_vegetariano.setter
    def es_vegetariano(self, valor):
        self._es_vegetariano = valor

    def es_sano(self):
        # Verifica si el ingrediente es sano según las reglas: menos de 100 calorías o es vegetariano.
        return (self.calorias, self.es_vegetariano)

    @abstractmethod
    def abastecer(self, cantidad):
        pass
