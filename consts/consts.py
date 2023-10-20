import enum


class EnumConstant(enum.Enum):
    def __str__(self):
        return self.value


class Busqueda(EnumConstant):
    LINEAL = "lineal"
    BINARIA = "binaria"


class Ordenamiento(EnumConstant):
    BURBUJA = "burbuja"
    BURBUJAOPT = "burbuja_optimizada"
    MERGESORT = "mergesort"
    QUICKSORT = "quicksort"


class Iteracion(EnumConstant):
    FIBO = "fibonacci"
    FACT = "fact"


class Recursividad(EnumConstant):
    FIBO = "fibonacci"
    FACT = "fact"
    FFT = "fft"
