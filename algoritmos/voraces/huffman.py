import heapq
from collections import defaultdict, Counter

class NodoHuffman:
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia


def construir_arbol_huffman(frecuencias):
    heap = [NodoHuffman(simbolo, frecuencia) for simbolo, frecuencia in frecuencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        nodo_izquierda = heapq.heappop(heap)
        nodo_derecha = heapq.heappop(heap)

        nodo_padre = NodoHuffman(None, nodo_izquierda.frecuencia + nodo_derecha.frecuencia)
        nodo_padre.izquierda = nodo_izquierda
        nodo_padre.derecha = nodo_derecha

        heapq.heappush(heap, nodo_padre)

    return heap[0]

def generar_codigos_huffman(arbol, codigo_actual="", diccionario_codigos=None):
    if diccionario_codigos is None:
        diccionario_codigos = {}

    if arbol.simbolo is not None:
        diccionario_codigos[arbol.simbolo] = codigo_actual
    if arbol.izquierda is not None:
        generar_codigos_huffman(arbol.izquierda, codigo_actual + "0", diccionario_codigos)
    if arbol.derecha is not None:
        generar_codigos_huffman(arbol.derecha, codigo_actual + "1", diccionario_codigos)

    return diccionario_codigos


def codificar(texto, diccionario_codigos):
    return ''.join(diccionario_codigos[simbolo] for simbolo in texto)


def decodificar(codigo, arbol):
    resultado = []
    nodo_actual = arbol

    for bit in codigo:
        if bit == '0':
            nodo_actual = nodo_actual.izquierda
        else:
            nodo_actual = nodo_actual.derecha

        if nodo_actual.simbolo is not None:
            resultado.append(nodo_actual.simbolo)
            nodo_actual = arbol

    return ''.join(resultado)
