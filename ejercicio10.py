# Este código debería calcular el factorial de un número 
# (el producto de todos los números enteros positivos hasta ese número), 
# pero no produce el resultado correcto.

def factorial(n):

    resultado = 1

    for i in range(1, n + 1):

        resultado *= i

    return resultado



numero = 5

print("Factorial de", numero, "es:", factorial(numero))