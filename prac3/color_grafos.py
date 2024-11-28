import quicksort
import numpy as np

def colorear_grafos(matriz_adyacencia: np.array) -> int:
    lista_nodos = [] # cada lista en esta lista contiene el ID del nodo, una lista con sus conexiones y el color (número entero empezando por el 1)
    contador = 0
    for fila in matriz_adyacencia:
        lista_nodos.append([contador, [], 0]) # ID, lista conexiones, color
        for i in range(len(fila)):
            if fila[i] == 1:
                lista_nodos[contador][1].append(i)
        contador += 1
    
    # guardo dos listas, una por num de conexiones (ordenada) y otra por id
    lista_nodos_ordenada = sorted(lista_nodos, key=lambda x: len(x[1]), reverse=True)

    nodos_coloreados = []
    colores_usados = []
    for i in range(len(lista_nodos_ordenada)):
        min_color = float("inf")

        for id_conexion in lista_nodos_ordenada[i][1]:
            if lista_nodos[id_conexion][2] == lista_nodos_ordenada[i][2] and id_conexion in nodos_coloreados:
                if lista_nodos[id_conexion][2] < min_color:
                    min_color = lista_nodos[id_conexion][2]

        if min_color != float("inf"):
            lista_nodos_ordenada[i][2] = lista_nodos[id_conexion][2] + 1
            lista_nodos[lista_nodos_ordenada[i][0]][2] = lista_nodos_ordenada[i][2]

        nodos_coloreados.append(lista_nodos_ordenada[i][0])
        if lista_nodos_ordenada[i][2] not in colores_usados:
            colores_usados.append(lista_nodos_ordenada[i][2])

    return lista_nodos, len(colores_usados)

adj_matrix = [
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0]
]

ln, cu = colorear_grafos(np.array(adj_matrix))
print(ln)
print(cu)