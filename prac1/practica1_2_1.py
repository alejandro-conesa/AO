import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0, 10, 400)
y = np.sqrt(n)
plt.plot(n, y, label=r'$n^{1/2}$')

n = np.linspace(0, 1.5, 400)
y = 10**n
plt.plot(n, y, label=r'$10^n$')

n = np.linspace(0, 10, 400)
y = n**1.5
plt.plot(n, y, label=r'$n^{1.5}$') 

n = np.linspace(1, 10, 400)
y = 2*np.sqrt(np.log2(n))
plt.plot(n, y, label=r'$2 \cdot \sqrt{\log_2 n}$')

n = np.linspace(0, 4, 400)
y = n**2 * np.log2(n)
plt.plot(n, y, label=r'$n^2 \cdot \log_2 n$')

n = np.linspace(0, 5, 400)
y = 2**n
plt.plot(n, y, label=r'$2^n$')

'''
n = np.linspace(0, 0.01, 400)
y = n**(np.log2(n))
plt.plot(n, y, label=r'$n^{\log_2 n}$')
'''

n = np.linspace(0, 5.5, 400)
y = n**2
plt.plot(n, y, label=r'$n^2$')

n = np.linspace(0, 10, 400)
y = n
plt.plot(n, y, label=r'$2^{\log_2 n}$')

plt.title('Gráficas')
plt.xlabel('n')
plt.ylabel('f(n)')
plt.legend()
plt.grid(True)
plt.savefig('ej1.pdf')
