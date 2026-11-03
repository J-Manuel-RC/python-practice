f"""
Crea un programa que solicite al usuario su edad.

Requisitos:
1. Solicita la edad utilizando input().
2. Convierte el dato a int.
3. Utiliza try y except.
4. Si introduce letras, muestra un mensaje indicando que debe ingresar números.
5. Si introduce un número válido, muestra su edad.
"""

try:
  edad = int(input("Introduce tu edad: "))
  
except ValueError:
  print("Debe introducir un numero")

else:
  print(f"Su edad es: {edad}")