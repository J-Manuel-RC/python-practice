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
Ventas 1er dia:
{ventas[:, :1]}

Ventas 3er dia:
{ventas[:, 2:]}

Ventas 2da sucursal de los 4 dias:
{ventas[:, 1:2]}

Venta 4to dia de 3ra sucursal:
{ventas[3:, 2:]}
"""

print(resumen)