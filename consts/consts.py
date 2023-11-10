import enum


class EnumConstant(enum.Enum):
    def __str__(self):
        return self.value


76


class Busqueda(EnumConstant):
    LINEAL = "lineal"
    BINARIA = "binaria"


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
