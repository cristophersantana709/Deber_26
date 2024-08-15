#  El siguiente código debería combinar todas las cadenas de una lista en una sola cadena, 
# separadas por un espacio, pero está agregando un espacio extra al final.

def combinar_cadenas(lista):

    cadena = ""

    for palabra in lista:

        cadena += palabra + " "

    return cadena



lista_cadenas = ["Hola", "mundo", "esto", "es", "Python"]

print("Cadena combinada:", combinar_cadenas(lista_cadenas))