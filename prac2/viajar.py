import math

def viajar(costes, volumenes, S, i = 0):
    if i >= len(costes):
        if S == 0:
            return 0
        else:
            return math.inf
    
    pos1 = viajar(costes, volumenes, S-volumenes[i], i+1) + costes[i]
    pos2 = viajar(costes, volumenes, S, i+1)

    return min(pos1, pos2)

print(viajar([4, 3, 2, 5, 1], [3, 2, 4, 5 ,1], 10))
