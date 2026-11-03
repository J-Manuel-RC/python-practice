f"""
Crea una lista llamada numeros con los siguientes valores:

numeros = [10, 20, 30, 40, 50]

Después utiliza un bucle for para:
1. Mostrar todos los números.
2. Calcular la suma de todos los números.
3. Calcular el promedio.
4. Mostrar únicamente los números mayores que 25.
"""

numeros = [10, 20, 30, 40, 50]

print("Los numeros de la lista son:")
for num in numeros:
  print(num)

print(f"Suma: {sum(numeros)}")
print(f"Promedio: {sum(numeros) / len(numeros)}")

print("Numeros mayores a 25:")
for num in numeros:
  if num > 25:
    print(num)