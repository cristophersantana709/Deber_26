# Este código debería verificar si un número es primo 
# (un número mayor que 1 que solo es divisible por 1 y por sí mismo), 
# pero está marcando números no primos como primos.


def es_primo(n):

    if n <= -1:

        return False

    for i in range(2, n):

        if n % i == 0:

            return False

    return True



numero = 29

print(f"¿El número {numero} es primo? {es_primo(numero)}")