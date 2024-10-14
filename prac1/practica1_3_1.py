import numpy as np
import matplotlib.pyplot as plt
import time

def g(n):
    if n == 1:
        return 1
    
    g(n-1)
    g(n-1)

def get_time(num):
    start = time.time()
    g(num)
    end = time.time()
    return end - start

factor = 1_000_000
num_ejecuciones = 10
max_num = 20

sizes = np.linspace(1, max_num, num_ejecuciones, dtype=int)
tiempo = []
for size in sizes:
    sub_tiempo = 0
    for _ in range(num_ejecuciones):
        sub_tiempo += get_time(size)
    tiempo.append(sub_tiempo/num_ejecuciones)

plt.plot(sizes, tiempo, label='Tiempo')

n = np.linspace(1, max_num, num_ejecuciones)
y = (2**n)/factor
plt.plot(n, y, label='Complejidad teórica')

plt.title('Complejidad función G(n)')
plt.ylabel('Tiempo')
plt.xlabel('n')
plt.legend()
plt.savefig('ej1_3_1.pdf')