#  Modifica el código para que funcione correctamente y suma todos los elementos de la lista sin errores.

def sumar_lista(numeros):

    suma = 0

    for i in range(len(numeros)):

        suma += numeros[i]

    return suma



lista_numeros = [1, 2, 3, 4, 5]

print("La suma es:", sumar_lista(lista_numeros))