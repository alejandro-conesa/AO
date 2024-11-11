import quicksort

def fontanero(t):
    t = quicksort.quicksort(t)
    tiempos_espera = [None for elem in t]
    for i in range(len(tiempos_espera)):
        suma = 0
        for j in range(i):
            suma += t[j]
        tiempos_espera[i] = suma
    return tiempos_espera