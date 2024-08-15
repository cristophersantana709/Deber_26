# Este código debería invertir una cadena 
# (es decir, escribirla al revés), 
# pero produce un resultado incorrecto.

def invertir_cadena(cadena):

    invertida = ""

    for i in range(len(cadena)):

        invertida += cadena[i - 1]

    return invertida



cadena = "Python"

print("Cadena invertida:", invertir_cadena(cadena))