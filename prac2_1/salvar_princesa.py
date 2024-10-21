import math
import numpy as np

def salvar_princesa(mazmorra):
    i = 0
    j = 0
    def salvar_princesa_custom(mazmorra, i, j):
        if i == mazmorra.shape[0] - 1 and j == mazmorra.shape[1] -1:
            return max(1, 1 - mazmorra[i, j])
        
        if i > mazmorra.shape[0] - 1 or j > mazmorra.shape[1] -1:
            return math.inf
        
        abajo = salvar_princesa_custom(mazmorra, i+1, j)
        derecha = salvar_princesa_custom(mazmorra, i, j+1)
        vida = max(1, 1 - mazmorra[i, j])

        return min(abajo, derecha) + vida


    return salvar_princesa_custom(mazmorra, i, j)


mazmorra = np.array([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
print(salvar_princesa(mazmorra))