from typing import List


def mergesort(datos: List) -> List:
    n = len(datos)
    if n == 1:
        return datos

    mitad = n // 2
    izq = datos[:mitad]
    der = datos[mitad:]

    izq = mergesort(izq)
    der = mergesort(der)

    return _merge(izq, der)


def _merge(izq: List, der: List) -> List:
    datos_ordenados = []
    i_izq, i_der = 0, 0

    while i_izq < len(izq) and i_der < len(der):
        if izq[i_izq] < der[i_der]:
            datos_ordenados.append(izq[i_izq])
            i_izq += 1
        else:
            datos_ordenados.append(der[i_der])
            i_der += 1

    datos_ordenados.extend(izq[i_izq:])
    datos_ordenados.extend(der[i_der:])

    return datos_ordenados
