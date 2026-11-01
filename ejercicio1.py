# Ejercicio 1
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