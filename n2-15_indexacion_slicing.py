"""
Ejercicio 6 — Control de inventario y movimientos
Una empresa registra las unidades disponibles de seis productos durante ocho semanas.

Cada fila representa una semana y cada columna un producto.
"""

import numpy as np
inventario = np.array([
    [120, 85, 140, 90, 110, 75],
    [115, 80, 135, 95, 105, 70],
    [110, 78, 130, 88, 100, 68],
    [105, 75, 125, 85, 95, 65],
    [100, 70, 120, 80, 90, 60],
    [95, 68, 115, 78, 85, 55],
    [90, 65, 110, 75, 80, 50],
    [85, 60, 105, 70, 75, 45]
])

"""
Objetivos:
1. Extrae los inventarios de las semanas 2, 4, 6 y 8.
2. Extrae los inventarios de los productos 2, 4 y 6 durante todas las semanas.
3. Extrae los inventarios de las semanas 3 a 7 y los productos 1 a 4.
4. Invierte simultáneamente el orden de las semanas y el de los productos.
5. Selecciona las semanas 1, 3, 5 y 7, junto con los productos 2, 4 y 6, conservando una matriz de cuatro filas y tres columnas.
Condición: no utilices bucles ni modifiques la matriz original.

Pista especial: el quinto objetivo tiene una dificultad adicional. Cuando seleccionas simultáneamente filas y columnas mediante listas de índices, NumPy puede emparejar las posiciones en lugar de formar todas las combinaciones posibles. Investiga y utiliza np.ix_() para resolverlo.

Ejemplo de su estructura:

seleccion = inventario[
    np.ix_([0, 2], [1, 3])
]

No necesitas memorizar np.ix_() todavía; lo importante es comprender por qué se utiliza.
"""