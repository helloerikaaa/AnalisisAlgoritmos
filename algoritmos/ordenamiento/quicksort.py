from typing import List


def quicksort(datos: List) -> List:
    if len(datos) <= 1:
        return datos

    pivot = datos[len(datos) // 2]
    left = [x for x in datos if x < pivot]
    middle = [x for x in datos if x == pivot]
    right = [x for x in datos if x > pivot]
    return quicksort(left) + middle + quicksort(right)
