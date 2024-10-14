from statistics import mean
import time
import numpy as np
import matplotlib.pyplot as plt

def ordenacion_uno(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

tiempos_totales_1 = []
sizes = np.linspace(1, 1000, 100, dtype=int)
for size in sizes:
    tiempos = []
    for i in range(10):
        array_aleatorio = np.random.randint(0, 100, size)
        start = time.time()
        ordenacion_uno(array_aleatorio)
        end = time.time()
        tiempo_ejecucion = end - start
        tiempos.append(tiempo_ejecucion)
    tiempo_promedio = mean(tiempos)
    tiempos_totales_1.append(tiempo_promedio*100000)

n = np.linspace(1, 100, 100)
y = n**2

plt.plot(sizes, tiempos_totales_1, label='Complejidad empírica')
plt.plot(n, y, label='Complejidad teórica')
plt.xlabel('Sizes')
plt.ylabel('Tiempos')
plt.yscale('log')
plt.xscale('log')
plt.title('Complejidades')
plt.legend()
plt.savefig('ej2.pdf')
