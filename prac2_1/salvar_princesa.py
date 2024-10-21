import math
import numpy as np

def salvar_princesa(mazmorra):
    i = 0
    j = 0
    def salvar_princesa_custom(mazmorra, i, j):
        if i == mazmorra.shape[0] - 1 and j == mazmorra.shape[1] -1:
            return max(1, 1 - mazmorra[i, j])
        
        if i >= mazmorra.shape[0] - 1 or j >= mazmorra.shape[1] -1:
            return math.inf
        
        


    return salvar_princesa_custom(mazmorra, i, j)


mazmorra = np.array([[-7, -2], [1,]])
print(salvar_princesa(mazmorra))