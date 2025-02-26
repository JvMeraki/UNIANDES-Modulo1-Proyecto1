from base import Base
from complemento import Complemento
from copa import Copa
from funciones import calcular_calorias, calcular_rentabilidad, es_sano
from malteada import Malteada


class Heladeria:
    def __init__(self):
        self.productos = {} # Diccionario para productos, donde la clave es el nombre
        self.ventas = 0

    def añadir_producto(self, producto):
        # Añade un producto a la heladería solo si tiene 3 ingredientes
        if len(producto.ingredientes) != 3:
            print(f"El producto {producto.nombre} debe tener exactamente 3 ingredientes")
            return False
        
        # Añadir el producto al inventario de la heladeria
        if len(self.productos) < 4:
            self.productos[producto.nombre] = producto
            print(f"Producto {producto.nombre} añadido con éxito.")
            return True
        else:
            print(f"La heladería ya tiene el máximo de 4 productos.")
            return False

    def vender(self, nombre_producto):
        # Vende un producto, si es posible según el inventario.
        if nombre_producto not in self.productos:
            print(f"El producto {nombre_producto} no está disponible.")
            return False
        
        producto = self.productos[nombre_producto]
        
        # Verificar si hay suficiente inventario de los ingredientes
        for ingrediente in producto.ingredientes:
            # Verificar la cantidad necesaria para bases (0.2 unidades por porción) y complementos (1 unidad por porción)
            cantidad_requerida = 0.2 if isinstance(ingrediente, Base) else 1
            if ingrediente.inventario < cantidad_requerida:
                print(f"No hay suficientes {ingrediente.nombre} para vender {producto.nombre}")
                return False
        
        # Reducir inventario de los ingredientes después de la venta
        for ingrediente in producto.ingredientes:
            cantidad_requerida = 0.2 if isinstance(ingrediente, Base) else 1
            ingrediente.inventario -= cantidad_requerida
        
        # Verificar si el producto es sano
        sano = True
        for ingrediente in producto.ingredientes:
            if not es_sano(ingrediente.calorias, ingrediente.es_vegetariano):
                sano = False
                break
        
        # Calcular calorias y rentabilidad
        calorias = calcular_calorias(producto.ingredientes, "Copa" if isinstance(producto, Copa) else "Malteada")
        rentabilidad = calcular_rentabilidad(producto.precio_publico, producto.ingredientes)
        
        # Registrar la venta
        self.ventas += producto.precio_publico
        print(f"Producto {nombre_producto} vendido por {producto.precio_publico} pesos.")
        print(f"Calorías: {calorias}, Rentabilidad: {rentabilidad}, ¿Es sano?: {'Sí' if sano else 'No'}")
        return True
    
    def producto_mas_rentable(self):
        if not self.productos:
            return None  # Si no hay productos, devolver None
        
        # Encontrar el producto más rentable
        producto_rentable = max(self.productos.values(), key=lambda p: p.calcular_rentabilidad())
        return producto_rentable

    def __str__(self):
        productos_str = "\n".join([str(p) for p in self.productos.values()])
        return f"Productos disponibles:\n{productos_str}\nVentas del día: {self.ventas}"
