#######################################################
#                                                     #
# Función para encontrar el n número de la serie      #
# Fibonacci de manera recursiva.                      #
# Casos base:                                         #
# f(0) = 0                                            #
# f(1) = 1                                            #
# Caso General:                                       #
#             f(n) = f(n-2) + f(n-1)                  #
#######################################################


# Creación de la función
def fibonacci(n):
    # Revisa si n cumple con los casos base
    if n <= 1:
        return n
    # Ejecuta el algoritmo recursivo hasta que se cumplen los casos base
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


# Método Main
if __name__ == '__main__':
    # Petición de datos al usuario
    n = int(input('Ingresa el valor de n para calcular el número fibonacci: '))
    # Llamada a la función iterativa
    fib = fibonacci(n)
    print(f'El valor de fibonnaci para {n} es {fib}')
