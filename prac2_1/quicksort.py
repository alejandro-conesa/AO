import numpy as np

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivote = array[0]
        izq = []
        der = []
        for i in range(1, len(array)):
            if array[i] >= pivote:
                der.append(array[i])
            else:
                izq.append(array[i])
        izq.append(pivote)
        return quicksort(izq) + quicksort(der)
    

print(quicksort([2, 5, 3, 3, 6, 10, 9, 1]))
        