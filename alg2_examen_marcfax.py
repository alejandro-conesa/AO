# Marcos Francés Requena
# Algoritmo 2

import time
import matplotlib.pyplot as plt 
import numpy as np 

def producto_recursivo(arr):
    if len(arr) == 1:
        return arr[0]
    medio = int(len(arr)/2)
    izq = producto_recursivo(arr[:medio])
    drch = producto_recursivo(arr[medio:])
    return izq * drch


def medir_tiempos(n, repeticiones):
    tiempos = []
    for _ in range(repeticiones):
        start_time = time.time()
        arr = np.random.randint(low = 1, high = max_num, size=(n,n))
        producto_recursivo(arr)
        end_time = time.time()
        result_time = end_time - start_time
        tiempos.append(result_time)
    return np.mean(tiempos) 

max_num = 1000
repeticiones = 100
factor = 1000000

n_values = np.linspace(1, max_num, repeticiones, dtype = int)

empirica = [medir_tiempos(n, repeticiones) for n in n_values]
teorica = [(n*np.log(n)) / factor for n in n_values]

plt.plot(n_values, empirica, label = "Complejidad empírica", color = "blue")
plt.plot(n_values, teorica, label = "Complejidad teórica", color = "red")
plt.title("Comparación complejidades segundo algoritmo")
plt.legend()
plt.xlabel("Tamaño del array")
plt.ylabel("Tiempo de ejecución (s)")
plt.savefig("Ej2.pdf")

plt.clf()

plt.plot(n_values, empirica, label = "Complejidad empírica", color = "blue")
plt.title("Complejidad empírica segundo algoritmo")
plt.legend()
plt.xlabel("Tamaño del array")
plt.ylabel("Tiempo de ejecución (s)")
plt.savefig("Ej2_empirica.pdf")

plt.clf()

plt.plot(n_values, teorica, label = "Complejidad teórica", color = "red")
plt.title("Complejidad teórica segundo algoritmo")
plt.legend()
plt.xlabel("Tamaño del array")
plt.ylabel("Tiempo de ejecución (s)")
plt.savefig("Ej2_teorica.pdf")
