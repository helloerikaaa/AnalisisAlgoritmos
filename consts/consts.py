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


class Iteracion(EnumConstant):
    FIBO = "fibonacci"
    FACT = "fact"


class Recursividad(EnumConstant):
    FIBO = "fibonacci"
    FACT = "fact"
    FFT = "fft"
