import time
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt

def ordenacion_uno(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def ordenacion_dos(arr):
    izq = []
    der = []
    if len(arr) <= 1:
        return arr
    pivote = arr[0]
    for i in range(1, len(arr)):
        if arr[i] <= pivote:
            izq.append(arr[i])
        if arr[i] > pivote:
            der.append(arr[i])
    return ordenacion_dos(izq) + [pivote] + ordenacion_dos(der)


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
    tiempos_totales_1.append(tiempo_promedio)
tiempos_totales_2 = []
sizes = np.linspace(1, 1000, 100, dtype=int)
for size in sizes:
    tiempos = []
    for i in range(10):
        array_aleatorio = np.random.randint(0, 100, size)
        start = time.time()
        ordenacion_dos(array_aleatorio)
        end = time.time()
        tiempo_ejecucion = end - start
        tiempos.append(tiempo_ejecucion)
    tiempo_promedio = mean(tiempos)
    tiempos_totales_2.append(tiempo_promedio)
print(tiempos_totales_1)
print(tiempos_totales_2)

plt.plot(sizes, tiempos_totales_1, label='Tiempos 1')
plt.plot(sizes, tiempos_totales_2, label='Tiempos 2')
plt.xlabel('Sizes')
plt.ylabel('Tiempos métodos')
plt.title('Método 1')
plt.legend()
plt.savefig('metodos.pdf')
plt.close()



