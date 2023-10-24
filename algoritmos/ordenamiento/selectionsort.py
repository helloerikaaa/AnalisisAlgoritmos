from typing import List


def selectionsort(datos: List) -> List:
    n = len(datos)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if datos[j] < datos[min_index]:
                min_index = j
        datos[i], datos[min_index] = datos[min_index], datos[i]

    return datos
