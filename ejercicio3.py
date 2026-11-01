# New Python file
f"""
Ejercicio 3. Cajero automático
Dificultad: 9/10


Simula un cajero automático con un saldo inicial de S/ 1,000.

Requisitos:
1. Muestra un menú que se repita hasta que el usuario elija salir:
   - 1: Consultar saldo.
   - 2: Retirar dinero.
   - 3: Depositar dinero.
   - 4: Salir.
2. Si elige retirar, solicita el importe.
3. Rechaza los retiros que sean negativos, iguales a cero o superiores al saldo disponible.
4. Si elige depositar, solicita el importe y rechaza cantidades iguales a cero o negativas.
5. Actualiza el saldo después de cada operación válida.
6. Si se introduce una opción distinta de 1, 2, 3 o 4, muestra un mensaje de opción inválida.
7. Al salir, muestra el saldo final.
Ejemplo de funcionamiento:
=== CAJERO AUTOMÁTICO ===
1. Consultar saldo
2. Retirar dinero
3. Depositar dinero
4. Salir

Selecciona una opción: 2
Importe a retirar: 120
Retiro exitoso.

Selecciona una opción: 1
Saldo disponible: S/ 880.00

Selecciona una opción: 4
Gracias por utilizar el cajero.
Saldo final: S/ 880.00


Pista: el bucle principal controla el menú. Dentro de él, las condiciones deciden qué operación ejecutar. No olvides que el saldo debe conservar su valor entre una vuelta y otra.
"""