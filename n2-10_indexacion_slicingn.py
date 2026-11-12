"""
Ejercicio 2 — Trabajando con matrices
Una empresa registra sus ventas en tres sucursales durante cuatro días
Representadas en la siguiente matriz:
"""
import numpy as np
ventas = np.array([
    [150, 200, 180],
    [220, 250, 210],
    [300, 280, 320],
    [190, 170, 200]
])

"""
Utilizando indexación, imprime:
1. Las ventas del primer día.
2. Las ventas del tercer día.
3. Las ventas de la segunda sucursal durante los cuatro días.
4. La venta del cuarto día en la tercera sucursal.
Recuerda: las filas representan los días y las columnas representan las sucursales.
"""

resumen =f"""
1. Las ventas del primer día:
{ventas[0, :]}
2. Las ventas del tercer día:
{ventas[2, :]}
3. Las ventas de la segunda sucursal durante los cuatro días:
{ventas[:, 1]}
4. La venta del cuarto día en la tercera sucursal:
{ventas[3, 2]}
"""

print(resumen)