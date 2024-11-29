import numpy as np

def laberinto(matriz):
    solucion = []
    posicion = [0,0]
    contador = 0
    max_contador = len(matriz)*len(matriz[0])
    # en el peor caso, hay tantos movimientos como casillas
    # si se llegan al máximo de casillas y no se ha salido del bucle, la función acaba
    while posicion != [len(matriz)-1, len(matriz[0])-1] and contador < max_contador:
        print(posicion)
        if (matriz[posicion[0]][posicion[1]+1] if posicion[1] + 1 < len(matriz[0]) else 0) == 1:
            solucion.append(posicion.copy())
            posicion[1] += 1
        elif (matriz[posicion[0]+1][posicion[1]] if posicion[0]+1 < len(matriz) else 0) == 1:
            solucion.append(posicion.copy())
            posicion[0] += 1
        elif (matriz[posicion[0]][posicion[1]-1] if posicion[1]-1 > 0 else 0) == 1:
            solucion.append(posicion.copy())
            posicion[1] -= 1
        elif (matriz[posicion[0]-1][posicion[1]] if posicion[0] - 1 > 0 else 0) == 1:
            solucion.append(posicion.copy())
            posicion[0] -= 1
        else:
            break
        contador += 1
    
    solucion.append(posicion)
    
    if solucion[-1] != [len(matriz)-1, len(matriz[0])-1]:
        return [-1]
    else:
        return solucion

print(laberinto([[1, 0, 1, 1, 1],
                 [1, 0, 1, 0, 1], 
                 [1, 0, 1, 0, 1], 
                 [1, 0, 1, 0, 1], 
                 [1, 1, 1, 0, 1]]))