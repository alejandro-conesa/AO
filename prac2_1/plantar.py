import math
import numpy as np

def mochila(matriz, i, j):
    if i == len(matriz) - 1 and j == -len(matriz[i]): #con numpy se saca mas facil
        return 0

    if i >= len(matriz) or j < -len(matriz[i]) or matriz[i][j] == 1:
        return math.inf
    
    pos1 = mochila(matriz, i+1, j)
    pos2 = mochila(matriz, i, j-1) 
    pos3 = mochila(matriz, i+1, j-1)
    return min(pos1, pos2, pos3) + 1

def plantar(matriz: list) -> int:
    i = 0
    j = -1
    return mochila(matriz, i, j)

def mochila_memo(matriz, i, j, pd):
    if i >= matriz.shape[0] or j < -matriz.shape[1]:
        return math.inf
    
    if pd[i, j] != -2:
        return pd[i, j]
    
    if i == matriz.shape[0] - 1 and j == -matriz.shape[1]:
        pd[i, j] = 0
        return pd[i, j]
    
    abajo = mochila_memo(matriz, i+1, j, pd)
    izquierda = mochila_memo(matriz, i, j-1, pd)
    diagonal = mochila_memo(matriz, i+1, j-1, pd)

    pd[i, j] = min(abajo, izquierda, diagonal) + 1
    return pd[i, j]
    
def plantar_memo(matriz):
    i = 0
    j = -1
    pd = np.full((matriz.shape[0]+1, matriz.shape[1]+1), -2)
    return mochila_memo(matriz, i, j, pd) + 1

def plantar_tab(matriz):
    i = matriz.shape[0]
    j = 0
    pd = np.full((matriz.shape[0], matriz.shape[1]), -1)
    pd[matriz.shape[0]-1, 0] = 0
    for a in range(matriz.shape[0]):
        for b in range(matriz.shape[1]):
            if matriz[a, b] == 1:
                pd[a, b] = 10^10

    for a in range(i-2, -1, -1):
        for b in range(1, j):
            arriba = pd[i-1, j]
            diagonal = pd[i-1, j+1]
            derecha = pd[i, j+1]
            pd[i, j] = min(arriba, diagonal, derecha) + 1

    return pd[0, -1]

matriz = np.array([[0, 0, 0, 0],[0, 1, 1, 0],[0, 1, 0, 0]])
print(plantar(matriz))
print(plantar_memo(matriz))
print(plantar_tab(matriz))