f"""
Reto adicional — Registro de ventas
Una tienda registra las ventas de cinco días:

ventas = np.array([150, 230, 180, 320, 270])

Realiza lo siguiente:
1. Imprime las ventas originales.
2. Crea un nuevo array llamado ventas_duplicadas multiplicando todas las ventas por 2.
3. Crea otro array llamado ventas_con_descuento restando 20 a cada venta.
4. Imprime los tres arrays.
Pista: puedes realizar operaciones directamente sobre el array, sin utilizar for.
"""

import numpy as np

ventas = np.array([150, 230, 180, 320, 270])
ventas_duplicadas = ventas * 2
ventas_con_descuento = np.array(ventas - 20)

resumen = f"""
Ventas                : {ventas}
Ventas duplicadas     : {ventas_duplicadas}
Ventas con descuento  : {ventas_con_descuento}
"""

print(resumen)