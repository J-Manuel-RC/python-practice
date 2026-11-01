# Ejercicio 1
f"""
Ejercicio 1. Sistema de ventas
Dificultad: 7/10


Una tienda necesita registrar las ventas de sus productos y calcular cuánto dinero ha generado.

Requisitos:
1. Solicita al usuario cuántas ventas desea registrar.
2. Recorre esa cantidad de ventas usando un bucle.
3. Solicita el importe de cada venta.
4. Si el importe es negativo, debe volver a solicitarlo hasta que sea válido.
5. Acumula el importe total de las ventas.
6. Al finalizar, muestra:
   - El total recaudado.
   - La cantidad de ventas registradas.
   - El promedio por venta.
   
Ejemplo del resultado esperado:
¿Cuántas ventas registrarás?: 3

Importe de la venta 1: 100
Importe de la venta 2: -20
Importe inválido. Intenta nuevamente.
Importe de la venta 2: 50
Importe de la venta 3: 150

Total recaudado: S/ 300.00
Ventas registradas: 3
Promedio por venta: S/ 100.00
"""
print("¿Cuántas ventas desea registrar?")
ventas = int(input("Cantidad: "))

while ventas <= 0:
    print("Debe registrar al menos una venta.")
    ventas = int(input("Cantidad: "))
  
lista = []

for i in range(ventas):
  importe = float(input(f"Importe de la venta {i+1})"))
  
  while(importe <= 0.0):
    
    print("El importe debe ser superior a S/ 0.00")
    importe = float(input(f"Importe de la venta {i + 1}: "))

  lista.append(importe)

total = sum(lista)
promedio = total / len(lista)

mensaje = f"""
============================
    Total:    S/{total:.2f}
    Ventas:   {len(lista)}
    Promedio: S/{promedio:.2f}
============================
"""

print(mensaje)