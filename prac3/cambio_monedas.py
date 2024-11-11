import quicksort

def cambiar_monedas(M, C):
    C = list(reversed(quicksort.quicksort(C))) # ordenamos C en orden descendente
    respuesta = {}

    suma = 0
    for moneda in C:
        respuesta[f'{moneda}'] = (M-suma)//moneda
        suma += moneda*respuesta[f'{moneda}']
    
    if suma == M:
        return respuesta
    else:
        return "El problema no tiene solución"


    

                

if __name__ == "__main__":
    print(cambiar_monedas(1.35, [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]))
