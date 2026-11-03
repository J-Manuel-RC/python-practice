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

saldo = 1000

def consultar():
  print(f"Saldo disponible {saldo:.2f}")
  
def retirar(importe):
  global saldo
  if importe > saldo:
    print(f"""
    Usted no cuenta con saldo suficiente.
    Saldo disponible {saldo:.2f}""")

  elif importe <= 0:
    print("""Imposible retirar monto menor a 0.
            Intentelo nuevamente""")
  else:
    saldo -= importe
    print(f"Retiro exitoso. Saldo: S/ {saldo:.2f}")

def depositar(importe):
  global saldo
  if importe <= 0:
    print("Operación inválida")

  else:
    saldo += importe
    print(f"Depósito exitoso. Saldo: S/ {saldo:.2f}")

    
while True:
  print("""
    === CAJERO AUTOMÁTICO ===

    1. Consultar saldo
    2. Retirar dinero
    3. Depositar dinero
    4. Salir
    """)

  operacion = int(input("Seleccione una opción: "))

  match operacion:
    case 1: consultar()
    case 2: 
      importe = float(input("Importe a retirar: "))
      retirar(importe)
    case 3: 
      importe = float(input("Importe a depositar: "))
      depositar(importe)
    case 4: 
      print(f"""
            Gracias por utilizar el cajero.
            Saldo final: S/ {saldo:.2f}
            """)
      break
    case _:
      print("Opción invalida. Vuelva a intentarlo")
