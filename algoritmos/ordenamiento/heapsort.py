import random
import time
import matplotlib.pyplot as plt


def heapify(datos, n, i):
    mas_grande = i 
    izq = 2 * i + 1
    der = 2 * i + 2

    
    if izq < n and datos[izq] > datos[mas_grande]:
        mas_grande = izq

    
    if der < n and datos[der] > datos[mas_grande]:
        mas_grande = der

    
    if mas_grande != i:
        datos[i], datos[mas_grande] = datos[mas_grande], datos[i]

        
        heapify(datos, n, mas_grande)

def heapsort(datos):
    n = len(datos)

    
    for i in range(n // 2 - 1, -1, -1):
        heapify(datos, n, i)

    
    for i in range(n - 1, 0, -1):
        datos[i], datos[0] = datos[0], datos[i]
        heapify(datos, i, 0)


def heapsort_timing_analysis():
    input_sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
    execution_times = []

    for size in input_sizes:
        datos = [random.randint(1, 1000) for _ in range(size)]

        start_time = time.time()
        heapsort(datos)
        end_time = time.time()

        execution_time = end_time - start_time
        execution_times.append(execution_time)

    return input_sizes, execution_times

def plot_complexity(input_sizes, execution_times):
    plt.figure(figsize=(8, 6))
    plt.plot(input_sizes, execution_times, marker='o', linestyle='-')
    plt.title('Heapsort Time Complexity Analysis')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    input_sizes, execution_times = heapsort_timing_analysis()
    plot_complexity(input_sizes, execution_times)
