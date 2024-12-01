import random

class Mochila:
    def __init__(self, v, w, W, N):
        self.v = v
        self.w = w
        self.W = W
        self.N = N
        self.count = 0
        self.best_x = None
        self.best_v = -1
    
    def cota_optimista(self, x, i, v_acc, w_acc):
        # asumimos que puedo fraccionar el resto de objetos
        restante = self.W - w_acc
        indices = sorted(range(i, self.N), key=lambda j: v[j] / w[j], reverse = True) # LÏNEA MUY IMPORTANTE, ordena los indices en base al valor/peso que asocian
        for j in indices:
            if self.w[j] <= restante:
                v_acc += v[j]
                restante -= self.w[j]
            else:
                v_acc += self.v[j] + (restante / self.w[j])
                break
        return v_acc

    def __v_atras(self, x, i, w_acc, v_acc):
        self.count += 1
        if w_acc <= self.W and self.cota_optimista(x, i, v_acc, w_acc) > self.best_v: # factible y prometedor
            if i == self.N:
                # nodo hoja
                if v_acc > self.best_v: 
                    self.best_v = v_acc
                    self.best_x = x.copy()
            else:
                for o in [0, 1]:
                    x[i] = o
                    self.__v_atras(x, i+1, w_acc + x[i]*w[i], v_acc + x[i]*v[i])
    
    def voraz(self):
        indices = sorted(range(self.N), key=lambda j: v[j] / w[j], reverse = True) # LÏNEA MUY IMPORTANTE, ordena los indices en base al valor/peso que asocian
        x = [0] * self.N
        v_acc = 0
        w_acc = 0
        for i in indices:
            if self.w[i]+w_acc <= self.W:
                x[i] = 1
                v_acc += self.v[i]
                w_acc += self.w[i]
        return x, v_acc

    def resolver(self):
        x = [-1] * self.N
        i = 0
        self.best_x, self.best_v = self.voraz()
        self.__v_atras(x=x, i=i, w_acc = 0, v_acc = 0)



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
    print(f'Llamadas: {mochila.count}')

