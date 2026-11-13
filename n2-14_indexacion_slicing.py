"""
Ejercicio 5 — Auditoría de calificaciones
Una institución almacena las calificaciones de siete estudiantes en seis asignaturas.
"""

import numpy as np
calificaciones = np.array([
    [18, 15, 17, 19, 16, 20],
    [14, 16, 13, 18, 15, 17],
    [20, 19, 18, 17, 20, 19],
    [12, 14, 15, 13, 16, 14],
    [17, 18, 16, 20, 19, 18],
    [15, 13, 14, 16, 12, 15],
    [19, 20, 18, 17, 19, 20]
])

"""
Objetivos:
1. Extrae las calificaciones de los estudiantes 2, 4 y 6.
2. Extrae las calificaciones de las asignaturas 1, 3, 4 y 6 para todos los estudiantes.
3. Obtén una submatriz con los estudiantes 3, 4, 5 y las asignaturas 2, 3 y 4.
4. Extrae las calificaciones del último estudiante en orden inverso.
5. Construye una selección que contenga los estudiantes 1, 3, 5 y 7, junto con las asignaturas 1, 3 y 6.
Condición: no modifiques la matriz original. Guarda cada selección en una variable independiente.

Pista: aquí necesitarás combinar listas de índices con slicing. Recuerda que los índices de NumPy comienzan en cero.
"""