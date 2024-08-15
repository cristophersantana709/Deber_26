# Optimiza el código para que se detenga cuando sea evidente que el número no es primo, 
# en lugar de recorrer todos los números hasta n-1

def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 y 3 son primos
    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminar múltiplos de 2 y 3
    
    # Verifica divisores desde 5 hasta sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Verifica i y i+2 (es decir, 5 y 7, 11 y 13, etc.)s
    
    return True

numero = 29

print(f"¿El número {numero} es primo? {es_primo(numero)}")