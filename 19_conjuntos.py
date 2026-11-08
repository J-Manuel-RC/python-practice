f"""
Una tienda tiene dos inventarios:

tienda_A = {"Laptop", "Mouse", "Teclado", "Monitor", "Audífonos"}
tienda_B = {"Mouse", "Teclado", "Impresora", "Cámara", "Laptop"}

Tu tarea:
1. Identifica los productos disponibles en ambas tiendas.
2. Identifica los productos exclusivos de cada tienda.
3. Obtén todos los productos disponibles.
4. Comprueba si "Laptop" está disponible en ambas tiendas.
5. Comprueba si "Impresora" está disponible en la tienda A.
"""

tienda_A = {"Laptop", "Mouse", "Teclado", "Monitor", "Audífonos"}
tienda_B = {"Mouse", "Teclado", "Impresora", "Cámara", "Laptop"}

producto = input("Buscar producto: ").strip().capitalize()

estaEnAmbos = producto in tienda_A and producto in tienda_B
estaEnA = producto in tienda_A
estaEnB = producto in tienda_B

resumen = f"""
========================================
Productos disponibles en ambas tiendas:
{tienda_A.intersection(tienda_B)}

Productos exclusivos de tienda A:
{tienda_A.difference(tienda_B)}

Productos exclusivos de tienda B:
{tienda_B.difference(tienda_A)}

Todos los productos:
{tienda_A.union(tienda_B)}

¿Está {producto} en ambas tiendas? {estaEnAmbos}
¿Está {producto} en tienda A? {estaEnA}
¿Está {producto} en tienda B? {estaEnB}
========================================
"""

print(resumen)