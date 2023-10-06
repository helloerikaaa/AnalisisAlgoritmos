
# Divide el arreglo en mitades y los junta de manera recursiva
def merge_sort(arreglo):
    # CASO BASE
    # Verifica si la lista tiene solo un elemento
    if len(arreglo) <= 1:
        return arreglo
    
    # DIVIDIR
    # Obtiene la mitad del arreglo
    mitad = len(arreglo)//2
    # Se divide el arreglo en dos mitades
    izq = arreglo[:mitad]
    der = arreglo[mitad:]
    
    # CONQUISTAR
    # Llamada recursiva para cada mitad
    izq = merge_sort(izq)
    der = merge_sort(der)
    
    # COMBINAR
    # Se funsionan las dos mitades ordenadas
    return merge(izq, der)

def merge(izq, der):
    ordenado = []
    i_izq, i_der = 0, 0
    
    # Ciclo para comparar todos los elementos y fusionar en orden
    while i_izq < len(izq) and i_der < len(der):
        if izq[i_izq] < der[i_der]:
            ordenado.append(izq[i_izq])
            i_izq += 1
        else:
            ordenado.append(der[i_der])
            i_der += 1
    
    # Agrega los elementos restantes, si es que existen
    ordenado.extend(izq[i_izq:])
    ordenado.extend(der[i_der:])
    
    return ordenado


if __name__ == "__main__":
    arreglo = [2, 7, 6, 3, 4, 8, 1, 5]
    print("Arreglo sin ordernar: ", arreglo)
    ordenado = merge_sort(arreglo)
    print("Arreglo ordenado: ", ordenado)