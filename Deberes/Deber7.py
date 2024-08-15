# Corrige el código para que cuente el número de palabras en la oración correctamente.

def contar_palabras(oracion):

    palabras = oracion.split(" ")

    return len(palabras)



oracion = "Este es un ejemplo de oración"

print("Número de palabras:", contar_palabras(oracion))