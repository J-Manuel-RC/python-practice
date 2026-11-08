f"""
Crea un conjunto llamado usuarios_autorizados con los siguientes usuarios:

{"Manuel", "Carlos", "Ana", "Pedro"}

Después:
1. Solicita un nombre mediante input().
2. Comprueba si el usuario está autorizado utilizando in.
3. Si está autorizado, muestra "Acceso permitido".
4. Si no está autorizado, muestra "Acceso denegado".
Conceptos: conjuntos, input(), in y condicionales.
"""

usuarios_autorizados = {"Manuel", "Carlos", "Ana", "Pedro"}

nombre = input("Nombre: ")

if nombre.capitalize() in usuarios_autorizados:
  print("Acceso permitido")
else:
  print("Acceso denegado")