from typing import List


def busqueda_binaria(datos: List, num: int) -> int:
    low, high = 0, len(datos) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = datos[mid]

        if mid_element == num:
            return mid
        elif mid_element < num:
            low = mid + 1
        else:
            high = mid - 1

    return -1
