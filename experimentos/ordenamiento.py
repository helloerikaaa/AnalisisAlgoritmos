import time
import argparse
from typing import List
from loguru import logger

from pipeline import pipeline
from utils.graficar import graficar
from consts.consts import Ordenamiento
from utils.utils import generar_arreglo


def crear_experimento(n: int, algoritmo: str) -> float:
    logger.info(f"Ejecutando el algortimo {algoritmo}")
    datos = generar_arreglo(n)
    start_time = time.time()
    pipeline.ALGORITMOS[Ordenamiento(algoritmo)](datos)
    end_time = time.time()
    return end_time - start_time


def ejecutar(algoritmo: str, entradas: List) -> None:
    tiempos_ejecucion = [crear_experimento(n, algoritmo) for n in entradas]

    for i in range(len(entradas)):
        logger.info(
            f"Tamaño de la entrada: {entradas[i]}, Tiempo de Ejecución: {tiempos_ejecucion[i]} segundos"
        )
    graficar(entradas, tiempos_ejecucion)


def main(algoritmo: str) -> None:
    entradas = [100, 1000, 10000, 100000, 1000000]
    ejecutar(algoritmo, entradas)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-a', '--algoritmo', help='Nombre del algoritmo de ordenamiento')
    args = parser.parse_args()

    main(args.algoritmo)
