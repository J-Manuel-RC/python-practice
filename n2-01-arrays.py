f"""
Ejercicio 1 — Primer array
Crea un programa que:
1. Importe NumPy.
2. Cree un array llamado edades con los valores 18, 22, 25, 30, 35.
3. Imprima el array.
4. Imprima el array multiplicado por 2.
"""

import numpy as np

edades = np.array([18, 22, 25, 30, 35])

resumen = f"""
Array     : {edades}
Array x 2 : {edades * 2}
"""

print(resumen)