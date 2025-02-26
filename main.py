import copa as cp
from base import Base
from complemento import Complemento
from funciones import es_sano
from heladeria import Heladeria
from malteada import Malteada

# Crear ingredientes
ingrediente1 = Base("Helado de Fresa", 50, 200, 10, True, "Fresa")
ingrediente2 = Base("Helado de Vainilla", 45, 150, 15, True, "Vainilla")
ingrediente3 = Complemento("Chocolate en trozos", 30, 100, 5, False)

# Crear una copa
copa1 = cp.Copa("Copa Fresa-Vainilla", 5000, [ingrediente1, ingrediente2, ingrediente3], "Vaso de cartón")


# Crear una malteada
malteada1 = Malteada("Malteada Vainilla", 6000, [ingrediente2, ingrediente3, ingrediente1], 250)

# Crear una heladería
heladeria = Heladeria()

# Probar añadir productos
print("Añadiendo productos a la heladería:")
heladeria.añadir_producto(copa1)
heladeria.añadir_producto(malteada1)

# Ver el estado de la heladería
print("\nEstado de la heladería:")
print(heladeria)

# Probar vender productos
print("\nVendiendo productos:")
heladeria.vender("Copa Fresa-Vainilla")

# Ver el estado de la heladería después de la venta
print("\nEstado de la heladería después de la venta:")
print(heladeria)

# Probar si el ingrediente es sano
print("\nVerificación de si los ingredientes son sanos:")
for ingrediente in copa1.ingredientes:
    sano = es_sano(ingrediente.calorias, ingrediente.es_vegetariano)
    print(f"El ingrediente {ingrediente.nombre} es {'sano' if sano else 'no sano'}.")

# Verificar si el producto más rentable es el correcto
print("\nProducto más rentable en la heladería:")
producto_rentable = heladeria.producto_mas_rentable()
if producto_rentable:
    print(f"El producto más rentable es: {producto_rentable.nombre} con rentabilidad de {producto_rentable.calcular_rentabilidad()}")
else:
    print("No hay productos en la heladería.")
