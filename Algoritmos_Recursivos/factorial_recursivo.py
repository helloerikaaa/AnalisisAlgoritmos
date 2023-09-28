#######################################################
#                                                     #
# Función para encontrar el factorial del número n    #
# de manera recursiva.                                #
# Caso base:                                          #
# 0! = 1                                              #
# Caso General:                                       #
#             n! = n x n-1 x n-2 x ... x 1            #
#######################################################


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Método main
if __name__ == '__main__':
    # Se pide el valor de n al usuario
    n = int(input('Ingresa el número para calcular el factorial: '))
    # Llamada a la función iterativa
    fact = factorial(n)
    print(f'El factorial de {n} es {fact}')