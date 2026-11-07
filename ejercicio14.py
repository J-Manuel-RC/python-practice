f"""
Ejercicio 2 — Inventario de productos

Crea un diccionario con tres productos. Cada producto debe tener:
- Nombre.
- Precio.
- Stock.
Después:
1. Recorre el diccionario con for.
2. Muestra el nombre, precio y stock de cada producto.
3. Calcula el valor total del inventario.
Fórmula:

Conceptos: diccionarios anidados, items() y acumuladores.
"""

productos = {
  "P001" : {
    "Nombre" : "Arroz",
    "Precio" : 4.30,
    "Stock" : 100
  },
  "P002" : {
    "Nombre" : "Azucar",
    "Precio" : 4.50,
    "Stock" : 150
  },
  "P003" : {
    "Nombre" : "Fideos",
    "Precio" : 4.00,
    "Stock" : 200
  }
}

total = 0
for codigo in productos:
  print("""
========================
  """)
  for clave, valor in productos[codigo].items():
    print(f"{clave} : {valor}")
  total += productos[codigo]["Precio"] * productos[codigo]["Stock"]

print(f"\nValor total del inventario: S/ {total:.2f}")