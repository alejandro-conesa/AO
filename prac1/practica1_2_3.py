import numpy as np
import matplotlib.pyplot as plt
import statistics
import time

def producto_matrices_cuadradas(A, B):
    n = A.shape[0]
    C = np.zeros(shape=(n, n))
    for i in range(0, n):
        for j in range(0, n):
            suma = 0
            for k in range(0, n):
                suma = suma + A[i, k] * B[k, j]
            C[i, j] = suma
    return C

tiempos_totales = []
sizes = np.linspace(1, 100, 100, dtype=int)
for size in sizes:
    tiempos = []
    for i in range(10):
        array_aleatorio_1 = np.random.randint(0, 100, (size, size))
        array_aleatorio_2 = np.random.randint(0, 100, (size, size))
        start = time.time()
        producto_matrices_cuadradas(array_aleatorio_1, array_aleatorio_2)
        end = time.time()
        tiempo_ejecucion = end - start
        tiempos.append(tiempo_ejecucion)
    tiempo_promedio = statistics.mean(tiempos)
    tiempos_totales.append(tiempo_promedio*10000)

n = np.linspace(1, 100, 100)
y = n**3

plt.plot(sizes, tiempos_totales, label='Complejidad empírica')
plt.plot(n, y, label='Complejidad teórica')
plt.xlabel('Sizes')
plt.ylabel('Tiempos')
plt.yscale('log')
plt.xscale('log')
plt.title('Complejidades')
plt.legend()
plt.savefig('ej3.pdf')