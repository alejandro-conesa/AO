import random

class Mochila:
    def __init__(self, v, w, W, N):
        self.v = v
        self.w = w
        self.W = W
        self.N = N
        self.best_x = None
        self.best_v = -1
    
    def __peso(self, x):
        p = 0
        for i in range(self.N):
            p += x[i]*self.w[i]
        return p

    def __valor(self, x):
        value = 0
        for i in range(self.N):
            value += x[i]*self.v[i]
        return value
    
    def __v_atras(self, x, i):
        if i == self.N:
            # nodo hoja
            if self.__peso(x) <= self.W: # factible
                self.best_v = self.__valor(x)
                self.best_x = x.copy()
        else:
            for o in [0, 1]:
                x[i] = o
                self.__v_atras(x, i+1)

    def resolver(self):
        x = [-1]*N
        i = 0
        self.__v_atras(x=x, i=i)



if __name__ == '__main__':
    random.seed(1)

    N = 5
    v = [random.randint(1,50) for _ in range(N)]
    w = [random.randint(1,50) for _ in range(N)]
    W = random.randint(N*1, N*25)

    mochila = Mochila(v, w, W, N)
    mochila.resolver()

    print(f'v = {v}')
    print(f'w = {w}')
    print(f'W = {W}')
    print(f'Solucion: {mochila.best_x}')
    print(f'Valor: {mochila.best_v}')

