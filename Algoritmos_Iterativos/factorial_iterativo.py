#######################################################
#                                                     #
# Función para encontrar el factorial del número n    #
# de manera iterativa.                                #
# Siendo el Factorial la siguiente expresión          #
#             n! = n x n-1 x n-2 x ... x 1            #
#######################################################


def factorial(n):
    # Si n es 0, entonces el resultado es 1, porque 0! = 1
    if n == 0:
        return 1
    # Inicialización de la variable fact en 1 ya que siempre el primer valor del cálculo es 1
    fact = 1
    # Ejecución del algoritmo recursivo desde 1 hasta n, ya que para n = 0 ya tenemos el cálculo
    for i in range(1, n + 1):
        # Se ejecuta la multiplicación de todos los valores desde 1 hasta n
        fact *= i
    # Regresa el factorial para n
    return fact


# Método main
if __name__ == '__main__':
    # Se pide el valor de n al usuario
    n = int(input('Ingresa el número para calcular el factorial: '))
    # Llamada a la función iterativa
    fact = factorial(n)
    print(f'El factorial de {n} es {fact}')
