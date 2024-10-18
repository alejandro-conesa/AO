def mezclar(arrayizq, arrayder):
    i = 0
    d = 0
    resultado = []
    while i < len(arrayizq) and d < len(arrayder):
        if arrayizq[i] <= arrayder[d]:
            resultado.append(arrayizq[i])
            i += 1
        else:
            resultado.append(arrayder[d])
            d += 1
        
    for elem in range(i, len(arrayizq)):
        resultado.append(arrayizq[elem])
    for elem in range(d, len(arrayder)):
        resultado.append(arrayder[elem])
    return resultado

def mergesort(array):
    if len(array) <= 1:
        return array
    mitad = int(len(array)/2)
    arrayizq = mergesort(array[:mitad])
    arrayder = mergesort(array[mitad:])

    array = mezclar(arrayizq, arrayder)
    return array

print(mergesort([1, 9, 2, 0, 65, 3, 7]))