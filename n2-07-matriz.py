f"""
Ejercicio 3 — Analizando las ventas
Una empresa registra sus ventas durante cuatro días en tres sucursales.

Crea esta matriz:
"""
import numpy as np

ventas = np.array([    
  [150, 200, 180],    
  [220, 250, 210],    
  [300, 280, 320],    
  [190, 170, 200]
])

#Responde mediante código:
resumen = f"""
1. ¿Cuántas dimensiones tiene?
{ventas.ndim}
2. ¿Cuántas filas y columnas tiene?
{ventas.shape}
3. ¿Cuántos valores almacena?
{ventas.size}
4. ¿Qué tipo de datos contiene?
{ventas.dtype}
"""

print(resumen)