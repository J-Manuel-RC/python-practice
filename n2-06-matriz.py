f"""
Ejercicio 2 — Matriz de estudiantes
Una institución registra las calificaciones de cuatro estudiantes en tres asignaturas.

Crea una matriz llamada calificaciones con estos datos:
Estudiante	Matemática	Programación	Inglés
Estudiante 1	18	16	15
Estudiante 2	14	17	19
Estudiante 3	20	18	17
Estudiante 4	12	15	16

Después imprime:
1. La matriz completa.
2. Su cantidad de dimensiones.
3. Su forma.
4. La cantidad total de calificaciones.
5. El tipo de dato.
"""
import numpy as np

calificaciones = np.array([
  [18,	16,	15],
  [14,	17,	19],
  [20,	18,	17],
  [12,	15,	16],
])

resumen = f"""
   MATRIZ
{calificaciones}

Dimensiones    : {calificaciones.ndim}
Forma          : {calificaciones.shape}
Cantidad emtos : {calificaciones.size}
Tipo de dato   : {calificaciones.dtype}
"""

print(resumen)