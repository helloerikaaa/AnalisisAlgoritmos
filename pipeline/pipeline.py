from consts.consts import Ordenamiento, Recursividad
from algoritmos.ordenamiento.heapsort import heapsort
from algoritmos.ordenamiento.mergesort import mergesort
from algoritmos.ordenamiento.quicksort import quicksort
from algoritmos.ordenamiento.bubblesort import bubblesort
from algoritmos.ordenamiento.insertionsort import insertionsort
from algoritmos.ordenamiento.selectionsort import selectionsort
from algoritmos.recursividad.factorial_recursivo import factorial
from algoritmos.recursividad.fibonacci_recursivo import fibonacci

ALGORITMOS = {
    Ordenamiento.MERGESORT: mergesort,
    Ordenamiento.BURBUJA: bubblesort,
    Ordenamiento.QUICKSORT: quicksort,
    Ordenamiento.INSERCION: insertionsort,
    Ordenamiento.SELECCION: selectionsort,
    Ordenamiento.HEAPSORT: heapsort,
    Recursividad.FACT: factorial,
    Recursividad.FIBO: fibonacci,
}
