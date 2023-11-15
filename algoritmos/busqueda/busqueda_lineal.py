from typing import List


def busqueda_lineal(datos: List[int], num: int) -> int:
    for i in range(len(datos)):
        if datos[i] == num:
            return i
    return -1
