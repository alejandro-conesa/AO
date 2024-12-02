import random
import color_grafos_voraz as voraz

class Grafo:
    def __init__(self, matriz, N):
        self.matriz = matriz
        self.N = N
        self.count = 0
        self.best_col = float("inf")
        self.best_x = None
        self.vecinos = self.calcular_vecinos()

    def calcular_vecinos(self):
        vecinos = []
        for i in range(len(self.matriz)):
            vecinos.append([x for x in self.matriz[i] if x == 1])
        return vecinos
            
    
    def factible(self, x):
        for nodo in range(self.N):
            for vecino in self.vecinos[nodo]:
                if x[nodo] == x[vecino] and x[vecino] != -1:
                    return False
        
        return True
    
    def vuelta_atras(self, x, i, col_acc):
        self.count += 1
        if self.factible(x) and col_acc + 1 <= self.best_col:
            if i == self.N:
                if col_acc < self.best_col:
                    self.best_x = x.copy()
                    self.best_col = col_acc
            else:
                for o in range(self.N):
                    x[i] = o
                    self.vuelta_atras(x, i+1, max(x))

    def resolver(self):
        x = [-1] * len(self.matriz)
        i = 0
        self.best_x, self.best_col = voraz.colorear_grafos(self.matriz)
        self.vuelta_atras(x, i, 0)   


adj_matrix = [
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0]
]

grafos = Grafo(adj_matrix, len(adj_matrix))
grafos.resolver()

print(grafos.best_x)
print(grafos.best_col)
print(grafos.count)