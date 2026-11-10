"""
Ejercicio 1 — Identificando dimensiones
Crea dos arrays: """

import numpy as np

numeros = np.array([10, 20, 30, 40, 50])
matriz = np.array([    
  [10, 20, 30],    
  [40, 50, 60]])

"""
Para cada uno imprime:
1. Su cantidad de dimensiones (ndim).
2. Su forma (shape).
3. Su cantidad de elementos (size).
4. Su tipo de dato (dtype).
"""

resumen = f"""
                           ARRAY
                  NUMEROS         MATRIZ       
Dimensiones     : {numeros.ndim}        -      {matriz.ndim}
Forma           : {numeros.shape}     -      {matriz.shape}
Cantidad emtos  : {numeros.size}        -      {matriz.size}
Tipo de dato    : {numeros.dtype}    -      {matriz.dtype}
"""

print(resumen)