f"""
Ejercicio 3 — Consulta de estudiantes

Crea un diccionario que almacene tres estudiantes y sus respectivas notas.

Después:
1. Solicita al usuario el nombre de un estudiante.
2. Consulta su nota.
3. Si existe, muestra su calificación.
4. Si no existe, muestra "Estudiante no encontrado".
Utiliza get() para resolverlo.

Conceptos: consulta, get() y condicionales.
"""

notas = {
  "Manuel": 18,
  "Carlos": 15,
  "Ana": 20
}
  
nombre = input("Nombre a consultar: ")

print(notas.get(nombre.capitalize(), "Estudiante no encontrado"))
