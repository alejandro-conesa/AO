def mochila(n, W, v, w):
    if n == -1 or W == 0:
        return 0
    
    if w[n] > W:
        return mochila(n-1, W, v, w)
    else:
        m1 = mochila(n-1, W, v, w)
        m2 = v[n] + mochila(n-1, W-w[n], v, w)
        return max(m1, m2)

def director_deportivo(valoraciones:list, precios:list, G:int) -> int:
    n = len(valoraciones) - 1
    return mochila(n, G, valoraciones, precios)
    
    
print(director_deportivo([6, 1, 3, 8], [950, 2400, 500, 2000], 3000))
