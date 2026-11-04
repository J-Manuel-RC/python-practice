f"""
Ejercicio 3 — Sistema de ventas

Desarrolla una función llamada calcular_venta que:
1. Reciba el precio de un producto.
2. Reciba la cantidad vendida.
3. Calcule el importe total.
4. Devuelva el resultado con return.
Luego solicita los datos al usuario y muestra:
- Nombre del producto.
- Precio unitario.
- Cantidad.
- Importe total.
Conceptos: reutilización de funciones y retorno de valores.
"""

def calcular_venta(precio, cantidad):
    return precio * cantidad


try:
    nombre = input("Producto: ").strip()

    if not nombre:
        raise ValueError("El nombre del producto no puede estar vacío")

    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    if precio <= 0:
        raise ValueError("El precio debe ser mayor que cero")

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero")

    resumen = f"""
    ==================================
    - Nombre del producto: {nombre}
    - Precio unitario: S/ {precio:.2f}
    - Cantidad: {cantidad}
    - Importe total: S/ {calcular_venta(precio, cantidad):.2f}
    ==================================
    """

    print(resumen)

except ValueError as error:
    print(f"Error: {error}")
