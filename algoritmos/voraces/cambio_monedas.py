from typing import List


def cambio_monedas(cantidad: int, denoms: List[int]) -> List[int]:
    sol = []
    total = 0
    denoms.sort(reverse=True)
    for d in denoms:
        while total + d <= cantidad:
            sol.append(d)
            total += d
    return sol
