# Este código debería comprobar si una palabra es un palíndromo 
# (una palabra que se lee igual de adelante hacia atrás), 
# pero no está funcionando correctamente para ciertas palabras.

def es_palindromo(palabra):

    palabra_invertida = ""

    for i in range(len(palabra)):

        palabra_invertida += palabra[i-1]

    return palabra == palabra_invertida



palabra = "radar"

print(f"¿La palabra '{palabra}' es un palíndromo? {es_palindromo(palabra)}")