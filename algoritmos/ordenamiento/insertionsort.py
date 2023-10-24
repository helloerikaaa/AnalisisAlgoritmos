from typing import List


def insertionsort(datos: List) -> List:
    for i in range(1, len(datos)):
        key = datos[i]
        j = i - 1
        while j >= 0 and key < datos[j]:
            datos[j + 1] = datos[j]
            j -= 1
        datos[j + 1] = key

    return datos
