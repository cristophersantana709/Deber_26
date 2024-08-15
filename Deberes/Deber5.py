# Asegúrate de que el código funciona correctamente 
# para listas con números positivos, negativos e incluso con ceros.

def filtrar_pares(numeros):

    pares = []

    for numero in numeros:

        if numero % 2 == 0:

            pares.append(numero)

    return pares

# Pruebas
lista_numeros = [1, 2, 3, 4, 5, 6]
print("Números pares:", filtrar_pares(lista_numeros))

lista_numeros_negativos = [-1, -2, -3, -4, -5, -6]
print("Números pares negativos:", filtrar_pares(lista_numeros_negativos))

lista_numeros_con_cero = [0, 1, 2, 3, -2, -4]
print("Números pares con cero:", filtrar_pares(lista_numeros_con_cero))