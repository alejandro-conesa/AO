import numpy as np

def planear_gira(C, R, entradas):
    dias = len(entradas)
    def mochila(d, c, tickets, r):
        if C == 0 or d <= 0:
            return 0
        
        pos1 = mochila(d-r, c-1, tickets, r) + tickets[d-1]
        pos2 = mochila(d-1, c, tickets, r)

        return max(pos1, pos2)
    
    return mochila(dias, C, entradas, R)

def planear_gira_memo(C, R, entradas):
    d = len(entradas)
    pd = np.full((d+1, C+1), -1)

    def pgm(d_pgm, C_pgm, R_pgm, entradas_pgm, pd_pgm):
        if pd_pgm[d_pgm, C_pgm] != -1:
            return pd_pgm[d_pgm, C_pgm]
        
        if C_pgm == 0 or d_pgm <= 0:
            pd_pgm[d_pgm, C_pgm] = 0 
            return pd_pgm[d_pgm, C_pgm]
        
        pos1 = pgm(d_pgm-R_pgm, C_pgm-1, R_pgm, entradas_pgm, pd_pgm) + entradas_pgm[d-1]
        pos2 = pgm(d_pgm-1, C_pgm, R_pgm, entradas_pgm, pd_pgm)

        pd_pgm[d_pgm, C_pgm] = max(pos1, pos2)
        return pd_pgm[d_pgm, C_pgm]

    return pgm(d, C, R, entradas, pd)

def planear_gira_tab(C, R, entradas):
    d = len(entradas)
    pd = np.full((d+1, C+1), -1)
    pd[0, :] = 0
    pd[:, 0] = 0
    for i in range(1, d+1):
        for j in range(1, C+1):
            if i-R < 0:
                pos1 = pd[0, j-1] + entradas[i-1]
            else:
                pos1 = pd[i-R, j-1] + entradas[i-1]
            pos2 = pd[i-1, j]
            pd[i, j] = max(pos1, pos2)

    return pd

def recuperar_soluciones(C, R, entradas, pd):
    i = len(entradas)
    j = C
    solucion = []
    while i > 0 and j > 0:
        if pd[i][j] != pd[i-1][j]:
            solucion.append(i-1)
            j -= 1
            i -= R
        else:
            i -= 1
    return list(reversed(solucion))

tabla = planear_gira_tab(3, 3, [3000, 6000, 7000, 8000, 9000])
print(tabla)
sol = recuperar_soluciones(3, 3, [3000, 6000, 7000, 8000, 9000], tabla)
print(sol)
    

    

    
    

    

    

