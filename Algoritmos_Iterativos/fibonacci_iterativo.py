#######################################################
#                                                     #
# Función para encontrar el n número de la serie      #
# Fibonacci de manera iterativa.                      #
# Siendo Fibonacci la siguiente expresión matemática  #
#             f(n) = f(n-2) + f(n-1)                  #
#######################################################


# Creación de la función
def fibonacci(n):
    # Inicializa un arreglo con los dos primeros elementos de la serie, en este caso 0 y 1
    fib = [0, 1]
    # Si el valor de n es menor o igual a cero, 
    # entonces regresa que el número fibonacci es igual a n
    if n <= 1:
        return fib[n]
    # Si la condición no se cumple, entonces se ejecuta el algoritmo iterativo
    else:
        # El algoritmo iterativo se ejecuta desde 2 hasta n. 
        # Empieza desde 2 porque ya conocemos los 2 primeros elementos de la serie
        for i in range(2, n+1):
            # Por cada iteración de i, se agrega un nuevo elemento a la lista, 
            # hasta que i es igual a n
            fib.append(fib[i-2] + fib[i-1])
        # Se regresa el valor de la serie fibonacci para n
        return fib[n]


# Método Main
if __name__ == '__main__':
    # Petición de datos al usuario
    n = int(input('Ingresa el valor de n para calcular el número fibonacci: '))
    # Llamada a la función iterativa
    fib = fibonacci(n)
    print(f'El valor de fibonnaci para {n} es {fib}')
