# listas y tuplas
f"""
Crea una lista llamada productos que contenga cinco productos.

Después:
1. Imprime el primer producto.
2. Imprime el último producto.
3. Modifica el segundo producto.
4. Agrega un producto nuevo.
5. Elimina uno de los productos.
"""

productos = ["Naranja", "Fresa", "Mango", "Sandia", "Lucuma"]

print(productos[0])
print(productos[-1])
productos[1] = "Platano"
productos.append("Mandarina")
productos.pop(3)


print("Resultado:")
for producto in productos:
  print(producto)