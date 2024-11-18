import quicksort

def fontanero(t):
    t = quicksort.quicksort(t)
    tiempos_espera = [None for elem in t]
    for i in range(len(tiempos_espera)):
        suma = 0
        for j in range(i):
            suma += t[j]
        tiempos_espera[i] = suma
    te_medio = sum(tiempos_espera)/len(tiempos_espera)
    return (t, tiempos_espera, te_medio)

print(fontanero([10, 2, 3, 15, 6]))