import quicksort
import numpy as np

def colorear_grafos(matriz_adyacencia: np.array) -> int:
    num_colores = 0
    nodo_color = {}
    num_conexiones = {}
    contador = 0
    for fila in matriz_adyacencia:
        num_conexiones[f'{contador}'] = int(sum(fila)) 
        # los colores son están representados por números       
        nodo_color[f'{int(nodo)}'] = 0
        contador += 1
    
    num_conexiones_ordenadas = dict(sorted(num_conexiones.items(), key=lambda x: x[1], reverse=True))


    for fila in num_conexiones_ordenadas.keys():        
        for elem in matriz_adyacencia[int(fila)]:
            nodo_color[f'elem']


    return num_conexiones, num_conexiones_ordenadas

print(colorear_grafos(np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])))