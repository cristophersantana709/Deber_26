# Corrige el código para que la cadena combinada no tenga un espacio extra al final.

def combinar_cadenas(lista):
    if not lista:
        return ""
    
    cadena = lista[0]  
    for palabra in lista[1:]:  
        cadena += " " + palabra
    
    return cadena

lista_cadenas = ["Hola", "mundo", "esto", "es", "Python"]
print("Cadena combinada:", combinar_cadenas(lista_cadenas))