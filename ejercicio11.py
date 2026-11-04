f"""
Ejercicio 2 — Calculadora básica

Crea cuatro funciones:
- sumar(a, b)
- restar(a, b)
- multiplicar(a, b)
- dividir(a, b)
Cada función debe recibir dos números y devolver el resultado con return.

Después, solicita dos números al usuario y muestra los resultados de las cuatro operaciones.

Considera qué sucede si el usuario intenta dividir entre cero.

Conceptos: funciones, parámetros, return y excepciones.
"""

def sumar(a, b):
  return a + b

def restar(a, b):
  return a - b
  
def multiplicar(a, b):
  return a * b

def dividir(a, b):
  try:
    return a / b
  except ZeroDivisionError:
    return "No se puede dividir por 0"


print(sumar(5,2))
print(restar(5, 2))
print(multiplicar(5, 2))
print(dividir(5, 0))