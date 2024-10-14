# Marcos Francés Requena
# Algoritmo 1

import time
import matplotlib.pyplot as plt 
import numpy as np 

def es_dominante(matriz):
    d = len(matriz)
    for i in range(1, d):
        suma = 0
        for j in range(1, d):
            if i != j:
                suma += matriz[i][j]
        if matriz[i][j] <= suma:
            return False
    return True

def medir_tiempos(n, repeticiones):
    tiempos = []
    for _ in range(repeticiones):
        start_time = time.time()
        matriz = np.random.randint(low = 1, high = 100, size=(n,n))
        es_dominante(matriz)
        end_time = time.time()
        result_time = end_time - start_time
        tiempos.append(result_time)
    return np.mean(tiempos)


repeticiones = 100
factor = 10000000
max_val = 100

n_values = np.linspace(1, max_val, repeticiones, dtype = int)

teorica = [(n**2)/factor for n in n_values]
empirica = [medir_tiempos(n, repeticiones) for n in n_values]

plt.plot(n_values, teorica, label = "Complejidad teórica", color = "blue")
plt.legend()
plt.title("Complejidad teórica primer algoritmo")
plt.xlabel("Tamaño de la matriz")
plt.ylabel("Tiempo de ejecución (s)")
plt.savefig("Ej1_teorica.pdf")

plt.clf()

plt.plot(n_values, empirica, label = "Complejidad empírica", color = "red")
plt.legend()
plt.title("Complejidad empírica primer algoritmo")
plt.xlabel("Tamaño de la matriz")
plt.ylabel("Tiempo de ejecución (s)")
plt.savefig("Ej1_empirica.pdf")


plt.clf()

plt.plot(n_values, teorica, label = "Complejidad teórica", color = "blue")
plt.plot(n_values, empirica, label = "Complejidad empírica", color = "red")
plt.legend()
plt.title("Complejidades primer algoritmo")
plt.xlabel("Tamaño de la matriz")
plt.ylabel("Tiempo de ejecución (s)")
plt.savefig("Ej1.pdf")
