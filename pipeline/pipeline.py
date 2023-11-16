from consts.consts import Ordenamiento, Recursividad, Iteracion, Busqueda
from algoritmos.ordenamiento.heapsort import heapsort
from algoritmos.ordenamiento.mergesort import mergesort
from algoritmos.ordenamiento.quicksort import quicksort
from algoritmos.ordenamiento.bubblesort import bubblesort
from algoritmos.ordenamiento.insertionsort import insertionsort
from algoritmos.ordenamiento.selectionsort import selectionsort
from algoritmos.recursividad.factorial_recursivo import factorial
from algoritmos.recursividad.fibonacci_recursivo import fibonacci
from algoritmos.iterativos.factorial_iterativo import factorial_iterativo
from algoritmos.iterativos.fibonacci_iterativo import fibonacci_iterativo
from algoritmos.busqueda.busqueda_binaria import busqueda_binaria
from algoritmos.busqueda.busqueda_lineal import busqueda_lineal

ALGORITMOS = {
    Busqueda.LINEAL: busqueda_lineal,
    Busqueda.BINARIA: busqueda_binaria,
    Ordenamiento.MERGESORT: mergesort,
    Ordenamiento.BURBUJA: bubblesort,
    Ordenamiento.QUICKSORT: quicksort,
    Ordenamiento.INSERCION: insertionsort,
    Ordenamiento.SELECCION: selectionsort,
    Ordenamiento.HEAPSORT: heapsort,
    Recursividad.FACT: factorial,
    Recursividad.FIBO: fibonacci,
    Iteracion.FACT: factorial_iterativo,
    Iteracion.FIBO: fibonacci_iterativo,
}
