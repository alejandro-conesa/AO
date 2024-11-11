import numpy as np
import math

def mochila_princesa(matriz, i, j):
    if i >= matriz.shape[0] or j >= matriz.shape[1]:
        return math.inf
    
    if i == matriz.shape[0]-1 and j == matriz.shape[1]-1:
        if matriz[i, j] >= 0:
            return 1
        else:
            return abs(matriz[i, j]) + 1
    
    derecha = mochila_princesa(matriz, i, j+1)
    abajo = mochila_princesa(matriz, i+1, j)

    return min(derecha, abajo)

def salvar_princesa(matriz):
    i = 0
    j = len()
    return mochila_princesa(matriz, i, j) + 1

mazmorra = np.array([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
print(salvar_princesa(mazmorra))