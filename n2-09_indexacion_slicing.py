"""
Ejercicio 1 — Extracción de elementos
Crea este array: """

import numpy as np
numeros = np.array([12, 24, 36, 48, 60, 72, 84, 96])

"""
Utilizando indexación y slicing, imprime:
1. El primer elemento.
2. El último elemento.
3. El elemento que ocupa el índice 4.
4. Los elementos desde el índice 2 hasta el 5, sin incluir el 5.
5. Los primeros cuatro elementos.
6. Los últimos tres elementos.
7. Todos los elementos en orden inverso.
"""

resumen = f"""
Primer elemento:\t{numeros[0]}
Ultimo elemento:\t{numeros[-1]}
Cuarto indice:\t{numeros[3]}
Del 2do al 5to:\t{numeros[2:5]}
Primeros 4:\t{numeros[:4]}
Ultimos 3:\t{numeros[-3:]}
Orden inverso:\t{numeros[::-1]}
""".expandtabs(20)

print(resumen)