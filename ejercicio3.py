# Este código debería encontrar el valor máximo en una lista de números, 
# pero devuelve resultados incorrectos.

def encontrar_maximo(numeros):

    maximo = 0

    for numero in numeros:

        if numero > maximo:

            maximo = numero

    return maximo



lista_numeros = [-10, -20, -30, -5, -15]

print("El valor máximo es:", encontrar_maximo(lista_numeros))