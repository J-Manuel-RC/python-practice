f"""
Ejercicio 2 — Creación de arrays
Crea tres arrays:
1. ceros: debe contener 6 ceros.
2. unos: debe contener 5 unos.
3. pares: debe contener los números pares desde 2 hasta 20, incluyendo el 20.
Utiliza las funciones que hemos aprendido.
"""

import numpy as np

ceros = np.zeros(6)
unos = np.ones(5)
pares = np.arange(2, 21, 2)

resumen = f"""
Ceros     : {ceros}
Unos      : {unos}
Pares     : {pares}
"""

print(resumen)