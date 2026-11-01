f"""
Ejercicio 2. Análisis de números
Dificultad: 8/10

Crea un programa que analice una secuencia de números enteros introducidos por el usuario.

Requisitos:
1. Solicita números enteros repetidamente.
2. El programa debe terminar cuando el usuario introduzca 0. El cero no cuenta como dato analizado.
3. Cuenta cuántos números positivos y cuántos negativos se ingresaron.
4. Calcula la suma de los números positivos y la suma de los negativos por separado.
5. Identifica el mayor número ingresado, sin contar el cero.
6. Al terminar, muestra un resumen. Si no se ingresó ningún número distinto de cero, informa que no hay datos para analizar.
Ejemplo:
Introduce un número (0 para terminar): 8
Introduce un número (0 para terminar): -3
Introduce un número (0 para terminar): 12
Introduce un número (0 para terminar): -5
Introduce un número (0 para terminar): 0

Positivos: 2
Negativos: 2
Suma de positivos: 20
Suma de negativos: -8
Mayor número: 12

Pista: while puede ayudarte a repetir hasta recibir el cero. Necesitarás varios contadores y acumuladores. Presta especial atención a cómo inicializas el mayor número.
"""

numPositivos = []
numNegativos = []

while True:
  numero = int(input("Introduce un número (0 para terminar): "))
  
  if numero == 0:
    break
  elif numero < 0:
    numNegativos.append(numero)
  elif numero > 0:
    numPositivos.append(numero)

if len(numPositivos) == 0 and len(numNegativos) == 0:
  print("No hay datos para analizar.")
  
else:
  positivos = len(numPositivos)
  negativos = len(numNegativos)
  sumaMayores = sum(numPositivos)
  sumaMenores = sum(numNegativos)
  mayor = max(numPositivos) if positivos > 0 else 0
  
resumen = f"""
=====================================
      Positivos:         {positivos}
      Negativos:         {negativos}
      Suma de positivos: {sumaMayores}
      suma de negativos: {sumaMenores}
      Numero mayor:      {mayor}
=====================================
"""

print(resumen)
