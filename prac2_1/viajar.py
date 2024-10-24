import math
import numpy as np

#recursiva
def viajar(costes, volumenes, S):
    n = len(costes)
    def mochila(c, v, s, i):
        if i == 0:
            if s == 0:
                return 0
            else:
                return math.inf
            
        pos1 = mochila(c, v, s-v[i-1], i-1) + c[i-1]
        pos2 = mochila(c, v, s, i-1)
        return min(pos1, pos2)
    
    return mochila(costes, volumenes, S, n)

#memo
def mochila_memo(c, v, s, i, tab):
    if tab[i, s] != -1:
        return tab[i, s] 

    if i == 0:
        if s == 0:
            tab[i, s] = 0
            return tab[i, s]
        else:
            tab[i, s] = 10**10
            return tab[i, s]
    
    pos1 = mochila_memo(c, v, s-v[i-1], i-1, tab) + c[i-1]
    pos2 = mochila_memo(c, v, s, i-1, tab)

    tab[i, s] = min(pos1, pos2)
    return tab[i, s]

def viajar_memo(costes, volumenes, S):
    n = len(costes)
    pd = np.full((n+1, S+1), -1)
    return mochila_memo(costes, volumenes, S, n, pd)

#tabulacion
def viajar_tab(costes, volumenes, S):
    n = len(costes)
    pd = np.full((n+1, S+1), -1)
    pd[0, :] = 10**10
    pd[0, 0] = 0
    for i in range(1, n+1):
        for j in range(0, S+1):
            pos1 = pd[i-1, j-volumenes[i-1]] + costes[i-1]
            pos2 = pd[i-1, j]
            pd[i, j] = min(pos1, pos2)
    
    return pd[n, S]

print(viajar_tab([4, 3, 2, 5, 1], [3, 2, 4, 5 ,1], 10))
