f"""
Ejercicio 1 — Registro de estudiante

Crea un diccionario llamado estudiante que contenga:
- Nombre.
- Edad.
- Carrera.
- Ciclo académico.
Después:
1. Muestra el nombre y la carrera.
2. Modifica la edad.
3. Agrega una clave llamada universidad.
4. Muestra el diccionario completo.
Conceptos: creación, acceso, modificación y adición.
"""

estudiante = {
  "Nombre" : "J. Manuel",
  "Edad" : 30,
  "Carrera" : "Ing. de Sistemas",
  "Ciclo académico" : 4
}

def imprimir():
  for clave, valor in estudiante.items():
    print(f"{clave} : {valor}")

estudiante.update({"Edad" : 31})
estudiante.update({"Universidad" : "Cibertec"})

resumen = f"""
==================================
Nombre: {estudiante["Nombre"]}
Carrera: {estudiante["Carrera"]}
==================================
"""

print(resumen)
imprimir()