f"""
Crea un pequeño sistema para administrar las notas de un estudiante.

Requisitos:
1. Crea una lista vacía llamada notas.
2. Solicita al usuario ingresar cinco notas.
3. Almacena cada nota en la lista.
4. Muestra todas las notas.
5. Calcula el promedio.
6. Muestra la nota mayor y la menor.
Puedes utilizar append(), for, input(), float(), sum(), max() y min().
"""

notas = []

while len(notas) < 5:
  nota = float(input(f"Nota #{len(notas) + 1}: "))
  notas.append(nota)
  
def imprimir():
    resultado = ""

    for nota in notas:
        resultado += f"{nota}\n"

    return resultado
  
promedio = sum(notas) / len(notas)
mayor = max(notas)
menor = min(notas)

resumen = f"""
====================
Notas:
{imprimir()}
Promedio:   {promedio:.1f}
Nota mayor: {mayor}
Nota menor: {menor}
====================
"""

print(resumen)