"""
Ejercicio 3 — Selección de información específica
Utiliza esta matriz:
filas = estudiantes (5)
columnas = asignaturas (4)
"""

import numpy as np
calificaciones = np.array([
    [18, 16, 15, 19],
    [14, 17, 19, 16],
    [20, 18, 17, 20],
    [12, 15, 16, 14],
    [17, 19, 18, 16]
])


"""
Realiza las siguientes operaciones:
1. Extrae las calificaciones del primer estudiante.
2. Extrae las calificaciones de los estudiantes 2, 3 y 4.
3. Extrae las calificaciones de la segunda asignatura de todos los estudiantes.
4. Extrae una submatriz con las filas de los estudiantes 1, 2 y 3, y las columnas de las asignaturas 2 y 3.
Recuerda que los índices comienzan en cero.
"""

resumen =f"""
Calificaciones 1er estudiante:
{calificaciones[:1, :]}
  
Calificaciones estudiantes 2,3 y 4:
{calificaciones[1:4, :]}

Calificaciones 2da asignatura de todos los estudiantes:
{calificaciones[:, 1:2]}

Subamatriz de los estudiantes 1, 2 y 3, y las columnas de las asignaturas 2 y 3:
{calificaciones[:3, 1:3]}
"""

print(resumen)