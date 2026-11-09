f"""
Ejercicio 3 — Secuencias numéricas
Crea dos arrays:
1. temperaturas: genera los números desde 10 hasta 50, avanzando de 5 en 5.
2. mediciones: genera 6 valores distribuidos uniformemente entre 0 y 100.
Utiliza np.arange() y np.linspace() respectivamente.
"""

import numpy as np

temperaturas = np.arange(10, 51, 5)
mediciones = np.linspace(0, 100, 6)

resumen = f"""
Temperaturas  : {temperaturas}
Mediciones    : {mediciones}
"""

print(resumen)