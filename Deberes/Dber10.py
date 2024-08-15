# Asegúrate de que el código funcione correctamente 
# para calcular el factorial de cualquier número entero positivo.

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

numero = 5
print("Factorial de", numero, "es:", factorial(numero))

# También probemos con 0
print("Factorial de 0 es:", factorial(0))

# Ejemplo para un número negativo (debería generar un error)
try:
    print("Factorial de -5 es:", factorial(-5))
except ValueError as E:
    print(E)