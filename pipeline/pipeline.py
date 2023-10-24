from consts.consts import Ordenamiento
from algoritmos.ordenamiento.mergesort import mergesort
from algoritmos.ordenamiento.quicksort import quicksort
from algoritmos.ordenamiento.bubblesort import bubblesort
from algoritmos.ordenamiento.insertionsort import insertionsort
from algoritmos.ordenamiento.selectionsort import selectionsort

ALGORITMOS = {
    Ordenamiento.MERGESORT: mergesort,
    Ordenamiento.BURBUJA: bubblesort,
    Ordenamiento.QUICKSORT: quicksort,
    Ordenamiento.INSERCION: insertionsort,
    Ordenamiento.SELECCION: selectionsort,
}
