f"""
Reto adicional — Diagnóstico de matrices
Crea tres arrays diferentes:
- array1: una matriz de 3 filas y 4 columnas con números enteros.
- array2: una matriz de 5 filas y 2 columnas con números decimales.
- array3: un array unidimensional con 8 números.
Después crea un pequeño informe que muestre para cada uno:
- Nombre del array.
- Dimensiones.
- Forma.
- Cantidad de elementos.
- Tipo de dato.
No necesitas escribir cada propiedad por separado. Puedes utilizar un for para recorrer los arrays.
"""
import numpy as np

enteros = np.array([
  [10, 20, 30, 40],
  [50, 60, 70, 80],
  [90, 100, 110, 120]
])

decimales = np.array([
  [11.5, 17.5],
  [19.5, 15.0],
  [12.5, 16.0],
  [17.0, 20.0],
  [10.5, 15.5]
])

uni = np.array([5, 10, 15, 20, 25, 30, 35, 40])

informe = f"""
- Nombre                  : Enteros - decimales - Unidimensional
- Dimensiones.            : {enteros.ndim}       - {decimales.ndim}         - {uni.ndim}
- Forma.                  : {enteros.shape}  - {decimales.shape}    - {uni.shape}
- Cantidad de elementos.  : {enteros.size}      - {decimales.size}        - {uni.size}
- Tipo de dato.           : {enteros.dtype}   - {decimales.dtype}   - {uni.dtype}
"""

print(informe)