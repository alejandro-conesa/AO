import numpy as np
import matplotlib.pyplot as plt
import time

factor = 1000000
num_ejecuciones = 100
max_num = 10000

def busqueda_binaria(arr, target):
    l = 0
    r = len(arr)-1
    while l <= r:
        m = int((l+r)/2)
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            return m
    return -1

def get_time(arr, target):
    start = time.time()
    busqueda_binaria(arr, target)
    end = time.time()
    return end - start

sizes = np.linspace(1, max_num, num_ejecuciones, dtype=int)
lista_tiempos_random = []
lista_tiempos_mejor = []
lista_tiempos_peor = []
for size in sizes:
    tiempo_random = 0
    tiempo_mejor = 0
    tiempo_peor = 0
    for _ in range(num_ejecuciones):
        array = np.linspace(1, max_num, size, dtype=int)
        tiempo_random += get_time(array, np.random.randint(low=1, high=max_num))
        tiempo_mejor += get_time(array, array[int((size-1)/2)])
        tiempo_peor += get_time(array, -1)
    lista_tiempos_random.append(tiempo_random/num_ejecuciones)
    lista_tiempos_mejor.append(tiempo_mejor/num_ejecuciones)
    lista_tiempos_peor.append(tiempo_peor/num_ejecuciones)

plt.plot(sizes, lista_tiempos_random, label='Complejidad empírica num aleatorio')
plt.plot(sizes, lista_tiempos_mejor, label='Complejidad empírica mejor caso')
plt.plot(sizes, lista_tiempos_peor, label='Complejidad empírica peor caso')

n = np.linspace(1, max_num, num_ejecuciones)
y = np.log(n)/factor

plt.plot(n, y, label='Complejidad teórica')

plt.xlabel('Sizes')
plt.ylabel('Tiempos')
plt.title('Complejidades')
plt.legend()
plt.savefig('ej4.pdf')

    
