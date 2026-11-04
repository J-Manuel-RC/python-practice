f"""
Ejercicio 1 — Función de saludo

Crea una función llamada saludar_usuario que:
1. Reciba el nombre de una persona como parámetro.
2. Muestre un saludo utilizando ese nombre.
3. Ejecute la función con al menos dos nombres diferentes.
Conceptos: def, parámetros y argumentos.
"""

def saludar_usuario(nombre):
  return f"Hola, {nombre}"

print(saludar_usuario("Manuel"))
print(saludar_usuario("Aube"))