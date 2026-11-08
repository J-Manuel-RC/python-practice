f"""
Tienes la siguiente lista:

numeros = [10, 20, 10, 30, 40, 20, 50, 30, 60]

Tu tarea:
1. Convierte la lista en un conjunto.
2. Muestra los números sin duplicados.
3. Agrega el número 70.
4. Elimina el número 30.
5. Convierte nuevamente el conjunto en una lista.
Conceptos: set(), add(), remove() y list().
"""

numeros = [10, 20, 10, 30, 40, 20, 50, 30, 60]

lista = set(numeros)
lista.add(70)
lista.remove(30)

for num in lista:
  print(num)

numeros = list(lista)