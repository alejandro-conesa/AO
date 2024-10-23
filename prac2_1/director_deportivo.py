import numpy as np

#no pd
def mochila(n, W, v, w):
    if n == 0 or W == 0:
        return 0
    
    if w[n-1] > W:
        return mochila(n-1, W, v, w)
    else:
        m1 = mochila(n-1, W, v, w)
        m2 = v[n-1] + mochila(n-1, W-w[n-1], v, w)
        return max(m1, m2)

def director_deportivo(valoraciones:list, precios:list, G:int) -> int:
    n = len(valoraciones)
    return mochila(n, G, valoraciones, precios)

#memoizacion
def mochila_memoizacion(n, W, v, w, pd):
    if pd[n, W] != -1:
        return pd[n, W]
    
    if n == 0 or W == 0:
        pd[n, W] = 0
        return pd[n, W]
    
    if w[n-1] > W:
        pd[n, W] = mochila_memoizacion(n-1, W, v, w, pd)
        return pd[n, W]
    else:
        m1 = mochila_memoizacion(n-1, W, v, w, pd)
        m2 = v[n-1] + mochila_memoizacion(n-1, W-w[n-1], v, w, pd)
        pd[n, W] = max(m1, m2)
        return pd[n, W]
    
def director_memoizacion(valoraciones, precios, G):
    pd = np.full((len(valoraciones)+1, G+1), -1)
    return(mochila_memoizacion(len(valoraciones), G, valoraciones, precios, pd))

#tabulacion
def director_tabulacion(valoraciones, precios, G):
    n = len(valoraciones)
    pd = np.full((n+1, G+1), -1)
    pd[0, :] = 0
    pd[:, 0] = 0
    for i in range(1, n+1):
        for j in range(1, G+1):
            if precios[i-1] > j:
                pd[i, j] = pd[i-1, j]
            else:
                pd[i, j] = max(pd[i-1, j], valoraciones[i-1]+pd[i-1, j-precios[i-1]])
    
    return pd

#recuperar soluciones
def recuperar_soluciones(n, W, v, w, pd):
    i = n
    j = W
    solucion = []
    while i > 0 and j > 0:
        if pd[i][j] != pd[i-1][j]:
            solucion.append(i-1)
            j -= w[i-1]
        i -= 1
    return np.flip(solucion)
    
pd = director_tabulacion([6, 1, 3, 8], [950, 2400, 500, 2000], 3000)
print(pd[4, 3000])
sol = recuperar_soluciones(4, 3000, [6, 1, 3, 8], [950, 2400, 500, 2000], pd)
print(sol)
