import numpy as np
import matplotlib.pyplot as plt
import time

# Mejor caso O(n log (n))
# Peor caso O(n^2)
def ordena(arr):
    izq = []
    der = []
    if len(arr) == 1:
        return arr
    else:
        pivote = arr[0]
        for x in range(1, len(arr)):
            if arr[x] <= pivote:
                izq.append(arr[x])
            if arr[x] > pivote:
                der.append(arr[x])
    
    izq.append(pivote)
    return ordena(izq) + ordena(der)

def get_time(arr):
    start = time.time()
    ordena(arr)
    end = time.time()
    return end - start


factor1 = 100_000_000_000_000
factor2 = 100_000_000_000
num_ejecuciones = 100
max_num = 10000

tiempo_medio = []
tiempo_peor = []
sizes = np.linspace(1, max_num, num_ejecuciones, dtype=int)
for size in sizes:
    sub_tiempo_medio = 0
    sub_tiempo_peor = 0
    for _ in range(num_ejecuciones):
        array_medio = np.random.randint(low=1, high=100, size=(1,size))
        array_peor = np.random.randint(low=1, high=100, size=(1,size))
        array_peor.sort()
        sub_tiempo_medio += get_time(array_medio)
        sub_tiempo_peor += get_time(array_peor)
    tiempo_medio.append(sub_tiempo_medio/num_ejecuciones)
    tiempo_peor.append(sub_tiempo_peor/num_ejecuciones)

plt.plot(sizes, tiempo_medio, label='Tiempo de ejecución medio')
plt.plot(sizes, tiempo_peor, label='Tiempo de ejecución peor caso')

n_peor = np.linspace(1, max_num, num_ejecuciones)
y_peor = (n_peor**2)/factor1
plt.plot(n_peor, y_peor, label='Complejidad teórica peor caso')

n_mejor = np.linspace(1, max_num, num_ejecuciones)
y_mejor = (n_mejor*np.log(n_mejor))/factor2
plt.plot(n_mejor, y_mejor, label='Complejidad teórica mejor caso')

plt.legend()
plt.title('Complejidad función ordenación')
plt.xlabel('Tamaño')
plt.ylabel('Tiempo')
plt.savefig('ej1_3_2.pdf')

