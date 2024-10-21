def planear_gira(C, R, entradas, d = 0):
    if C == 0 or d >= len(entradas):
        return 0
    
    pos1 = planear_gira(C-1, R, entradas, d+R) + entradas[d]
    pos2 = planear_gira(C, R, entradas, d+1)

    return max(pos1, pos2)

print(planear_gira(3, 3, [3000, 6000, 7000, 8000, 9000]))
    

    

    
    

    

    

