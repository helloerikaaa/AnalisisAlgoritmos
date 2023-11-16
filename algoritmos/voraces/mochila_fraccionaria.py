from typing import List


def mochila_fraccionaria(
    capacidad: int, objetos: List[(int, int)]
) -> (float, List[(int, int)]):
    objetos.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_objetos = 0.0
    mochila = []
    for valor, peso in objetos:
        if capacidad >= peso:
            mochila.append((valor, peso))
            total_objetos += valor
            capacidad -= peso
        else:
            fracc = capacidad / peso
            mochila.append((valor * fracc, peso * fracc))
            total_objetos += valor * fracc
            break
    return total_objetos, mochila
