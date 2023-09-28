#######################################################
#                                                     #
# Este programa genera una gráfica donde se muestran  #
# los crecimientos asintóticos de las diferentes      #
# funciones de complejidad computacional              #
# 0 hasta 1000. Entre más grande sea el número de     #
# ejecuciones, se deberá tardar más tiempo.           #
#                                                     #
#######################################################

# Librería para creación de datos (rangos, arreglos, matrices)
import numpy as np
# Librería para hacer gráficas
import matplotlib.pyplot as plt

# Rango de 0 a 100 para generar los puntos de la gráfica
n = np.arange(0, 100)

# Cálculo de tiempo constante
tiempo_constante = np.ones_like(n)
# Cálculo de tiempo logarítmico
tiempo_logaritmico = np.log2(n)
# Cálculo de tiempo lineal
tiempo_lineal = n
# Cálculo de tiempo lineal logarítmico
tiempo_n_log_n = n * np.log2(n)
# Cálculo de tiempo cuadrático
tiempo_cuadratico = n**2

# Crear la figura con todas las gráficas
plt.figure(figsize=(10, 6))
plt.plot(n, tiempo_constante, label='O(1)', color='red')
plt.plot(n, tiempo_logaritmico, label='O(log n)', color='green')
plt.plot(n, tiempo_lineal, label='O(n)', color='blue')
plt.plot(n, tiempo_n_log_n, label='O(n log n)', color='purple')
plt.plot(n, tiempo_cuadratico, label='O(n^2)', color='orange')

# Agrega texto al eje x
plt.xlabel('Tamaño de la entrada (n)')
# Agrega texto al eje y
plt.ylabel('Tiempo de ejecución')
# Agrega el título de la gráfica
plt.title('Comparación de Órdenes Asintóticos de Análisis')
# Agrega la leyenda de la gráfica
plt.legend()
# Muestra líneas en el gráfico
plt.grid(True)

# Ajusta el eje y a los valores calculados con la función cuadrática
plt.ylim(0, max(tiempo_cuadratico))

# Mostrar el gráfico
plt.show()
