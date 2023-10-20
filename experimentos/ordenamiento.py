import time
from pipeline import pipeline
from utils.graficar import graficar
from utils.utils import generar_arreglo
from consts.consts import Ordenamiento

def ejecutar_experimento(n: int, algoritmo: str):
    datos = generar_arreglo(n)
    start_time = time.time()
    pipeline.ALGORITMOS[Ordenamiento(algoritmo)](datos)
    end_time = time.time()
    return end_time - start_time

def ejecutar_merge():
    entradas = [100, 1000, 10000, 100000, 1000000]
    tiempos_ejecucion = [ejecutar_experimento(n, "mergesort") for n in entradas]

    for i in range(len(entradas)):
        print(
            f"Tamaño de la entrada: {entradas[i]}, Tiempo de Ejecución: {tiempos_ejecucion[i]} segundos"
        )
    graficar(entradas, tiempos_ejecucion)

def main():
    ejecutar_merge()


if __name__ == "__main__":
    main()
