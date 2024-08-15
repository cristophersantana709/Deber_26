#  Este código debería contar el número de palabras en una oración, pero no funciona como se espera.

def contar_palabras(oracion):

    palabras = oracion.split(",")

    return len(palabras)



oracion = "Este es un ejemplo de oración"

print("Número de palabras:", contar_palabras(oracion))