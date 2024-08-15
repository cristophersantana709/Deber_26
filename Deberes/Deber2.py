# Modifica el código para que, si la lista está vacía, 
# devuelva un mensaje que diga "La lista está vacía" 
# en lugar de intentar calcular el promedio.

def calcular_promedio(numeros):

    suma = 0

    for numero in numeros:
        
        suma += numero

    promedio = suma / len(numeros)

    return promedio



lista_numeros = [10, 20, 30, 40, 50]

promedio = calcular_promedio(lista_numeros)
if promedio is not None:
    print("El promedio es:", promedio)
else:
    print("La lista está vacía, no se puede calcular el promedio.")