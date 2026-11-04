f"""
Crea una calculadora de división.

Requisitos:
1. Solicita dos números.
2. Convierte ambos a float.
3. Realiza la división.
4. Controla el error si el usuario introduce letras.
5. Controla el error si el segundo número es cero.
6. Utiliza else para mostrar el resultado.
7. Utiliza finally para mostrar un mensaje de finalización.
"""

try:
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))

    resultado = num1 / num2

except ValueError:
    print("Valor incorrecto. Debes ingresar numeros.")

except ZeroDivisionError:
    print("No se puede dividir entre cero.")

else:
    print(f"El resultado es: {resultado}")

finally:
    print("Operacion finalizada")