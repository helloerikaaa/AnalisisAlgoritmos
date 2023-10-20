import random


def generar_arreglo(n):
    arreglo = [random.randint(0, 100) for i in range(n)]
    return arreglo
