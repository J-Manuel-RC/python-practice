f"""
Crea un pequeño sistema para consultar productos almacenados en una lista.

Utiliza esta lista:

productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Impresora"]

Requisitos:
1. Solicita al usuario un índice.
2. Convierte el índice a entero.
3. Muestra el producto correspondiente.
4. Controla ValueError si introduce letras.
5. Controla IndexError si introduce una posición inexistente.
6. Utiliza else para mostrar un mensaje cuando la consulta sea exitosa.
Reto adicional: evita que el usuario ingrese índices negativos, ya que Python permite utilizarlos para acceder a elementos desde el final de una lista.
"""

productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Impresora"]

try:
  indice = int(input("Selecciona un indice del 1 al 5: "))

  print(productos[indice - 1])
  
except ValueError:
   print("DEbe introducir un numero")

except IndexError:
  print("El indice indicado no existe. Seleccione del 1 al 5")

except:
  if indice < 1:
    print("Solo valores del 1 al 5")