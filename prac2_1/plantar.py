import math

def plantar(matriz: list, i = 0, j = -1) -> int:
    if i == len(matriz) - 1 and j == -len(matriz[i]): #con numpy se saca mas facil
        return 0
    
    if i >= len(matriz) or j < -len(matriz[i]) or matriz[i][j] == 1:
        return math.inf

    pos1 = plantar(matriz, i+1, j)
    pos2 = plantar(matriz, i, j-1) 
    pos3 = plantar(matriz, i+1, j-1)

    return min(pos1, pos2, pos3) + 1

print(plantar([[0, 0, 0, 0],[0, 1, 1, 0],[0, 1, 0, 0]]))