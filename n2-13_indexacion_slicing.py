"""
Ejercicio 4 — Análisis de ventas por sucursal
Una empresa registra sus ventas durante seis meses en cinco sucursales.

Cada fila representa un mes y cada columna una sucursal.
"""

import numpy as np

ventas = np.array([
    [1200, 1500, 1800, 1100, 1600],
    [1350, 1450, 1900, 1250, 1700],
    [1400, 1600, 2100, 1300, 1800],
    [1550, 1700, 2000, 1400, 1950],
    [1650, 1800, 2300, 1500, 2050],
    [1750, 1900, 2500, 1600, 2200]
])

"""
Objetivos:
1. Extrae todas las ventas de los meses 2, 3, 4 y 5.
2. Extrae las ventas de las sucursales 1, 3 y 5 durante los seis meses.
3. Extrae una submatriz que contenga los meses 3, 4 y 5, y las sucursales 2, 3 y 4.
4. Extrae las ventas de los últimos tres meses de las últimas dos sucursales.
5. Invierte el orden de los meses sin alterar el orden de las sucursales.
Condición: utiliza slicing e indexación avanzada. No utilices bucles.

Pista: para seleccionar las sucursales 1, 3 y 5, necesitas índices no consecutivos.
"""

resumen = f"""
1. Extrae todas las ventas de los meses 2, 3, 4 y 5:
{ventas[1:5, :]}

2. Extrae las ventas de las sucursales 1, 3 y 5 durante los seis meses:
{ventas[: , [0, 2, 4]]}

3. Extrae una submatriz que contenga los meses 3, 4 y 5, y las sucursales 2, 3 y 4:
{ventas[2:5, 1:4]}

4. Extrae las ventas de los últimos tres meses de las últimas dos sucursales:
{ventas[-3: , -2:]}

5. Invierte el orden de los meses sin alterar el orden de las sucursales:
{ventas[::-1, :]}
"""

print(resumen)