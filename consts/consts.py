import enum


class EnumConstant(enum.Enum):
    def __str__(self):
        return self.value


class Busqueda(EnumConstant):
    LINEAL = "lineal_search"
    BINARIA = "binary_search"


class Ordenamiento(EnumConstant):
    BURBUJA = "bubblesort"
    BURBUJAOPT = "bubblesort_opt"
    MERGESORT = "mergesort"
    QUICKSORT = "quicksort"
    SELECCION = "selectionsort"
    INSERCION = "insertionsort"
    HEAPSORT = "heapsort"


class Iteracion(EnumConstant):
    FIBO = "fibonacci_iter"
    FACT = "factorial_iter"


class Recursividad(EnumConstant):
    FIBO = "fibonacci_rec"
    FACT = "factorial_rec"
    FFT = "fft"


class Greedy(EnumConstant):
    MONEDAS = "cambio_monedas"
    MOCHILA_FRAC = "mochila_fraccionaria"
    HUFFMAN = "huffman"
