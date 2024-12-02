import quicksort

class Monedas:
    def __init__(self, M, C, N):
        self.M = M
        self.C = C
        self.N = N
        self.best_x = None
        self.best_c = float("inf")
        self.count = 0
    
    def v_atras(self, x, i, m_acc, c_acc):
        self.count += 1
        if m_acc <= self.M and self.cota_optimista(x, i, m_acc, c_acc) <= self.best_c:
            if i == self.N:
                if c_acc < self.best_c and m_acc == self.M:
                    self.best_x = x.copy()
                    self.best_c = c_acc
            else:
                max_monedas = int((self.M-m_acc)//self.C[i])
                if max_monedas > 0:
                    for o in range(max_monedas+1):
                        x[i] = o
                        self.v_atras(x, i+1, m_acc+o*self.C[i], c_acc+o)
                else:
                    x[i] = 0
                    self.v_atras(x, i+1, m_acc, c_acc)

    
    def voraz(self):
        indices = sorted(range(self.N), key = lambda j: self.C[j], reverse=True)
        suma = 0
        num_monedas = 0
        x = [0]*self.N

        for i in indices:
            x[i] = (self.M-suma)//self.C[i]
            num_monedas += int(x[i])
            suma += x[i]*self.C[i]
        
        return x, num_monedas

    def cota_optimista(self, x, i, m_acc, c_acc):
        return 0

    
    def resolver(self):
        x = [0]*self.N
        i = 0
        self.best_x, self.best_c = self.voraz()
        self.v_atras(x=x, i=i, m_acc=0, c_acc=0)


moneda = Monedas(1.3, [2, 1, 0.5, 0.2, 0.1], 5)
moneda.resolver()
print(moneda.best_x)
print(moneda.best_c)
print(moneda.count)
