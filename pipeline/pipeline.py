from consts.consts import Ordenamiento
from algoritmos.ordenamiento.mergesort import mergesort
from algoritmos.ordenamiento.quicksort import quicksort
from algoritmos.ordenamiento.bubblesort import bubblesort

ALGORITMOS = {
    Ordenamiento.MERGESORT: mergesort,
    Ordenamiento.BURBUJA: bubblesort,
    Ordenamiento.QUICKSORT: quicksort,
}
