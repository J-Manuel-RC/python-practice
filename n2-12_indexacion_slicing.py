"""
Reto adicional — Informe de ventas
Una empresa registra sus ventas durante cinco días en cuatro sucursales.
"""

import numpy as np
ventas = np.array([
    [150, 200, 180, 220],
    [250, 300, 280, 270],
    [190, 210, 230, 200],
    [320, 350, 310, 330],
    [280, 260, 290, 300]
])

"""
Construye un informe que permita obtener:
1. Todas las ventas del tercer día.
2. Todas las ventas de la cuarta sucursal.
3. Las ventas de los primeros tres días.
4. Las ventas de los dos últimos días.
5. Una selección de las ventas de los días 2, 3 y 4, correspondientes a las sucursales 1 y 2.
Condición: resuelve todo mediante indexación y slicing. No utilices bucles.
"""