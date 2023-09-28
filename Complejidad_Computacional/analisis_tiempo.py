#######################################################
#                                                     #
# Este programa permite saber cuál es el tiempo       #
# de ejecución de un proceso en específico. En este   #
# caso, el proceso es sumar todos los números desde   #
# 0 hasta 1000. Entre más grande sea el número de     #
# ejecuciones, se deberá tardar más tiempo.           #
#                                                     #
#######################################################

# Librería para el tiempo
import time

# Se captura la hora en la que se empieza a ejecutar el proceso
inicio = time.time()
res = 0
# Este for se ejecuta desde 0 hasta 1000
for i in range(0, 1000):
    # Se suma todos los números desde 0 hasta 1000
    res = res + i
# Se imprime el resultado final
print(res)
# Se captura la hora en la que terminó de ejecutar el proceso
fin = time.time()
# Hace el cálculo del tiempo de ejecución de todo el proceso
tiempo_ejecutado = fin - inicio
# Imprime el tiempo de ejecución en segundos
print(tiempo_ejecutado)
