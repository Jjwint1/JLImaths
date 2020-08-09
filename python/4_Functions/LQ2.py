import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(2, 100)

y = lambda n: 2*(n-2)**(2/3)

plt.plot(n, y(n), '-', color="#2D0000", lw=1)
plt.xlabel(r'$n$')
plt.ylabel(r'$y(n)$')
plt.savefig('../../figures/4_Functions/LQ2bii.png', dpi=600)
plt.close()

y = np.linspace(2, 100)

n = lambda y: 2 + (y/2)**(3/2)

plt.plot(y, n(y), '-', color="#2D0000", lw=1)
plt.xlabel(r'$y$')
plt.ylabel(r'$n(y)$')
plt.savefig('../../figures/4_Functions/LQ2biii.png', dpi=600)
plt.close()

m = np.linspace(0.001, 100, 1000000)

n = lambda m: m/4 + (16/m)**(1/2)

plt.plot(m, n(m), '-', color="#2D0000", lw=1)
plt.xlabel(r'$m$')
plt.ylabel(r'$n(m)$')
plt.savefig('../../figures/4_Functions/LQ2ci.png', dpi=600)


