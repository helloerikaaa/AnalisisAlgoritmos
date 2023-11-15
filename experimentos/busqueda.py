import time
import argparse
from typing import List
from loguru import logger

from pipeline import pipeline
from utils.graficar import graficar
from consts.consts import Busqueda
from utils.utils import generar_arreglo


def crear_experimento(n: int, algoritmo: str, numero: int) -> float:
    logger.info(f"Ejecutando el algortimo {algoritmo} con n={n}")
    datos = generar_arreglo(n)
    if algoritmo == "binary_search":
        datos = sorted(datos)
        numero = int(numero)
    start_time = time.time()
    pipeline.ALGORITMOS[Busqueda(algoritmo)](datos, numero)
    end_time = time.time()
    return end_time - start_time


def ejecutar(algoritmo: str, entradas: List, numero: int) -> None:
    tiempos_ejecucion = [crear_experimento(n, algoritmo, numero) for n in entradas]

    for i in range(len(entradas)):
        logger.info(
            f"Tamaño de la entrada: {entradas[i]}, Tiempo de Ejecución: {tiempos_ejecucion[i]} segundos"
        )
    graficar(entradas, tiempos_ejecucion)


def main(algoritmo: str, numero: int) -> None:
    entradas = [100, 1000, 10000, 100000, 1000000]
    ejecutar(algoritmo, entradas, numero)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-a", "--algoritmo", help="Nombre del algoritmo de ordenamiento"
    )
    parser.add_argument("-n", "--numero", help="Número a buscar")
    args = parser.parse_args()

    main(args.algoritmo, args.numero)
