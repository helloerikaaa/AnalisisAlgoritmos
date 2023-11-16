import random


def generar_arreglo(n):
    arreglo = [random.randint(0, 10) for _ in range(n)]
    return arreglo
