from tqdm import tqdm
from typing import List


def bubblesort(datos: List) -> List:
    n = len(datos)

    for i in tqdm(range(n)):
        swapped = False
        for j in range(0, n - i - 1):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                swapped = True
        if not swapped:
            break
    return datos
